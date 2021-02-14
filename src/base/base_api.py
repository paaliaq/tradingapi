"""Base class for trading APIs."""
import os
from abc import ABC, abstractmethod
from collections import OrderedDict
from typing import Dict, List


class BaseApi(ABC):
    """Base class for trading APIs.

    This class was inspired by the methods from alpaca-trade-api-python.
    For reference, please see: https://github.com/alpacahq/alpaca-trade-api-python
    """

    def __init__(self, env_dict: Dict) -> None:
        """Class initialization function."""
        # Check inputs
        is_dict = isinstance(env_dict, dict) or isinstance(env_dict, OrderedDict)
        if not is_dict:
            raise ValueError("env_dict must be a dictionary.")

        values_are_strings = all([isinstance(v, str) for v in env_dict.values()])
        if not values_are_strings:
            raise ValueError("All values in env_dict must be strings.")

        # Set environment variables
        for k, v in env_dict.items():
            os.environ[k] = v

    @abstractmethod
    def get_account(self) -> Dict:
        """Get the account."""
        pass

    @abstractmethod
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
        """
        pass

    @abstractmethod
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
        pass

    @abstractmethod
    def get_order(self, order_id: str) -> Dict:
        """Get an order with specific order_id."""
        pass

    @abstractmethod
    def cancel_order(self, order_id: str) -> None:
        """Cancel an order with specific order_id."""
        pass

    @abstractmethod
    def cancel_all_orders(self) -> None:
        """Cancel all orders."""
        pass

    @abstractmethod
    def list_positions(self) -> List[Dict]:
        """Get a list of open positions."""
        pass

    @abstractmethod
    def get_position(self, symbol: str) -> Dict:
        """Get an open position for a symbol."""
        pass

    @abstractmethod
    def close_position(self, symbol: str) -> Dict:
        """Liquidates the position for the given symbol at market price."""
        pass

    @abstractmethod
    def close_all_positions(self) -> List[Dict]:
        """Liquidates all open positions at market price."""
        pass
