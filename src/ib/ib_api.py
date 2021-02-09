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
        ib.connect('127.0.0.1', 4002, clientId=13)

    def get_account(self) -> Dict:
        """Get the accounts associated with login."""
        response = requests.get("https://localhost:5000/v1/api/portfolio/accounts",
                            verify=False)
        return response.json()[0]

    def submit_order(self,
                     account_id: str,
                     con_id: str,
                     qty: float,
                     side: str,
                     customer_order_id: str = "test",
                     parent_order_id: str = None,
                     sector_type: str = "STK",
                     extended_hours: bool = False,
                     order_type: str = "MKT",
                     price: float = None,
                     symbol: str = None,
                     time_in_force: str = "DAY") -> List[Dict]:
        """Submit an order.

        Args:
            account_id: str = None, Optional.
            It should be one of the accounts returned by /iserver/accounts.
            If not passed, the first one in the list is selected.

            con_id: str, is the identifier of the security you want to trade,
            you can find the conid with /iserver/secdef/search.

            sector_type: str, conid:type for example 265598:STK

            customer_order_id: str, Arbitraty string that can be used to identify the order,
            e.g "my-fb-order"

            parent_order_id: str, When placing bracket orders,
            the child parentId must be equal to the cOId (customer order id) of the parent.

            order_type: str = "MKT", Can be one of "MKT" (Market), "LMT" (Limit),
            "STP" (Stop) or "STP_LIMIT" (stop limit)

            extended_hours: bool, If true, order will be eligible to execute
            in premarket/afterhours.

            price: float = None, Optional if order is "MKT",
            for "LMT", this is the limit price. For "STP" this is the stop price.

            side: str, "SELL" or "BUY"

            symbol: str = None, Called  ticker in api doc.

            time_in_force: str, "GTC" (Good Till Cancel) or "DAY".
            DAY orders are automatically cancelled at the end of the Day or Trading hours.

            qty: float, quantity bought

        Returns:
            List[Dict,Dict]: A list of dictionary containing order information and
            dictionary of response
        """

        order_body = {
            # acctId is optional.
            # It should be one of the accounts returned by /iserver/accounts.
            # If not passed, the first one in the list is selected.
            "acctId": account_id,

            # conid is the identifier of the security you want to trade,
            # you can find the conid with /iserver/secdef/search.
            "conid": con_id,

            # conid:type for example 265598:STK
            "secType": sector_type,

            # Customer Order ID.
            # An arbitraty string that can be used to identify the order,
            # e.g "my-fb-order". The value must be unique for a 24h span.
            # Please do not set this value for child orders when placing a
            # bracket order.
            "cOID": customer_order_id,

            # When placing bracket orders,
            # the child parentId must be equal to the cOId (customer order id)
            # of the parent.
            "parentId": parent_order_id,

            # orderType can be one of MKT (Market), LMT (Limit),
            # STP (Stop) or STP_LIMIT (stop limit)
            "orderType": order_type,

            # listingExchange is optional. By default we use "SMART" routing.
            # Possible values are available via this end point:
            # /v1/portal/iserver/contract/{{conid}}/info,
            # see valid_exchange: e.g:
            # SMART,AMEX,NYSE, CBOE,ISE,CHX,ARCA,ISLAND,DRCTEDGE,BEX,BATS,EDGEA,
            # CSFBALGO,JE FFALGO,BYX,IEX,FOXRIVER,TPLUS1,NYSENAT,PSX
            "listingExchange": "SMART",

            # set to true if the order can be executed outside regular trading hours.
            "outsideRTH": extended_hours,

            # optional if order is MKT, for LMT, this is the limit price.
            # For STP this is the stop price.
            "price": price,

            # SELL or BUY
            "side": side,

            "ticker": symbol,

            # GTC (Good Till Cancel) or DAY.
            # DAY orders are automatically cancelled at the end of the Day or
            # Trading hours.
            "tif": time_in_force,

            # for example QuickTrade
            "referrer": "QuickTrade",

            # usually integer, for some special cases can be float numbers
            "quantity": qty,

            # double number,
            # this is the cash quantity field which can only be used for
            # FX conversion order.
            "fxQty": 0,

            # If true, the system will use the Adaptive Algo to submit the order
            # https://www.interactivebrokers.com/en/index.php?f=19091
            "useAdaptive": False,

            # set to true if the order is a FX conversion order
            "isCurrencyConversion": False,

            # Set the allocation method when placing an order using an FA account
            # for a group Possible allocation methods are "NetLiquidity",
            # "AvailableEquity", "EqualQuantity" and "PctChange".
            "allocationMethod": None
        }

        order_response = requests.post("https://localhost:5000/v1/api/iserver/account/" +
                                      account_id + "/order", verify=False,
                                      data=order_body)
        order_response = order_response.json()

        return [order_body, order_response]

    def list_orders(self) -> Dict:
        """List orders.
        Returns:
            List[Dict]: a list of dictionaries containing order information
        """
        response = requests.get("https://localhost:5000/v1/api/iserver/account/orders",
                              verify=False)
        orders = response.json()["orders"]

        return orders

    def get_order(self, order_id: str) -> Dict:
        """Get an order with specific order_id."""
        return None

    def cancel_order(self, order_id: str, account_id: str) -> Dict:
        """Cancel an order with specific order_id."""
        #  Must call /iserver/accounts endpoint prior to cancelling an order.
        requests.get("https://localhost:5000/v1/api/iserver/accounts",
                              verify=False)
        response = requests.delete("https://localhost:5000/v1/api/iserver/account/" +
                                   account_id + "/order/" + order_id, verify=False)
        response_content = response.json()
        return response_content

    def cancel_all_orders(self) -> None:
        """Cancel all orders."""

    def list_positions(self) -> Position:
        """Get a list of open positions."""
        positions = ib.positions()

        return positions

    def get_position(self, symbol: str) -> Dict:
        """Get an open position for a symbol."""
        return None

    def close_position(self, symbol: str) -> Dict:
        """Liquidates the position for the given symbol at market price."""
        self.list_positions() # Extract specific one
        self.submit_order()
        return None

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
