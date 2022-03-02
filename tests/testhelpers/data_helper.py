import json

from alpaca_trade_api.entity import Account, Clock, Order
from dateutil import parser

from domainmodels.account import DomainAccount, Status
from domainmodels.clock import DomainClock
from domainmodels.order import DomainOrder, OrderSide, Type
from typing import List

# json.dumps(domain_account.__dict__, default=str)


def import_api_get_clock() -> Clock:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/get_clock/api_get_clock.json", "r") as data:
        api_clock = Clock(None)
        api_clock.__dict__ = json.loads(data.read())
        return api_clock


def import_expected_get_clock() -> DomainClock:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/get_clock/expected_get_clock.json", "r") as data:
        domain_clock = DomainClock()
        domain_clock.__dict__ = json.loads(data.read())
        return domain_clock


def import_api_get_account() -> Account:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/get_account/api_get_account.json", "r") as data:
        api_account = Account(None)
        api_account.__dict__ = json.loads(data.read())
        return api_account


def import_expected_get_account() -> DomainAccount:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/get_account/expected_get_account.json", "r") as data:
        domain_account = DomainAccount()
        domain_account.__dict__ = json.loads(data.read())

        domain_account.created_at = parser.parse(domain_account.created_at)
        domain_account.status = Status[domain_account.status]

        return domain_account


def import_api_submit_order() -> Order:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/submit_order/api_submit_order.json", "r") as data:
        api_order = Order(None)
        api_order.__dict__ = json.loads(data.read())
        return api_order


def import_expected_submit_order() -> DomainOrder:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/submit_order/expected_submit_order.json", "r") as data:
        domain_order = DomainOrder(None)
        domain_order.__dict__ = json.loads(data.read())

        domain_order.side = OrderSide[domain_order.side.upper()]
        domain_order.type = Type[domain_order.type.upper()]
        return domain_order


def import_api_get_order() -> Order:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/get_order/api_get_order.json", "r") as data:
        api_order = Order(None)
        api_order.__dict__ = json.loads(data.read())
        return api_order


def import_expected_get_order() -> DomainOrder:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/get_order/expected_get_order.json", "r") as data:
        domain_order = DomainOrder(None)
        domain_order.__dict__ = json.loads(data.read())
        return domain_order


def import_api_list_orders() -> Order:
    """Import the simulated output from the alpaca api."""
    with open("tests/data/list_orders/api_list_orders.json", "r") as data:
        api_order = Order(None)
        api_order.__dict__ = json.loads(data.read())
        return api_order


def import_expected_list_orders() -> DomainOrder:
    """Import the expected output from the alpaca api wrapper."""
    with open("tests/data/list_orders/expected_list_orders.json", "r") as data:
        domain_order = DomainOrder(None)
        domain_order.__dict__ = json.loads(data.read())
        return domain_order
