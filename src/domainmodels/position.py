"""A position."""
from enum import Enum


class Exchange(str, Enum):
    """The identifier of the exchange."""

    NYSE = "NYSE"
    NASDAQ = "NASDAQ"


class Side(str, Enum):
    """The side of the position."""

    LONG = "long"
    SHORT = "short"


class AssetClass(str, Enum):
    """The identifier of the asset class."""

    US_EQUITY = "us_equity"


class DomainPosition:
    """The domain order."""

    asset_id: str
    symbol: str
    qty: int
    side: Side = Side.LONG
    exchange: Exchange = Exchange.NASDAQ
    asset_class: AssetClass = AssetClass.US_EQUITY
    asset_marginable: bool
    avg_entry_price: float
    market_value: float
    cost_basis: float
    unrealized_pl: float
    unrealized_plpc: float
    unrealized_intraday_pl: float
    unrealized_intraday_plpc: float
    current_price: float
    lastday_price: float
    change_today: float
