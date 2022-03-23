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


class CryptoStatus(str, Enum):
    """The status of if crypto is enabled."""

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class DomainAccount:
    """An account."""

    id: UUID
    account_number: str
    account_blocked: bool
    accrued_fees: float
    buying_power: float
    cash: float
    created_at: datetime
    currency: str
    daytrade_count: int
    daytrading_buying_power: float
    equity: float
    initial_margin: float
    last_equity: float
    last_maintenance_margin: float
    long_market_value: float
    maintenance_margin: float
    multiplier: float
    non_marginable_buying_power: float
    pattern_day_trader: bool
    pending_transfer_in: float
    portfolio_value: float
    regt_buying_power: float
    short_market_value: float
    shorting_enabled: bool
    sma: int
    status: Status
    crypto_status: CryptoStatus
    trade_suspended_by_user: bool
    trading_blocked: bool
    transfers_blocked: bool
