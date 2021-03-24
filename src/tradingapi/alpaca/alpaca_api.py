"""Base class for trading APIs."""
from typing import Any, Dict, List

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
        limit_price: str = None,
        stop_price: str = None,
        **kwargs: Any
    ) -> Dict:
        """Submit an order.

        Args:
            symbol: symbol or asset ID
            qty: int
            side: buy or sell
            type: market, limit, stop, stop_limit or trailing_stop
            limit_price: str of float
            stop_price: str of float
            **kwargs: Arbitrary keyword arguments, among them for instance:
                time_in_force: day, gtc, opg, cls, ioc, fok
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
        # Initialize default kwargs if necessary
        if "time_in_force" not in kwargs:
            time_in_force = "day"
        if "extended_hours" not in kwargs:
            extended_hours = None
        if "order_class" not in kwargs:
            order_class = None
        if "take_profit" not in kwargs:
            take_profit = None
        if "stop_loss" not in kwargs:
            stop_loss = None
        if "trail_price" not in kwargs:
            trail_price = None
        if "trail_percent" not in kwargs:
            trail_percent = None

        # Submit order
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

    def list_orders(self, **kwargs: Any) -> List[Dict]:
        """List orders.

        Args:
            **kwargs: Arbitrary keyword arguments, among them the following:
                status: open, closed or all. Defaults to open.
                limit: Defaults to 50 and max is 500
                after: timestamp
                until: timestamp
                direction: asc or desc

        Returns:
            List[Dict]: a list of dictionaries containing order information
        """
        # Initialize default kwargs if necessary
        if "status" not in kwargs:
            status = None
        if "limit" not in kwargs:
            limit = None
        if "after" not in kwargs:
            after = None
        if "until" not in kwargs:
            until = None
        if "direction" not in kwargs:
            direction = None

        order_list = self.api.list_orders(
            status=status, limit=limit, after=after, until=until, direction=direction
        )
        order_list = [order.__dict__["_raw"] for order in order_list]

        return order_list

    def get_order(self, order_id: str, **kwargs: Any) -> Dict:
        """Get an order with specific order_id."""
        order = self.api.get_order(order_id=order_id)
        order_dict = order.__dict__["_raw"]
        return order_dict

    def cancel_order(self, order_id: str, **kwargs: Any) -> None:
        """Cancel an order with specific order_id."""
        self.api.cancel_order(order_id=order_id)

    def cancel_all_orders(self, **kwargs: Any) -> None:
        """Cancel all orders."""
        self.api.cancel_all_orders()

    def list_positions(self, **kwargs: Any) -> List[Dict]:
        """Get a list of open positions."""
        position_list = self.api.list_positions()
        position_list = [position.__dict__["_raw"] for position in position_list]
        return position_list

    def get_position(self, symbol: str, **kwargs: Any) -> Dict:
        """Get an open position for a symbol."""
        position = self.api.get_position(symbol=symbol)
        position_dict = position.__dict__["_raw"]
        return position_dict

    def close_position(self, symbol: str, **kwargs: Any) -> Dict:
        """Liquidates the position for the given symbol at market price."""
        position = self.api.close_position(symbol=symbol)
        position_dict = position.__dict__["_raw"]
        return position_dict

    def close_all_positions(self, **kwargs: Any) -> List[Dict]:
        """Liquidates all open positions at market price."""
        position_list = self.api.close_all_positions()
        position_list = [position.__dict__["_raw"] for position in position_list]
        return position_list
