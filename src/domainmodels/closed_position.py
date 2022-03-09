"""The closed position response."""

from typing import Optional
from domainmodels.order import DomainOrder


class ClosedPositionError:
    """ClosedPositionError."""

    available: int
    code: int
    existing_qty: int
    held_for_orders: int
    message: str
    symbol: str


class ClosedPosition:
    """ClosedPosition."""

    symbol: str
    http_status_code: int
    order: Optional[DomainOrder]
    error: Optional[ClosedPositionError]
