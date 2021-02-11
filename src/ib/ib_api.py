"""Base class for trading APIs."""
from typing import Dict, List
from ib_insync import *

from src.base.base_api import BaseApi


class IbApi(BaseApi):
    """Class for Alpaca API.

    This class is using the interactive broker api.
    For reference, please see:
    https://interactivebrokers.com/api/doc.html
    and
    https://www.interactivebrokers.com/en/trading/ib-api.php
    """

    def __init__(self):
        """Class initialization function."""
        ib = IB()
        ib.connect('127.0.0.1', 4002, clientId=13) # Todo change?

    def get_account(self) -> List:
        """Get the accounts associated with login."""
        accounts = ib.client.getAccounts()

        self.accounts = accounts

        return accounts

    def submit_order(self,
                     symbol: str = None,
                     currency: str = None,
                     qty: float = None,
                     side: str = None,
                     order_type: str = "MKT",
                     limit_price: float = None,
                     stop_price: float = None) -> List[Dict]:
        """Submit an order.

                Args:
                    symbol: str = None, Selected asset for trade

                    currency str = None, The underlying’s currency.

                    qty: float, quantity traded.

                    side: str, "SELL" or "BUY", direction.

                    order_type: str = "MKT", Can be one of "MKT" (Market), "LMT" (Limit),
                    "STP" (Stop) or "STP_LIMIT" (stop limit)

                    extended_hours: bool, If true, order will be eligible to execute
                    in premarket/afterhours.

                     limit_price: float = None,

                     stop_price: float = None,

                Returns:
                    List[Dict, Trade]: A list containing dictionary of trade and Trade object
                """

        # Define order according to dict
        order_dict = {
            "STP LMT": {"orderType": order_type, "totalQuantity": qty,
                        "AuxPrice": stop_price,
                        "LmtPrice": limit_price, "action": side},
            "STP": {"orderType": order_type, "totalQuantity": qty,
                    "AuxPrice": stop_price, "action": side},
            "LMT": {"orderType": order_type, "totalQuantity": qty,
                    "LmtPrice": limit_price, "action": side},
            "MKT": {"orderType": order_type, "totalQuantity": qty, "action": side},
        }

        order_definition = order_dict[order_type]

        order = Order(**order_definition)

        # Define contract (which asset)
        contract = Stock(symbol=symbol, exchange="SMART", currency=currency)

        # Place order, send request
        trade = ib.placeOrder(contract, order)

        # Confirm submission
        assert trade.orderStatus.status == 'Submitted'

        trade_dict = trade.dict()

        return [trade_dict, trade]

    def list_orders(self) -> list[Dict, ]:
        """List orders.
        Returns:
            List[Dict]: a list of dictionaries containing order information
        """
        open_orders_dict = [x.dict() for x in ib.reqAllOpenOrders()]

        return open_orders_dict

    def get_order(self, order_id: str) -> Dict:
        """Get an order with specific order_id."""
        for x in ib.reqAllOpenOrders():
            if x.permId == int(order_id):  # This is is unqiue
                order = x.dict()

        return order

    def cancel_order(self, order_id: str) -> Dict:
        """Cancel an order with specific order_id.
        """
        for x in ib.reqAllOpenOrders():
            if x.permId == int(order_id):
                order = x

        trade = ib.cancelOrder(order)

        trade_dict = trade.dict()

        return trade_dict

    def cancel_all_orders(self) -> List[Dict]:
        """Cancel all orders."""
        cancelled_orders = []
        for x in ib.reqAllOpenOrders():
            order = x
            trade = ib.cancelOrder(order)
            trade_dict = trade.dict()
            cancelled_orders.append(trade_dict)

        return cancelled_orders

    def list_positions(self) -> List[Dict]:
        """Get a list of open positions."""
        positions = []
        for x in range(0, len(ib.positions())):
            positions.append({"account": ib.positions()[x].account,
                              "contract": ib.positions()[x].contract.dict(),
                              "quantity": ib.positions()[x].position,
                              "avgCost": ib.positions()[x].avgCost})
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
        for x in range(0, len(ib.positions())):
            if ib.positions()[x].contract.symbol == symbol:
                old_contract = ib.positions()[x].contract
                position = ib.positions()[x].position

        # Define sell contract according to current contract/position
        new_contract = Stock(conId=old_contract.conId)
        new_contract = ib.qualifyContracts(new_contract)

        order = MarketOrder("SELL", position)
        trade = ib.placeOrder(new_contract[0], order)

        return trade.dict()

    def close_all_positions(self) -> List[Dict]:
        """Liquidates all open positions at market price."""
        self.list_positions() # Extract specific one

        return None

    def extend_session(self) -> str:
        """Extends interactive session."""
        response = requests.post("https://localhost:5000/v1/api/tickle", verify=False)
        return response.status_code

    def end_session(self):
        """Extends interactive session."""
        ib.disconnect()
