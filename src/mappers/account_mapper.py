"""Account mapper."""

from alpaca_trade_api.entity import Account
from dateutil import parser

from domainmodels.account import DomainAccount, Status
from mappers.mapper import Mapper


class AccountMapper(Mapper[Account, DomainAccount]):
    """Mapper to map from Account to DomainAccount."""

    def map(self, account: Account) -> DomainAccount:
        """Function to map from Account to DomainAccount."""
        # Account
        domain_account = DomainAccount()

        domain_account.id = account.id
        domain_account.account_number = account.account_number
        domain_account.account_blocked = account.account_blocked
        domain_account.accrued_fees = float(account.accrued_fees)
        domain_account.buying_power = float(account.buying_power)
        domain_account.cash = float(account.cash)

        try:
            domain_account.created_at = parser.parse(account.created_at)
        except TypeError:
            domain_account.created_at = account.created_at.to_pydatetime()

        domain_account.crypto_status = account.crypto_status
        domain_account.currency = account.currency
        domain_account.daytrade_count = int(account.daytrade_count)
        # noinspection DuplicatedCode
        domain_account.daytrading_buying_power = float(account.daytrading_buying_power)
        domain_account.equity = float(account.equity)
        domain_account.initial_margin = float(account.initial_margin)
        domain_account.last_equity = float(account.last_equity)
        domain_account.last_maintenance_margin = float(account.last_maintenance_margin)
        domain_account.long_market_value = float(account.long_market_value)
        domain_account.maintenance_margin = float(account.maintenance_margin)
        domain_account.multiplier = float(account.multiplier)
        domain_account.non_marginable_buying_power = float(
            account.non_marginable_buying_power
        )
        domain_account.pattern_day_trader = account.pattern_day_trader
        domain_account.pending_transfer_in = float(account.pending_transfer_in)
        domain_account.portfolio_value = float(account.portfolio_value)
        domain_account.regt_buying_power = float(account.regt_buying_power)
        domain_account.short_market_value = float(account.short_market_value)
        domain_account.shorting_enabled = float(account.shorting_enabled)
        domain_account.sma = float(account.sma)
        domain_account.status = Status[account.status]
        domain_account.trade_suspended_by_user = account.trade_suspended_by_user
        domain_account.trading_blocked = account.trading_blocked
        domain_account.transfers_blocked = account.transfers_blocked

        return domain_account
