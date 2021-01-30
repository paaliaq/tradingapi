"""Base class for trading APIs."""
from typing import Dict, List

import requests
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

    def get_accounts(self) -> Dict:
        """Get the accounts associated with login."""
        response = requests.get("https://localhost:5000/v1/api/portfolio/accounts",
                            verify=False)
        return response.json()[0]

    def get_portfolio(self, account_id, page = 0) -> Dict:
        """Get ."""
        return None

    def submit_order(self) -> Dict:
        """Submit an order.
        Returns:
            Dict: a dictionary containing order information
        """
        return None

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
        accounts = requests.get("https://localhost:5000/v1/api/iserver/accounts",
                              verify=False)
        response = requests.delete("https://localhost:5000/v1/api/iserver/account/" +
                                   account_id + "/order/" + order_id, verify=False)
        response_content = response.json()
        return response_content

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

    def extend_session(self) -> str:
        """Extends interactive session."""
        response = requests.post("https://localhost:5000/v1/api/tickle", verify=False)
        return response.status_code

    def end_session(self) -> str:
        """Extends interactive session."""
        response = requests.post("https://localhost:5000/v1/api/logout", verify=False)
        return response.status_code