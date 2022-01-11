import asyncio
import sys
import os

sys.path.append("./src")
from tradingapi.alpaca.alpaca_api import AlpacaApi
from domainmodels.clock import DomainClock
from domainmodels.account import DomainAccount
from domainmodels.order import Type as OrderType
from domainmodels.order import DomainOrder
from domainmodels.order import OrderSide
from domainmodels.position import DomainPosition

print(os.getcwd())

async def main() -> None:

    api_settings = {
        "APCA_API_KEY_ID": "PK8HDG7R05LLSH8YM25W",
        "APCA_API_SECRET_KEY": "tthYbkvPYymnDuQJDYsdmfZ7v9lFmec2KRal0tYF",
        "APCA_API_BASE_URL": "https://paper-api.alpaca.markets",
        "APCA_RETRY_MAX": "3"
    }
    
    api = AlpacaApi(api_settings)

    # Check that get_clock works
    # account_alpaca = api.api.get_clock()
    clock = await api.get_clock()
    assert isinstance(clock, DomainClock)
    assert hasattr(clock, "is_open")

    # Check that get_account works
    # account_alpaca = api.api.get_account()
    account = await api.get_account()
    assert isinstance(account, DomainAccount)
    assert hasattr(account, "cash")

    # Check that cancel_all_orders works (it returns None)
    await api.cancel_all_orders()

    # Check that submit_order works
    # order_alpaca = api.api.submit_order(symbol="TSLA", qty=1, side="buy", 
    # type="stop_limit", stop_price=1400, limit_price=10000, time_in_force="day")
    tsla_stop_limit_order = await api.submit_order(
        symbol="TSLA",
        qty=1,
        side=OrderSide.BUY,
        type=OrderType.STOP_LIMIT,
        stop_price=1400,
        limit_price=10000 # set high limit s.t. the order does not get filled
    )
    assert isinstance(tsla_stop_limit_order, DomainOrder)
    assert hasattr(tsla_stop_limit_order, "limit_price")

    # Check that list_orders works
    # my_orders = api.api.list_orders()
    my_orders = await api.list_orders()
    assert len(my_orders) > 0
    assert all([isinstance(order, DomainOrder) for order in my_orders])

    # Check that get_order works
    # tsla_stop_limit_order_dupe = api.api.get_order(order_id=tsla_stop_limit_order.id)
    tsla_stop_limit_order_dupe = await api.get_order(order_id=tsla_stop_limit_order.id)
    assert isinstance(tsla_stop_limit_order_dupe, DomainOrder)

    # Check that cancel_order works
    await api.cancel_order(order_id=tsla_stop_limit_order.id) # it returns None

    # Check that cancel_all_orders works
    await api.cancel_all_orders() # it returns None

    # Add two other orders that go through.
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

    # Check that list_positions works
    my_positions = await api.list_positions()
    assert len(my_positions)>0
    assert all([isinstance(position, DomainPosition) for position in my_positions])
    assert all([hasattr(position, "side") for position in my_positions])

    # Check that get_position works
    aapl_position = await api.get_position(symbol="AAPL")
    assert isinstance(aapl_position, DomainPosition)
    assert hasattr(aapl_position, "side")

    # Check that close_position works
    closed_aapl_position = await api.close_position(symbol="AAPL")
    assert isinstance(closed_aapl_position, DomainPosition)
    assert hasattr(closed_aapl_position, "side")

    # Check that close_all_positions works
    closed_positions = await api.close_all_positions()
    assert len(closed_positions)>0
    assert all([isinstance(position, DomainPosition) for position in closed_positions])
    assert all([hasattr(position, "side") for position in closed_positions])

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())