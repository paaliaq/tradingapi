"""Base class for trading APIs."""
from typing import Dict, List
import ib_insync as ibin

from src.base.base_api import BaseApi

# TODO test all functions
class IbApi(BaseApi):
    """Class for interactive broker API.

    This class use the package ib-insync for making asynchronous requests toward
    interactive broker trading work station (TWS) api.
    For reference of TWS, please see:
    https://interactivebrokers.github.io/tws-api/index.html
    and for ib-insync
    https://rawgit.com/erdewit/ib_insync/master/docs/html/readme.html
    """

    def __init__(self) -> None:
        """Class initialization function."""
        self.ib = ibin.IB()
        self.ib.connect('127.0.0.1', 4002, clientId=13)  # Ports

    def get_account(self) -> Dict:
        """Get the accounts associated with login."""
        accounts = self.ib.client.getAccounts()

        self.accounts = accounts

        return accounts

    def submit_order(self,
                     symbol: str,
                     currency: str,
                     qty: float = None,
                     side: str = None,
                     type: str = "MKT",
                     limit_price: float = None,
                     stop_price: float = None,
                     ) -> Dict:
        """Create and submit an order.

        Args:
            symbol: str = None, Selected asset for trade
            currency str = None, The assets underlying currency (traded in).
            qty: float, quantity bought or sold.
            side: str, "SELL" or "BUY", direction.
            type: str = "MKT", Can be one of "MKT" (Market), "LMT" (Limit),
            "STP" (Stop) or "STP_LIMIT" (stop limit)
            limit_price: float = None,
            stop_price: float = None,

        Returns:
            List[Dict]: A list containing the order, based of trade object.
        """
        # Define order according to dict
        order_dict = {
            "STP LMT": {"orderType": type, "totalQuantity": qty,
                        "AuxPrice": stop_price,
                        "LmtPrice": limit_price, "action": side},
            "STP": {"orderType": type, "totalQuantity": qty,
                    "AuxPrice": stop_price, "action": side},
            "LMT": {"orderType": type, "totalQuantity": qty,
                    "LmtPrice": limit_price, "action": side},
            "MKT": {"orderType": type, "totalQuantity": qty, "action": side},
        }
        order_definition = order_dict[type]
        order = ibin.order.Order(**order_definition)  # Place order

        # Define contract (which asset being traded)
        contract = ibin.Stock(symbol=symbol, exchange="SMART", currency=currency)

        # Place order, send request
        trade = self.ib.client.placeOrder(contract, order)

        # Confirm submission
        assert trade.orderStatus.status == 'Submitted'

        trade_dict = trade.dict()

        return trade_dict

    def list_orders(self) -> list[Dict]:
        """List orders.

        Returns:
            List[Dict]: a list of dictionaries containing order information
        """
        open_orders_dict = [x.dict() for x in self.ib.client.reqAllOpenOrders()]

        return open_orders_dict

    def get_order(self, order_id: str) -> Dict:
        """Get an order with specific order_id."""
        for x in self.ib.client.reqAllOpenOrders():
            if x.permId == int(order_id):  # Order id is unique
                order = x.dict()

        return order

    def cancel_order(self, order_id: str) -> Dict:
        """Cancel an order with specific order_id."""
        for x in self.ib.client.reqAllOpenOrders():
            if x.permId == int(order_id):  # Order id is unique
                order = x

        trade = self.ib.client.cancelOrder(order)  # Requires order object for cancellation

        trade_dict = trade.dict()

        return trade_dict

    def cancel_all_orders(self) -> List[Dict]:
        """Cancel all orders."""
        cancelled_orders = []
        for x in self.ib.reqAllOpenOrders():
            order = x
            trade = self.ib.client.cancelOrder(order)
            trade_dict = trade.dict()
            cancelled_orders.append(trade_dict)

        return cancelled_orders

    def list_positions(self) -> List[Dict]:
        """Get a list of open positions."""
        positions = []
        for x in range(0, len(self.ib.positions())):
            positions.append({"account": self.ib.positions()[x].account,
                              "contract": self.ib.positions()[x].contract.dict(),
                              "quantity": self.ib.positions()[x].position,
                              "avgCost": self.ib.positions()[x].avgCost})
        return positions

    def get_position(self, symbol: str) -> Dict:
        """Get an open position for a symbol."""
        positions = self.list_positions()

        for x in positions:
            if x["contract"]["symbol"] == symbol:
                position = x

        return position

    def close_position(self, symbol: str) -> Dict:
        """Liquidates the position for the given symbol at market price."""
        for x in range(0, len(self.ib.positions())):
            if self.ib.positions()[x].contract.symbol == symbol:
                old_contract = self.ib.positions()[x].contract
                position = self.ib.positions()[x].position

        # Define sell contract according to current contract/position
        new_contract = ibin.contract.Stock(conId=old_contract.conId)
        new_contract = self.ib.qualifyContracts(new_contract)  # Validates the contract

        # Place an order using a contract and order object.
        order = ibin.order.MarketOrder("SELL", position)
        trade = self.ib.client.placeOrder(new_contract[0], order)

        return trade.dict()

    def close_all_positions(self) -> List[Dict]:
        """Liquidates all open positions at market price."""
        closed_positions = []
        for x in range(0, len(self.ib.positions())):
            old_contract = self.ib.positions()[x].contract
            position = self.ib.positions()[x].position

            # Define sell contract according to current contract/position
            new_contract = ibin.Stock(conId=old_contract.conId)
            new_contract = self.ib.qualifyContracts(new_contract)  # Validates the contract

            # Place an order using a contract and order object.
            order = ibin.order.MarketOrder("SELL", position)
            trade = self.ib.client.placeOrder(new_contract, order)

            closed_positions.append(trade.dict())

        return closed_positions
