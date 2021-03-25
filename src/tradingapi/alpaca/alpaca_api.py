"""Base class for trading APIs."""
from typing import Any, Dict, List, Union

import alpaca_trade_api as tradeapi
from tradingapi.base.base_api import BaseApi


class AlpacaApi(BaseApi):
    """Class for Alpaca API.

    This class is based on alpaca-trade-api-python.
    For reference, please see: https://github.com/alpacahq/alpaca-trade-api-python
    """

    def __init__(self, env_dict: Dict) -> None:
        """Class initialization function."""
        super().__init__(env_dict)  # type: ignore
        self.api = tradeapi.REST()

    def get_account(self, **kwargs: Any) -> Dict:
        """Get the account."""
        account = self.api.get_account()
        account_dict = account.__dict__["_raw"]
        return account_dict

    def _handle_kwargs_submit_order(self, **kwargs: Any) -> Dict:
        """Function to initialize missing kwargs for submit_order function."""
        # Initialize default kwargs if necessary
        if "time_in_force" not in kwargs:
            kwargs["time_in_force"] = "day"
        if "extended_hours" not in kwargs:
            kwargs["extended_hours"] = None
        if "take_profit" not in kwargs:
            kwargs["take_profit"] = None
        if "stop_loss" not in kwargs:
            kwargs["stop_loss"] = None
        if "trail_price" not in kwargs:
            kwargs["trail_price"] = None
        if "trail_percent" not in kwargs:
            kwargs["trail_percent"] = None
        return kwargs

    def submit_order(
        self,
        symbol: str,
        qty: int,
        side: str,
        type: str,
        limit_price: float = None,
        stop_price: float = None,
        **kwargs: Any
    ) -> Dict:
        """Submit an order.

        Args:
            symbol: symbol or asset ID
            qty: int
            side: "SELL" or "BUY"
            type: can be one of "MKT" (Market), "LMT" (Limit),
                "STP" (Stop) or "STP_LIMIT" (stop limit)
            limit_price: the limit price
            stop_price: the stop price
            **kwargs: Arbitrary keyword arguments, among them for instance:
                time_in_force (str = "day"): day, gtc, opg, cls, ioc, fok
                extended_hours (bool = None): bool. If true, order will be eligible to
                    execute in premarket/afterhours.
                take_profit (dict = None): dict with field "limit_price" e.g
                    {"limit_price": "298.95"}
                stop_loss (dict = None): dict with fields "stop_price" and "limit_price"
                    e.g {"stop_price": "297.95", "limit_price": "298.95"}
                trail_price (str = None): str of float
                trail_percent (str = None): str of float

        Returns:
            Dict: a dictionary containing order information
        """
        # Handle kwargs
        kwargs = self._handle_kwargs_submit_order(**kwargs)

        # Checking categorical input arguments
        valid_side = {"BUY": "buy", "SELL": "sell"}
        if side not in valid_side:
            raise ValueError("'side' needs to be in {}".format(valid_side))
        valid_type = {
            "MKT": "market",
            "LMT": "limit",
            "STP": "stop",
            "STP_LIMIT": "stop_limit",
        }
        if type not in valid_type:
            raise ValueError("'type' needs to be in {}".format(valid_type.keys()))
        valid_time_in_force = {"day", "gtc", "opg", "cls", "ioc", "fok"}
        if kwargs["time_in_force"] not in valid_time_in_force:
            raise ValueError(
                "'time_in_force' needs to be in {}".format(valid_time_in_force)
            )

        # Mapping arguments
        side = valid_side[side]
        type = valid_type[type]

        # Special formatting
        if limit_price is not None:
            limit_price_adj: Union[str, None] = str(limit_price)
        else:
            limit_price_adj = None
        if stop_price is not None:
            stop_price_adj: Union[str, None] = str(stop_price)
        else:
            stop_price_adj = None

        # Submit order
        order = self.api.submit_order(
            symbol=symbol,
            qty=qty,
            side=side,
            type=type,
            limit_price=limit_price_adj,
            stop_price=stop_price_adj,
            # kwargs
            time_in_force=kwargs["time_in_force"],
            extended_hours=kwargs["extended_hours"],
            take_profit=kwargs["take_profit"],
            stop_loss=kwargs["stop_loss"],
            trail_price=kwargs["trail_price"],
            trail_percent=kwargs["trail_percent"],
        )
        order_dict = order.__dict__["_raw"]
        return order_dict

    def list_orders(self, **kwargs: Any) -> List[Dict]:
        """List orders.

        Args:
            **kwargs: Arbitrary keyword arguments, among them the following:
                status (str = "open"): open, closed or all. Defaults to open.
                limit (int = 50): Defaults to 50 and max is 500
                after: timestamp
                until: timestamp
                direction: asc or desc

        Returns:
            List[Dict]: a list of dictionaries containing order information
        """
        # Initialize default kwargs if necessary
        if "status" not in kwargs:
            status = "open"
        else:
            status = kwargs["status"]
        if "limit" not in kwargs:
            limit = 50
        else:
            limit = kwargs["limit"]
        if "after" not in kwargs:
            after = None
        else:
            after = kwargs["after"]
        if "until" not in kwargs:
            until = None
        else:
            until = kwargs["until"]
        if "direction" not in kwargs:
            direction = None
        else:
            direction = kwargs["direction"]

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

    def cancel_order(self, order_id: str, **kwargs: Any) -> Dict:
        """Cancel an order with specific order_id."""
        self.api.cancel_order(order_id=order_id)
        return {}  # Dummy return statement since alpaca does not return anything

    def cancel_all_orders(self, **kwargs: Any) -> List[Dict]:
        """Cancel all orders."""
        self.api.cancel_all_orders()
        return [{}]  # Dummy return statement since alpaca does not return anything

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
