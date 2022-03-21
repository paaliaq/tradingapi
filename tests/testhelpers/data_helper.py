import json

from alpaca_trade_api.entity import Account, Clock, Order, Calendar, Position
from dateutil import parser
from datetime import datetime
from domainmodels.account import DomainAccount, Status
from domainmodels.clock import DomainClock
from domainmodels.order import DomainOrder, OrderSide, Type
from domainmodels.position import DomainPosition
from domainmodels.trading_day import TradingDay
from typing import List

# json.dumps(domain_account.__dict__, default=str)


def import_api_get_clock() -> Clock:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/get_clock/api_get_clock.json", "r") as d:
        api_clock = Clock(None)
        api_clock.__dict__ = json.loads(d.read())
        return api_clock


def import_expected_get_clock() -> DomainClock:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/get_clock/expected_get_clock.json", "r") as d:
        domain_clock = DomainClock()
        domain_clock.__dict__ = json.loads(d.read())
        return domain_clock


def import_api_get_account() -> Account:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/get_account/api_get_account.json", "r") as d:
        api_account = Account(None)
        api_account.__dict__ = json.loads(d.read())
        return api_account


def import_expected_get_account() -> DomainAccount:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/get_account/expected_get_account.json", "r") as d:
        domain_account = DomainAccount()
        domain_account.__dict__ = json.loads(d.read())

        domain_account.created_at = parser.parse(domain_account.created_at)
        domain_account.status = Status[domain_account.status]

        return domain_account


def import_api_submit_order() -> Order:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/submit_order/api_submit_order.json", "r") as d:
        api_order = Order(None)
        api_order.__dict__ = json.loads(d.read())
        return api_order


def import_expected_submit_order() -> DomainOrder:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/submit_order/expected_submit_order.json", "r") as d:
        domain_order = DomainOrder(None)
        domain_order.__dict__ = json.loads(d.read())

        domain_order.side = OrderSide[domain_order.side.upper()]
        domain_order.type = Type[domain_order.type.upper()]
        return domain_order


def import_api_get_order() -> Order:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/get_order/api_get_order.json", "r") as d:
        api_order = Order(None)
        api_order.__dict__ = json.loads(d.read())
        return api_order


def import_expected_get_order() -> DomainOrder:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/get_order/expected_get_order.json", "r") as d:
        domain_order = DomainOrder(None)
        domain_order.__dict__ = json.loads(d.read())
        return domain_order


def import_api_list_orders() -> List[Order]:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/list_orders/api_list_orders.json", "r") as d:

        order_list = json.loads(d.read())
        api_order_list = []
        for order in order_list:
            api_order = Order(None)
            api_order.__dict__ = order
            api_order_list.append(api_order)

        return api_order_list


def import_expected_list_orders() -> List[DomainOrder]:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/list_orders/expected_list_orders.json", "r") as d:

        order_list = json.loads(d.read())
        domain_order_list = []
        for order in order_list:
            domain_order = DomainOrder(None)
            domain_order.__dict__ = order
            domain_order.side = OrderSide[domain_order.side.upper()]
            domain_order.type = Type[domain_order.type.upper()]
            domain_order_list.append(domain_order)

        return domain_order_list


def import_api_get_trading_days() -> List[Calendar]:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/get_trading_days/api_get_trading_days.json", "r") as d:

        trading_days = json.loads(d.read())
        api_trading_day_list = []
        for day in trading_days:
            api_trading_day = Calendar(None)
            api_trading_day.__dict__ = day
            api_trading_day_list.append(api_trading_day)

        return api_trading_day_list


def import_expected_get_trading_days() -> List[TradingDay]:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/get_trading_days/expected_get_trading_days.json", "r") as d:

        format = '%Y-%m-%d %H:%M:%S'
        trading_days = json.loads(d.read())
        domain_trading_day_list = []
        for day in trading_days:
            domain_trading_day = TradingDay()
            day["open"] = datetime.strptime(day["open"], format)
            day["close"] = datetime.strptime(day["close"], format)
            domain_trading_day.__dict__ = day
            domain_trading_day_list.append(domain_trading_day)

        return domain_trading_day_list


def import_api_get_position() -> Position:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/get_position/api_get_position.json", "r") as d:
        api_position = Position(None)
        api_position.__dict__ = json.loads(d.read())
        return api_position


def import_expected_get_position() -> DomainPosition:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/get_position/expected_get_position.json", "r") as d:
        domain_position = DomainPosition()
        domain_position.__dict__ = json.loads(d.read())
        return domain_position


def import_api_list_positions() -> List[Position]:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/list_positions/api_list_positions.json", "r") as d:

        position_list = json.loads(d.read())
        api_position_list = []
        for position in position_list:
            api_position = Position(None)
            api_position.__dict__ = position
            api_position_list.append(api_position)

        return api_position_list


def import_expected_list_positions() -> List[DomainPosition]:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/list_positions/expected_list_positions.json", "r") as d:

        position_list = json.loads(d.read())
        domain_position_list = []
        for position in position_list:
            domain_position = DomainPosition()
            domain_position.__dict__ = position
            domain_position_list.append(domain_position)

        return domain_position_list
