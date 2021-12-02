"""The account."""
from datetime import datetime
from uuid import UUID


class DomainAccount:
    """An account."""

    id: UUID
    account_number: str
    account_blocked: bool
    buying_power: str
    cash: str
    created_at: datetime
    currency: str
    daytrade_count: int
    daytrading_buying_power: str
    equity: str
    initial_margin: str
    last_equity: str
    last_maintenance_margin: str
    long_market_value: str
    maintenance_margin: str
    multiplier: int
    pattern_day_trader: bool
    portfolio_value: str
    regt_buying_power: str
    short_market_value: int
    shorting_enabled: bool
    sma: int
    status: str
    trade_suspended_by_user: bool
    trading_blocked: bool
    transfers_blocked: bool