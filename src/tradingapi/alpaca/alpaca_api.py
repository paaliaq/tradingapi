"""Base class for trading APIs."""
from datetime import datetime
from typing import Any, Dict, List

import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import Orders
from domainmodels.account import DomainAccount
from domainmodels.clock import DomainClock
from domainmodels.order import DomainOrder
from domainmodels.trading_day import TradingDay
from helpers.async_wrapper import async_wrap
from mappers.account_mapper import AccountMapper
from mappers.clock_mapper import ClockMapper
from mappers.order_mapper import OrderMapper
from mappers.tradingday_mapper import TradingDayMapper
from tradingapi.base.base_api import BaseApi


class AlpacaApi(BaseApi):
    """Class for Alpaca API.

    This class is based on alpaca-trade-api-python.
    For reference, please see: https://github.com/alpacahq/alpaca-trade-api-python
    """

    def __init__(self, env_dict: Dict) -> None:
        """Class initialization function."""
        super().__init__(env_dict)  # type: ignore
        self.api = tradeapi.REST()

    async def get_account(self) -> DomainAccount:
        """Get the account."""
        # Get Account
        get_account_async = async_wrap(self.api.get_account)
        account = await get_account_async()

        # Mapping
        account_mapper = AccountMapper()
        domain_account = account_mapper.map(account)

        return domain_account

    def _handle_kwargs_submit_order(self, **kwargs: Any) -> Dict:
        """Function to initialize missing kwargs for submit_order function."""
        # Initialize default kwargs if necessary
        if "time_in_force" not in kwargs:
            kwargs["time_in_force"] = "day"
        if "extended_hours" not in kwargs:
            kwargs["extended_hours"] = None
        if "take_profit" not in kwargs:
            kwargs["take_profit"] = None
        if "stop_loss" not in kwargs:
            kwargs["stop_loss"] = None
        if "trail_price" not in kwargs:
            kwargs["trail_price"] = None
        if "trail_percent" not in kwargs:
            kwargs["trail_percent"] = None
        return kwargs

    async def get_clock(self) -> DomainClock:
        """Returns the clock."""
        # Get clock
        get_clock_async = async_wrap(self.api.get_clock)
        clock = await get_clock_async()

        # Mapping
        clock_mapper = ClockMapper()
        domain_clock = clock_mapper.map(clock)

        return domain_clock

    async def get_trading_days(
        self, start: datetime, end: datetime
    ) -> List[TradingDay]:
        """Function to get calendars."""
        get_calendar_async = async_wrap(self.api.get_calendar)

        calendars = await get_calendar_async(start.isoformat(), end.isoformat())

        # Mapping
        trading_day_mapper = TradingDayMapper()
        domains_trading_days = [trading_day_mapper(c) for c in calendars]

        return domains_trading_days

    async def submit_order(
        self,
        order: Orders,
    ) -> DomainOrder:
        """Submit an order.

        Args:
            order: The order to submit

        Returns:
            DomainOrder: The places order
        """
        # We do no mapping here, as the sdk directly takes all of the values

        # Get Account
        submit_order_async = async_wrap(self.api.submit_order)

        # Submit order
        order = await submit_order_async(
            symbol=order.symbol,
            qty=order.qty,
            side=order.side.value,
            type=order.type.value,
            limit_price=order.limit_price,
            stop_price=order.stop_price,
            time_in_force=order.time_in_force.value,
            extended_hours=order.extended_hours,
            take_profit=order.take_profit,
            stop_loss=order.stop_loss,
            trail_price=order.trail_price,
            trail_percent=order.trail_percent,
            order_class=order.order_class.value,
            instructions=None,  # not documented in alpaca?
        )

        # Mapping
        order_mapper = OrderMapper()
        domain_order = order_mapper.map(order)

        return domain_order

    def list_orders(self, **kwargs: Any) -> List[Dict]:
        """List orders.

        Args:
            **kwargs: Arbitrary keyword arguments, among them the following:
                status (str = "open"): open, closed or all. Defaults to open.
                limit (int = 50): Defaults to 50 and max is 500
                after: timestamp
                until: timestamp
                direction: asc or desc

        Returns:
            List[Dict]: a list of dictionaries containing order information
        """
        # Initialize default kwargs if necessary
        if "status" not in kwargs:
            status = "open"
        else:
            status = kwargs["status"]
        if "limit" not in kwargs:
            limit = 50
        else:
            limit = kwargs["limit"]
        if "after" not in kwargs:
            after = None
        else:
            after = kwargs["after"]
        if "until" not in kwargs:
            until = None
        else:
            until = kwargs["until"]
        if "direction" not in kwargs:
            direction = None
        else:
            direction = kwargs["direction"]

        order_list = self.api.list_orders(
            status=status, limit=limit, after=after, until=until, direction=direction
        )
        order_list = [order.__dict__["_raw"] for order in order_list]

        return order_list

    def get_order(self, order_id: str, **kwargs: Any) -> Dict:
        """Get an order with specific order_id."""
        order = self.api.get_order(order_id=order_id)
        order_dict = order.__dict__["_raw"]
        return order_dict

    def cancel_order(self, order_id: str, **kwargs: Any) -> Dict:
        """Cancel an order with specific order_id."""
        self.api.cancel_order(order_id=order_id)
        return {}  # Dummy return statement since alpaca does not return anything

    def cancel_all_orders(self, **kwargs: Any) -> List[Dict]:
        """Cancel all orders."""
        self.api.cancel_all_orders()
        return [{}]  # Dummy return statement since alpaca does not return anything

    def list_positions(self, **kwargs: Any) -> List[Dict]:
        """Get a list of open positions."""
        position_list = self.api.list_positions()
        position_list = [position.__dict__["_raw"] for position in position_list]
        return position_list

    def get_position(self, symbol: str, **kwargs: Any) -> Dict:
        """Get an open position for a symbol."""
        position = self.api.get_position(symbol=symbol)
        position_dict = position.__dict__["_raw"]
        return position_dict

    def close_position(self, symbol: str, **kwargs: Any) -> Dict:
        """Liquidates the position for the given symbol at market price."""
        position = self.api.close_position(symbol=symbol)
        position_dict = position.__dict__["_raw"]
        return position_dict

    def close_all_positions(self, **kwargs: Any) -> List[Dict]:
        """Liquidates all open positions at market price."""
        position_list = self.api.close_all_positions()
        position_list = [position.__dict__["_raw"] for position in position_list]
        return position_list
