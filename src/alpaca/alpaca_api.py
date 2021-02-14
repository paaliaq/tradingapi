"""Base class for trading APIs."""
from typing import Dict, List

import alpaca_trade_api as tradeapi
from src.base.base_api import BaseApi


class AlpacaApi(BaseApi):
    """Class for Alpaca API.

    This class is based on alpaca-trade-api-python.
    For reference, please see: https://github.com/alpacahq/alpaca-trade-api-python
    """

    def __init__(self, env_dict: Dict) -> None:
        """Class initialization function."""
        super().__init__(env_dict)  # type: ignore
        self.api = tradeapi.REST()

    def get_account(self) -> Dict:
        """Get the account."""
        account = self.api.get_account()
        account_dict = account.__dict__["_raw"]
        return account_dict

    def submit_order(
        self,
        symbol: str,
        qty: int,
        side: str,
        type: str,
        time_in_force: str,
        limit_price: str = None,
        stop_price: str = None,
        extended_hours: bool = None,
        order_class: str = None,
        take_profit: dict = None,
        stop_loss: dict = None,
        trail_price: str = None,
        trail_percent: str = None,
    ) -> Dict:
        """Submit an order.

        Args:
            symbol: symbol or asset ID
            qty: int
            side: buy or sell
            type: market, limit, stop, stop_limit or trailing_stop
            time_in_force: day, gtc, opg, cls, ioc, fok
            limit_price: str of float
            stop_price: str of float
            extended_hours: bool. If true, order will be eligible to execute
                in premarket/afterhours.
            order_class: simple, bracket, oco or oto
            take_profit: dict with field "limit_price" e.g
                {"limit_price": "298.95"}
            stop_loss: dict with fields "stop_price" and "limit_price" e.g
                {"stop_price": "297.95", "limit_price": "298.95"}
            trail_price: str of float
            trail_percent: str of float

        Returns:
            Dict: a dictionary containing order information
        """
        order = self.api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=type,
            time_in_force=time_in_force,
            limit_price=limit_price,
            stop_price=stop_price,
            extended_hours=extended_hours,
            order_class=order_class,
            take_profit=take_profit,
            stop_loss=stop_loss,
            trail_price=trail_price,
            trail_percent=trail_percent,
        )
        order_dict = order.__dict__["_raw"]
        return order_dict

    def list_orders(
        self,
        status: str = None,
        limit: int = None,
        after: str = None,
        until: str = None,
        direction: str = None,
    ) -> List[Dict]:
        """List orders.

        Args:
            status: open, closed or all. Defaults to open.
            limit: Defaults to 50 and max is 500
            after: timestamp
            until: timestamp
            direction: asc or desc.

        Returns:
            List[Dict]: a list of dictionaries containing order information
        """
        order_list = self.api.list_orders(
            status=status, limit=limit, after=after, until=until, direction=direction
        )
        order_list = [order.__dict__["_raw"] for order in order_list]

        return order_list

    def get_order(self, order_id: str) -> Dict:
        """Get an order with specific order_id."""
        order = self.api.get_order(order_id=order_id)
        order_dict = order.__dict__["_raw"]
        return order_dict

    def cancel_order(self, order_id: str) -> None:
        """Cancel an order with specific order_id."""
        self.api.cancel_order(order_id=order_id)

    def cancel_all_orders(self) -> None:
        """Cancel all orders."""
        self.api.cancel_all_orders()

    def list_positions(self) -> List[Dict]:
        """Get a list of open positions."""
        position_list = self.api.list_positions()
        position_list = [position.__dict__["_raw"] for position in position_list]
        return position_list

    def get_position(self, symbol: str) -> Dict:
        """Get an open position for a symbol."""
        position = self.api.get_position(symbol=symbol)
        position_dict = position.__dict__["_raw"]
        return position_dict

    def close_position(self, symbol: str) -> Dict:
        """Liquidates the position for the given symbol at market price."""
        position = self.api.close_position(symbol=symbol)
        position_dict = position.__dict__["_raw"]
        return position_dict

    def close_all_positions(self) -> List[Dict]:
        """Liquidates all open positions at market price."""
        position_list = self.api.close_all_positions()
        position_list = [position.__dict__["_raw"] for position in position_list]
        return position_list
