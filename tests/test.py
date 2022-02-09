import unittest
from unittest.mock import Mock

import aiounittest
from testfixtures import compare

import testhelpers.data_helper as dh
from tradingapi.alpaca.alpaca_api import AlpacaApi


class AlpacaTests(aiounittest.AsyncTestCase):
    api_settings = {
        "APCA_API_KEY_ID": "PK8HDG7R05LLSH8YM25W",
        "APCA_API_SECRET_KEY": "tthYbkvPYymnDuQJDYsdmfZ7v9lFmec2KRal0tYF",
        "APCA_API_BASE_URL": "https://paper-api.alpaca.markets",
        "APCA_RETRY_MAX": "3"
    }

    def setUp(self) -> None:
        # Instantiate the wrapper api and patch a mock method for expected results
        self.alpaca_api = AlpacaApi(self.api_settings)
        self.alpaca_api.api = Mock()

    async def test_get_clock_ok(self):
        """Test the clock method."""

        # Import the fake api call that is going to be sent in to wrapper function
        self.alpaca_api.api.get_clock.return_value = dh.import_api_get_clock()

        # Run method tested
        clock = await self.alpaca_api.get_clock()

        # Import the expected results after wrapper function has been applied
        expected_clock = dh.import_expected_get_clock()

        # Compare objects and verify test results
        compare(clock, expected_clock, prefix="Expected clock object is different.")

    async def test_get_account(self):
        """Test the get account method."""

        self.alpaca_api.api.get_account.return_value = dh.import_api_get_account()
        account = await self.alpaca_api.get_account()
        # expected_account = dh.import_expected_get_account_pydantic()
        # compare(account, expected_account, prefix="Expected account object is different.")

    async def test_cancel_all_orders(self):
        """Test the get cancel all orders method."""

        # self.alpaca_api.api.cancel_all_orders.return_value = dh.import_api_cancel_all_orders()
        # canceled_orders = await self.alpaca_api.cancel_all_orders()
        # expected_canceled_orders = dh.import_expected_cancel_all_orders()
        # compare(canceled_orders, expected_canceled_orders, prefix="Expected canceled order object is different.")

        pass

    async def test_submit_order(self):
        """Test the submit order method."""

        # self.alpaca_api.api.submit_order.return_value = dh.import_api_submit_order()
        # order = await self.alpaca_api.submit_order()
        # expected_order = dh.import_expected_submit_order()
        # compare(order, expected_order, prefix="Expected order object is different.")

        pass

    async def test_list_orders(self):
        """Test the list orders method."""

        # self.alpaca_api.api.list_orders.return_value = dh.import_api_list_orders()
        # orders = await self.alpaca_api.list_orders()
        # expected_orders = dh.import_expected_list_orders()
        # compare(orders, expected_orders, prefix="Expected orders object is different.")

        pass

    async def test_get_order(self):
        """Test the get order method."""

        # self.alpaca_api.api.get_order.return_value = dh.import_api_get_order()
        # order = await self.alpaca_api.get_order()
        # expected_order = dh.import_expected_get_order()
        # compare(order, expected_order, prefix="Expected order object is different.")

        pass

    async def test_cancel_order(self):
        """Test the cancel order method."""

        # self.alpaca_api.api.cancel_order.return_value = dh.import_api_cancel_order()
        # canceled_order = await self.alpaca_api.cancel_order()
        # expected_cancel_order= dh.import_expected_cancel_order()
        # compare(canceled_order, expected_cancel_order, prefix="Expected canceled order object is different.")

        pass

    async def test_cancel_all_orders(self):
        """Test the cancel all orders method."""

        # self.alpaca_api.api.cancel_all_orders.return_value = dh.import_api_cancel_all_orders()
        # canceled_orders = await self.alpaca_api.cancel_all_orders()
        # expected_canceled_orders = dh.import_expected_cancel_all_orders()
        # compare(canceled_orders, expected_canceled_orders, prefix="Expected canceled orders object is different.")
        pass

    async def test_submit_order(self):
        """Test the submit order method."""

        # self.alpaca_api.api.submit_order.return_value = dh.import_api_submit_order()
        # order = await self.alpaca_api.submit_order()
        # expected_order = dh.import_expected_submit_order()
        # compare(order, expected_order, prefix="Expected order object is different.")

        pass

    async def test_list_positions(self):
        """Test the list positions method."""

        # self.alpaca_api.api.list_positions.return_value = dh.import_api_list_positions()
        # positions = await self.alpaca_api.list_positions()
        # expected_order = dh.import_expected_list_positions()
        # compare(order, expected_order, prefix="Expected order object is different.")

        pass

    async def test_get_position(self):
        """Test the get position method."""

        # self.alpaca_api.api.get_position.return_value = dh.import_api_get_position()
        # position = await self.alpaca_api.get_position()

        pass

    async def test_close_position(self):
        """Test the close position method."""

        # self.alpaca_api.api.close_position.return_value = dh.import_api_close_position()
        # closed_position = await self.alpaca_api.close_position()

        pass

    async def test_close_all_positions(self):
        """Test the close all positions method."""

        # self.alpaca_api.api.close_all_positions.return_value = dh.import_api_close_all_positions()
        # closed_positions = await self.alpaca_api.close_all_positions()

        pass

    async def test_get_trading_days(self):
        """Test the get trading days method."""

        # self.alpaca_api.api.get_trading_days.return_value = dh.import_api_get_trading_days()
        # trading_days = await self.alpaca_api.get_trading_days()

        pass


if __name__ == '__main__':
    unittest.main()

# clock = await api.get_clock()

# account = await api.get_account()
# await api.cancel_all_orders()
# tsla_stop_limit_order = await api.submit_order(
# my_orders = await api.list_orders()
## tsla_stop_limit_order_dupe = api.api.get_order(order_id=tsla_stop_limit_order.id)
# tsla_stop_limit_order_dupe = await api.get_order(order_id=tsla_stop_limit_order.id)
# await api.cancel_order(order_id=tsla_stop_limit_order.id)  # it returns None
# await api.cancel_all_orders()  # it returns None
# aapl_market_order = await api.submit_order(
# my_positions = await api.list_positions()
# aapl_position = await api.get_position(symbol="AAPL")
# closed_aapl_order = await api.close_position(symbol="AAPL")
# closed_positions = await api.close_all_positions()
# trading_days = await api.get_trading_days(from_dt, to_dt)
