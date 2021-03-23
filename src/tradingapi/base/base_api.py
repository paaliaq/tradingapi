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
        qty: float,
        side: str,
        type: str,
        currency: str,
        limit_price: float = None,
        stop_price: float = None,
    ) -> Dict:
        """Submit an order.

        Args:
            symbol: symbol or asset ID
            qty: int
            side: buy or sell
            type: market, limit, stop, stop_limit or trailing_stop
            limit_price: float
            stop_price: float
            currency:str, currency of traded exchange stock
        """
        pass

    @abstractmethod
    def list_orders(self) -> List[Dict]:
        """List orders.

        Args:
            Defaults to open.

        Returns:
            List[Dict]: a list of dictionaries containing order information
        """
        pass

    @abstractmethod
    def get_order(self, order_id: str) -> Dict:
        """Get an order with specific order_id."""
        pass

    @abstractmethod
    def cancel_order(self, order_id: str) -> Dict:
        """Cancel an order with specific order_id."""
        pass

    @abstractmethod
    def cancel_all_orders(self) -> List[Dict]:
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
