from alpaca_trade_api.entity import Account
from domainmodels.account import DomainAccount

from mappers.mapper import Mapper


class AccountMapper(Mapper[Account, DomainAccount]):
    def map(self, account: Account) -> DomainAccount:

        # Account
        domain_account = DomainAccount()

        domain_account.id = account.id
        domain_account.account_number = account.account_number
        domain_account.account_blocked = account.account_blocked
        domain_account.buying_power = account.buying_power
        domain_account.cash = account.cash
        domain_account.created_at = account.created_at
        domain_account.currency = account.currency
        domain_account.daytrade_count = account.daytrade_count
        domain_account.daytrading_buying_power = account.daytrading_buying_power
        domain_account.equity = account.equity
        domain_account.initial_margin = account.initial_margin
        domain_account.last_equity = account.last_equity
        domain_account.last_maintenance_margin = account.last_maintenance_margin
        domain_account.long_market_value = account.long_market_value
        domain_account.maintenance_margin = account.maintenance_margin
        domain_account.multiplier = account.multiplier
        domain_account.pattern_day_trader = account.pattern_day_trader
        domain_account.portfolio_value = account.__delattr__portfolio_value
        domain_account.regt_buying_power = account.regt_buying_power
        domain_account.short_market_value = account.short_market_value
        domain_account.shorting_enabled = account.shorting_enabled
        domain_account.sma = account.sma
        domain_account.status = account.status
        domain_account.trade_suspended_by_user = account.trade_suspended_by_user
        domain_account.trading_blocked = account.trading_blocked
        domain_account.transfers_blocked = account.transfers_blocked

        return domain_account
