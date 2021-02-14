"""Base class for trading APIs."""
from abc import ABC, abstractmethod
from typing import Dict, List


class BaseApi(ABC):
    """Base class for trading APIs.

    This class was inspired by the methods from alpaca-trade-api-python.
    For reference, please see: https://github.com/alpacahq/alpaca-trade-api-python
    """

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
        limit_price: str = None,
        stop_price: str = None,
        currency: str = None
    ) -> Dict:
        """Submit an order.

        Args:
            symbol: symbol or asset ID
            qty: int
            side: buy or sell
            type: market, limit, stop, stop_limit or trailing_stop
            limit_price: str of float
            stop_price: str of float
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
