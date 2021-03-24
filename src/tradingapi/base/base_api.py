"""Base class for trading APIs."""
import os
from abc import ABC, abstractmethod
from collections import OrderedDict
from typing import Any, Dict, List


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
    def get_account(self, **kwargs: Any) -> Dict:
        """Get the account."""
        pass

    @abstractmethod
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
            qty: quantity of shares
            side: buy or sell
            type: market, limit, stop, stop_limit
            limit_price: the limit price
            stop_price: the stop price
            **kwargs: Arbitrary keyword arguments.
        """
        pass

    @abstractmethod
    def list_orders(self, **kwargs: Any) -> List[Dict]:
        """Get a list with all orders."""
        pass

    @abstractmethod
    def get_order(self, order_id: str, **kwargs: Any) -> Dict:
        """Get an order with specific order_id."""
        pass

    @abstractmethod
    def cancel_order(self, order_id: str, **kwargs: Any) -> Dict:
        """Cancel an order with specific order_id."""
        pass

    @abstractmethod
    def cancel_all_orders(self, **kwargs: Any) -> List[Dict]:
        """Cancel all orders."""
        pass

    @abstractmethod
    def list_positions(self, **kwargs: Any) -> List[Dict]:
        """Get a list of open positions."""
        pass

    @abstractmethod
    def get_position(self, symbol: str, **kwargs: Any) -> Dict:
        """Get an open position for a symbol."""
        pass

    @abstractmethod
    def close_position(self, symbol: str, **kwargs: Any) -> Dict:
        """Liquidates the position for the given symbol at market price."""
        pass

    @abstractmethod
    def close_all_positions(self, **kwargs: Any) -> List[Dict]:
        """Liquidates all open positions at market price."""
        pass
