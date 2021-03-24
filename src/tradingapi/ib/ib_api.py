"""Base class for trading APIs."""
from typing import Dict, List
import ib_insync as ibin
import collections

from tradingapi.base.base_api import BaseApi


class IbApi(BaseApi):
    """Class for interactive broker API.

    This class use the package ib-insync for making asynchronous requests toward
    interactive broker trading work station (TWS) api.
    For reference of TWS, please see :
    https://interactivebrokers.github.io/tws-api/index.html
    and for ib-insync
    https://rawgit.com/erdewit/ib_insync/master/docs/html/readme.html
    """

    def __init__(self) -> None:
        """Class initialization function."""
        self.ib = ibin.ib.IB()
        self.ib.connect("127.0.0.1", 4002, clientId=13)  # Ports

    def get_account(self) -> Dict:
        """Get the accounts associated with login."""
        accounts_summaries = self.ib.accountSummary()

        account = {}
        for account_summary in accounts_summaries:
            if account_summary.account != "ALL":
                tag = account_summary.tag
                value = account_summary.value
                account[tag] = value

        self.account = account

        return account

    def submit_order(
        self,
        symbol: str,
        qty: float,
        side: str,
        type: str,
        currency: str,
        limit_price: float = None,
        stop_price: float = None,
        **kwargs: Any
    ) -> Dict:
        """Create and submit an order.

        Args:
            symbol: str, Selected asset for trade
            qty: float, quantity bought or sold.
            side: str, "SELL" or "BUY", direction.
            type: str, Can be one of "MKT" (Market), "LMT" (Limit),
                "STP" (Stop) or "STP_LIMIT" (stop limit).
            limit_price: the limit price
            stop_price: the stop price

        Returns:
            Dict: A list containing the order, based of trade object.
        """
        # Initialize default kwargs if necessary
        if "currency" not in kwargs:
            currency = "USD"

        # Define order according to dict
        order_dict = {
            "STP LMT": {
                "orderType": type,
                "totalQuantity": qty,
                "auxPrice": stop_price,
                "lmtPrice": limit_price,
                "action": side,
            },
            "STP": {
                "orderType": type,
                "totalQuantity": qty,
                "auxPrice": stop_price,
                "action": side,
            },
            "LMT": {
                "orderType": type,
                "totalQuantity": qty,
                "lmtPrice": limit_price,
                "action": side,
            },
            "MKT": {"orderType": type, "totalQuantity": qty, "action": side},
        }
        order_definition = collections.OrderedDict(order_dict[type])  # mypy workaround

        order = ibin.Order(**order_definition)  # Place order

        # Define contract (which asset being traded)
        contract = ibin.Stock(symbol=symbol, exchange="SMART", currency=currency)

        # Place order, send request
        trade = self.ib.placeOrder(contract=contract, order=order).__dict__

        # Confirm submission
        self.ib.sleep(2)
        assert order in self.ib.orders()

        trade_dict = trade.__dict__

        return trade_dict

    def list_orders(self, **kwargs: Any) -> List[Dict]:
        """Get a list with all orders."""
        open_orders_dict = [x.__dict__ for x in self.ib.reqAllOpenOrders()]

        return open_orders_dict

    def get_order(self, order_id: str, **kwargs: Any) -> Dict:
        """Get an order with specific order_id."""
        open_orders = self.ib.reqAllOpenOrders()
        for order in open_orders:
            if order.permId == int(order_id):  # Order id is unique
                order_dict = order.__dict__

        if "order_dict" not in locals():
            print("Order doesn't exist!")
            order_dict = {}

        return order_dict

    def cancel_order(self, order_id: str, **kwargs: Any) -> Dict:
        """Cancel an order with specific order_id."""
        open_orders = self.ib.reqAllOpenOrders()
        for order in open_orders:
            if order.permId == int(order_id):  # Order id is unique
                trade = self.ib.cancelOrder(order)
                trade_dict = trade.__dict__
        if "trade_dict" not in locals():
            print("Order doesn't exist!")
            trade_dict = {}

        return trade_dict

    def cancel_all_orders(self, **kwargs: Any) -> List[Dict]:
        """Cancel all orders."""
        cancelled_orders = []
        open_orders = self.ib.reqAllOpenOrders()
        for order in open_orders:
            trade = self.ib.cancelOrder(order)
            trade_dict = trade.__dict__
            cancelled_orders.append(trade_dict)

        return cancelled_orders

    def list_positions(self, **kwargs: Any) -> List[Dict]:
        """Get a list of open positions."""
        positions = []
        for x in range(0, len(self.ib.positions())):
            positions.append(
                {
                    "account": self.ib.positions()[x].account,
                    "contract": self.ib.positions()[x].contract.__dict__,
                    "quantity": self.ib.positions()[x].position,
                    "avgCost": self.ib.positions()[x].avgCost,
                }
            )
        return positions

    def get_position(self, symbol: str, **kwargs: Any) -> Dict:
        """Get an open position for a symbol."""
        positions = self.list_positions()

        for x in positions:
            if x["contract"]["symbol"] == symbol:
                position = x

        if "position" not in locals():
            print("Position for symbol doesn't exist!")
            position = {}

        return position

    def close_position(self, symbol: str, **kwargs: Any) -> Dict:
        """Liquidates the position for the given symbol at market price."""
        for x in range(0, len(self.ib.positions())):
            if self.ib.positions()[x].contract.symbol == symbol:
                old_contract = self.ib.positions()[x].contract
                position = self.ib.positions()[x].position

        if "position" not in locals():
            print("Position for symbol doesn't exist!")
            return {}

        # Define sell contract according to current contract/position
        new_contract = ibin.Stock(conId=old_contract.conId)
        self.ib.qualifyContracts(new_contract)  # Validates the contract

        # Place an order using a contract and order object.
        order = ibin.MarketOrder("SELL", position)
        trade = self.ib.placeOrder(contract=new_contract, order=order)
        assert order in self.ib.orders()

        return trade.__dict__

    def close_all_positions(self, **kwargs: Any) -> List[Dict]:
        """Liquidates all open positions at market price."""
        closed_positions = []
        for x in range(0, len(self.ib.positions())):
            old_contract = self.ib.positions()[x].contract
            position = self.ib.positions()[x].position

            if "position" not in locals():
                print("No positions to close!")
                return [{}]

            # Define sell contract according to current contract/position
            new_contract = ibin.Stock(conId=old_contract.conId)
            self.ib.qualifyContracts(new_contract)  # Validates the contract

            # Place an order using a contract and order object.
            order = ibin.order.MarketOrder("SELL", position)
            trade = self.ib.placeOrder(new_contract, order)

            closed_positions.append(trade.__dict__)

        return closed_positions
