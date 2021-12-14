"""A trading day."""

from datetime import date, datetime
from typing import Optional


class TradingDay:
    """Represents a trading day with open and close date times."""

    close: Optional[datetime] = None
    open: Optional[datetime] = None

    @property
    def date(self) -> Optional[date]:
        """Get the date of the trading date.

        Returns:
            date: The date of the trading date
        """
        trading_day = self.open
        return trading_day.date() if trading_day is not None else None
