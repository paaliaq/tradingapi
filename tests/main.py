import asyncio
from datetime import datetime
import json
import pickle
import sys

sys.path.insert(0, '../src')

print(sys.path)

from domainmodels.account import DomainAccount
from domainmodels.clock import DomainClock
from domainmodels.closed_position import ClosedPosition
from domainmodels.order import DomainOrder, OrderSide
from domainmodels.order import Type as OrderType
from domainmodels.position import DomainPosition
from domainmodels.trading_day import TradingDay
from tradingapi.alpaca.alpaca_api import AlpacaApi


async def main() -> None:
    # api_settings = {
    #     "APCA_API_KEY_ID": "PK8HDG7R05LLSH8YM25W",
    #     "APCA_API_SECRET_KEY": "tthYbkvPYymnDuQJDYsdmfZ7v9lFmec2KRal0tYF",
    #     "APCA_API_BASE_URL": "https://paper-api.alpaca.markets",
    #     "APCA_RETRY_MAX": "3"
    # }

    api_settings = {
        "APCA_API_KEY_ID": "PKMLR3Z5916GTNCP10JI",
        "APCA_API_SECRET_KEY": "hNJj2I3YoUGRLefjumNRvNSzMjCIjzygqT3r1rni",
        "APCA_API_BASE_URL": "https://paper-api.alpaca.markets",
        "APCA_RETRY_MAX": "3"
    }

    api = AlpacaApi(api_settings)

    # # Check that get_clock works
    # # account_alpaca = api.api.get_clock()
    # clock = await api.get_clock()
    # assert isinstance(clock, DomainClock)
    # assert hasattr(clock, "is_open")

    # # Check that get_account works
    # account = await api.get_account()

    # assert isinstance(account, DomainAccount)
    # assert hasattr(account, "cash")

    # # Check that cancel_all_orders works (it returns None)
    # await api.cancel_all_orders()

    # TODO: Dumps conducted until here.

    # Check that submit_order works
    # order_alpaca = api.api.submit_order(symbol="TSLA", qty=1, side="buy", 
    # type="stop_limit", stop_price=1400, limit_price=10000, time_in_force="day")
    # tsla_stop_limit_order = await api.submit_order(
    #     symbol="TSLA",
    #     qty=1,
    #     side=OrderSide.BUY,
    #     type=OrderType.STOP_LIMIT,
    #     stop_price=1400,
    #     limit_price=10000  # set high limit s.t. the order does not get filled
    # )

    # with open("tests/data/submit_order/expected_submit_order.json", 'w') as f:
    #     json.dump(tsla_stop_limit_order.__dict__, f)

    #################################################################################
    # Check that list_orders works
    #################################################################################

    # # First cancel all orders to start with a clean sheet
    # await api.cancel_all_orders()

    # # Place 2 orders so we have >1 order in our list of orders
    # tsla_stop_limit_order = await api.submit_order(
    #     symbol="TSLA",
    #     qty=1,
    #     side=OrderSide.BUY,
    #     type=OrderType.STOP_LIMIT,
    #     stop_price=1400,
    #     limit_price=1  # set small limit s.t. the order does not get filled
    # )

    # msft_stop_limit_order = await api.submit_order(
    #     symbol="MSFT",
    #     qty=1,
    #     side=OrderSide.BUY,
    #     type=OrderType.STOP_LIMIT,
    #     stop_price=1400,
    #     limit_price=1  # set small limit s.t. the order does not get filled
    # )


    # # Write out expected list order
    # order_list = await api.list_orders()
    # #print([order.__dict__ for order in order_list])

    # with open("tests/data/list_orders/expected_list_orders.json", 'w') as f:
    #     json.dump([order.__dict__ for order in order_list], f)

    # # Write out api list order
    # order_list_api = api.api.list_orders()
    # #print([order.__dict__ for order in order_list_api])

    # with open("tests/data/list_orders/api_list_orders.json", 'w') as f:
    #     json.dump([order.__dict__ for order in order_list_api], f)

    #################################################################################
    # Check that list_orders works
    #################################################################################

    # # Check trading days
    # from_dt = datetime(2022, 3, 1)
    # to_dt = datetime(2022, 3, 15)
    # format = '%Y-%m-%d %H:%M:%S'
    
    # # Write out expected trading days
    # trading_days = await api.get_trading_days(from_dt, to_dt)
    # trading_days_converted = []
    # for day in trading_days:
    #     day.__dict__["open"] = datetime.strftime(day.__dict__["open"], format)
    #     day.__dict__["close"] = datetime.strftime(day.__dict__["close"], format)
    #     trading_days_converted.append(day)
    # # print([day.__dict__ for day in trading_days_converted])

    # with open("tests/data/get_trading_days/expected_get_trading_days.json", "w") as f:
    #     json.dump([day.__dict__ for day in trading_days_converted], f)

    # # Write out api trading days
    # trading_days_api = api.api.get_calendar(from_dt, to_dt)
    # # print([day.__dict__ for day in trading_days_api])
    # with open("tests/data/get_trading_days/api_get_trading_days.json", "w") as f:
    #     json.dump([day.__dict__ for day in trading_days_api], f)


    #################################################################################
    # Check that test_get_position_ok works
    #################################################################################

    # # Close all positions
    # closed_positions = await api.close_all_positions()

    # # Close all orders
    # await api.cancel_all_orders()  # it returns None

    # # Place an order that goes through
    # aapl_market_order = await api.submit_order(
    #     symbol="AAPL",
    #     qty=1,
    #     side=OrderSide.BUY,
    #     type=OrderType.MARKET
    # )
    # await asyncio.sleep(5) # wait 5 seconds to be sure the order went through

    # # Write expected position
    # position = await api.get_position(symbol="AAPL")
    # # print(position.__dict__)
    # with open("tests/data/get_position/expected_get_position.json", "w") as f:
    #     json.dump(position.__dict__, f)

    # # Write out api position
    # position_api = api.api.get_position(symbol="AAPL")
    # # print(position_api.__dict__)
    # with open("tests/data/get_position/api_get_position.json", "w") as f:
    #     json.dump(position_api.__dict__, f)

    # sys.exit()


    #################################################################################
    # Check that test_list_positions_ok works
    #################################################################################

    # Close all positions
    closed_positions = await api.close_all_positions()

    # Close all orders
    await api.cancel_all_orders()  # it returns None

    # Place two orders that go through
    aapl_market_order = await api.submit_order(
        symbol="AAPL",
        qty=1,
        side=OrderSide.BUY,
        type=OrderType.MARKET
    )
    msft_market_order = await api.submit_order(
        symbol="MSFT",
        qty=1,
        side=OrderSide.BUY,
        type=OrderType.MARKET
    )
    await asyncio.sleep(5) # wait 5 seconds to be sure the order went through

    # Write expected position list
    position_list = await api.list_positions()
    #print([position.__dict__ for position in position_list])
    with open("tests/data/list_positions/expected_list_positions.json", "w") as f:
        json.dump([position.__dict__ for position in position_list], f)

    # Write out api position list
    position_list_api = api.api.list_positions()
    #print([position.__dict__ for position in position_list_api])
    with open("tests/data/list_positions/api_list_positions.json", "w") as f:
        json.dump([position.__dict__ for position in position_list_api], f)

    sys.exit()


    # #################################################################################
    # # Other
    # #################################################################################

    # # assert isinstance(tsla_stop_limit_order, DomainOrder)
    # # assert hasattr(tsla_stop_limit_order, "limit_price")

    # # Check that list_orders works
    # # my_orders = api.api.list_orders()
    # # my_orders = await api.list_orders()

    # #with open("data/get_account/expected_list_orders.pkl") as f:
    # #    pickle.dump(my_orders, f)

    # # assert len(my_orders) > 0
    # # assert all([isinstance(order, DomainOrder) for order in my_orders])

    # # Check that get_order works
    # # print(tsla_stop_limit_order.id)
    # # tsla_stop_limit_order_dupe = await api.get_order(order_id=tsla_stop_limit_order.id)
    # # with open("tests/data/get_order/expected_get_order.json", "w") as f:
    # #     json.dump(tsla_stop_limit_order_dupe.__dict__, f)
    # # assert isinstance(tsla_stop_limit_order_dupe, DomainOrder)

    # # tsla_stop_limit_order = api.api.get_order(order_id=tsla_stop_limit_order.id)
    # # with open("tests/data/get_order/api_get_order.json", "w") as f:
    # #     json.dump(tsla_stop_limit_order.__dict__, f)


    # # Check that cancel_order works
    # await api.cancel_order(order_id=tsla_stop_limit_order.id)  # it returns None

    # # Check that cancel_all_orders works
    # await api.cancel_all_orders()  # it returns None

    # # Add two other orders that go through.
    # aapl_market_order = await api.submit_order(
    #     symbol="AAPL",
    #     qty=1,
    #     side=OrderSide.BUY,
    #     type=OrderType.MARKET
    # )
    # msft_market_order = await api.submit_order(
    #     symbol="MSFT",
    #     qty=2,
    #     side=OrderSide.BUY,
    #     type=OrderType.MARKET
    # )

    # # TODO: Do we need to look ath the results here as well? Why are we not doing any test check here?
    # # with open("data/get_account/expected_get_order.pkl") as file:
    # #    pickle.dump(tsla_stop_limit_order_dupe, file)

    # # Check that list_positions works
    # my_positions = await api.list_positions()

    # #with open("data/get_account/expected_list_positions.pkl") as file:
    # #    pickle.dump(my_positions, file)

    # assert len(my_positions) > 0
    # assert all([isinstance(position, DomainPosition) for position in my_positions])
    # assert all([hasattr(position, "side") for position in my_positions])

    # # Check that get_position works
    # aapl_position = await api.get_position(symbol="AAPL")

    # #with open("data/get_account/expected_get_position.pkl") as file:
    # #    pickle.dump(aapl_position, file)

    # assert isinstance(aapl_position, DomainPosition)
    # assert hasattr(aapl_position, "side")

    # # Check that close_position works
    # closed_aapl_order = await api.close_position(symbol="AAPL")

    # with open("data/get_account/expected_close_position.pkl") as file:
    #     pickle.dump(closed_aapl_order, file)

    # assert isinstance(closed_aapl_order, DomainOrder)
    # assert hasattr(closed_aapl_order, "side")

    # # Check that close_all_positions works
    # closed_positions = await api.close_all_positions()

    # with open("data/get_account/expected_close_all_positions.pkl") as file:
    #     pickle.dump(closed_positions, file)

    # assert len(closed_positions) > 0
    # assert all([isinstance(position, ClosedPosition) for position in closed_positions])




if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
