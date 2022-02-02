import json

from types import SimpleNamespace

from domainmodels.clock import DomainClock


def import_api_get_clock():
    """Import the simulated output from the alpaca api."""
    with open("data/api_get_clock.json", "r") as data:
        data_json = data.read()
        return json.loads(data_json, object_hook=lambda d: SimpleNamespace(**d))


def import_expected_get_clock() -> DomainClock:
    """Import the expected output from the alpaca api wrapper."""
    with open("data/expected_get_clock.json", "r") as data:
        domain_clock = DomainClock()
        domain_clock.__dict__ = json.loads(data.read())
        return domain_clock
