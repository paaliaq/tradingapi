import json
import pickle

from alpaca_trade_api.entity import Account
from alpaca_trade_api.entity import Clock

from domainmodels.account import DomainAccount
from domainmodels.clock import DomainClock


# json.dumps(domain_account.__dict__, default=str)


def import_api_get_clock() -> Clock:
    """Import the simulated output from the alpaca api."""
    with open("data/api_get_clock.json", "r") as data:
        api_clock = Clock(None)
        api_clock.__dict__ = json.loads(data.read())
        return api_clock


def import_expected_get_clock() -> DomainClock:
    """Import the expected output from the alpaca api wrapper."""
    with open("data/expected_get_clock.json", "r") as data:
        domain_clock = DomainClock()
        domain_clock.__dict__ = json.loads(data.read())
        return domain_clock


def import_api_get_account() -> Account:
    """Import the simulated output from the alpaca api."""
    with open("data/api_get_account.json", "r") as data:
        api_account = Account(None)
        api_account.__dict__ = json.loads(data.read())
        return api_account


def import_expected_get_account() -> DomainAccount:
    """Import the simulated output from the alpaca api."""
    with open("data/get_account/expected_get_account.pkl", "r") as file:
        domain_account = pickle.load(file)
        return domain_account
