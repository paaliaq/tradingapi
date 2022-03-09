"""The account."""
from datetime import datetime
from enum import Enum
from uuid import UUID


class Status(str, Enum):
    """The type of the order."""

    ONBOARDING = "ONBOARDING"
    SUBMISSION_FAILED = "SUBMISSION_FAILED"
    SUBMITTED = "SUBMITTED"
    ACCOUNT_UPDATED = "ACCOUNT_UPDATED"
    APPROVAL_PENDING = "APPROVAL_PENDING"
    ACTIVE = "ACTIVE"
    REJECTED = "REJECTED"


class DomainAccount:
    """An account."""

    id: UUID
    account_number: str
    account_blocked: bool
    accrued_fees: float
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
    non_marginable_buying_power: float
    pattern_day_trader: bool
    pending_transfer_in: float
    portfolio_value: str
    regt_buying_power: str
    short_market_value: int
    shorting_enabled: bool
    sma: int
    status: Status
    trade_suspended_by_user: bool
    trading_blocked: bool
    transfers_blocked: bool
