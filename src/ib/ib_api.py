"""Base class for trading APIs."""
from typing import Dict, List

from src.base.base_api import BaseApi


class AlpacaApi(BaseApi):
    """Class for Alpaca API.

    This class is using the interactive broker api.
    For reference, please see:
    https://interactivebrokers.com/api/doc.html
    and
    https://www.interactivebrokers.com/en/trading/ib-api.php
    """

    def __init__(self, key_id: str, secret_key: str, base_url: str):
        """Class initialization function."""

    def get_account(self) -> Dict:
        """Get the account."""
        return None

    def submit_order(self) -> Dict:
        """Submit an order.
        Returns:
            Dict: a dictionary containing order information
        """
        return None

    def list_orders(self) -> List[Dict]:
        """List orders.

        Returns:
            List[Dict]: a list of dictionaries containing order information
        """
        return None

    def get_order(self, order_id: str) -> Dict:
        """Get an order with specific order_id."""
        return None

    def cancel_order(self, order_id: str) -> None:
        """Cancel an order with specific order_id."""

    def cancel_all_orders(self) -> None:
        """Cancel all orders."""

    def list_positions(self) -> List[Dict]:
        """Get a list of open positions."""
        return None

    def get_position(self, symbol: str) -> Dict:
        """Get an open position for a symbol."""
        return None

    def close_position(self, symbol: str) -> Dict:
        """Liquidates the position for the given symbol at market price."""
        return None

    def close_all_positions(self) -> List[Dict]:
        """Liquidates all open positions at market price."""
        return None
