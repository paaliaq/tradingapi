import datetime

from alpaca_trade_api.entity import Calendar
from domainmodels.trading_day import TradingDay

from mappers.mapper import Mapper


class TradingDayMapper(Mapper[Calendar, TradingDay]):
    def map(self, calendar: Calendar) -> TradingDay:

        # Calendar
        trading_day = TradingDay()
        trading_day.open = datetime.combine(
            calendar.date.to_pydatetime(), calendar.open
        )
        trading_day.close = datetime.combine(
            calendar.date.to_pydatetime(), calendar.close
        )

        return trading_day
