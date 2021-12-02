from alpaca_trade_api.entity import Clock
from domainmodels.clock import DomainClock

from mappers.mapper import Mapper


class ClockMapper(Mapper[Clock, DomainClock]):
    def map(self, clock: Clock) -> DomainClock:

        # Clock
        domain_clock = DomainClock()

        domain_clock.is_open = clock.is_open
        domain_clock.next_close = clock.next_close
        domain_clock.next_open = clock.next_open
        domain_clock.timestamp = clock.timestamp

        return domain_clock
