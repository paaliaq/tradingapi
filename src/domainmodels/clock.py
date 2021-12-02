"""The clock."""
from datetime import datetime
from typing import Optional


class DomainClock:
    """A clock."""

    is_open: Optional[bool] = None
    next_close: Optional[datetime] = None
    next_open: Optional[datetime] = None
    timestamp: Optional[datetime] = None
