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
        self.api = AlpacaApi(self.api_settings)
        # self.api = Mock()

    async def test_get_clock_ok(self):
        """Test the return of clock api."""

        # Instantiate the wrapper api and patch a mock method for expected results
        alpaca_api = AlpacaApi(self.api_settings)
        alpaca_api.api.get_clock = Mock()

        # Import the fake api call that is going to be sent in to wrapper function
        alpaca_api.api.get_clock.return_value = dh.import_api_get_clock()

        # Run method tested
        clock = await alpaca_api.get_clock()

        # Import the expected results after wrapper function has been applied
        expected_clock = dh.import_expected_get_clock()

        #
        compare(clock, expected_clock, prefix="Expected clock object is different.")


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
#
