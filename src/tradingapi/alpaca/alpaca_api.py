"""Base class for trading APIs."""
from datetime import datetime
from typing import Any, Dict, List, Optional

import alpaca_trade_api as tradeapi
from domainmodels.account import DomainAccount
from domainmodels.clock import DomainClock
from domainmodels.closed_position import ClosedPosition
from domainmodels.order import (
    DomainOrder,
    OrderClass,
    OrderSide,
    StopLoss,
    TakeProfit,
    TimeInForce,
    Type,
)
from domainmodels.position import DomainPosition
from domainmodels.trading_day import TradingDay
from helpers.async_wrapper import async_wrap
from mappers.account_mapper import AccountMapper
from mappers.clock_mapper import ClockMapper
from mappers.closed_positions_mapper import ClosedPositionMapper
from mappers.order_mapper import OrderMapper
from mappers.position_mapper import PositionMapper
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

    # def _handle_kwargs_submit_order(self, **kwargs: Any) -> Dict:
    #     """Function to initialize missing kwargs for submit_order function."""
    #     # Initialize default kwargs if necessary
    #     if "time_in_force" not in kwargs:
    #         kwargs["time_in_force"] = "day"
    #     if "extended_hours" not in kwargs:
    #         kwargs["extended_hours"] = None
    #     if "take_profit" not in kwargs:
    #         kwargs["take_profit"] = None
    #     if "stop_loss" not in kwargs:
    #         kwargs["stop_loss"] = None
    #     if "trail_price" not in kwargs:
    #         kwargs["trail_price"] = None
    #     if "trail_percent" not in kwargs:
    #         kwargs["trail_percent"] = None
    #    return kwargs

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

        calendars = await get_calendar_async(
            start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d")
        )

        # Mapping
        trading_day_mapper = TradingDayMapper()
        domains_trading_days = [trading_day_mapper.map(c) for c in calendars]

        return domains_trading_days

    async def submit_order(
        self,
        symbol: str,
        qty: int,
        side: OrderSide,
        type: Type = Type.MARKET,
        time_in_force: TimeInForce = TimeInForce.DAY,
        extended_hours: bool = False,
        order_class: OrderClass = OrderClass.SIMPLE,
        stop_price: Optional[float] = None,
        limit_price: Optional[float] = None,
        take_profit: Optional[TakeProfit] = None,
        stop_loss: Optional[StopLoss] = None,
        trail_price: Optional[float] = None,
        trail_percent: Optional[float] = None,
        notional: Optional[float] = None,
    ) -> DomainOrder:
        """Submit an order.

        Args:
            symbol: str,
            qty: int,
            side: OrderSide,
            type: Type = Type.MARKET,
            time_in_force: TimeInForce = TimeInForce.DAY,
            extended_hours: bool = False,
            order_class: OrderClass = OrderClass.SIMPLE,
            stop_price: Optional[float] = None,
            limit_price: Optional[float] = None,
            take_profit: Optional[TakeProfit] = None,
            stop_loss: Optional[StopLoss] = None,
            trail_price: Optional[float] = None,
            trail_percent: Optional[float] = None,
            notional: Optional[float] = None,

        Returns:
            DomainOrder: The places order
        """
        # We do no mapping here, as the sdk directly takes all of the values

        # Get Account
        submit_order_async = async_wrap(self.api.submit_order)

        # Submit order
        order = await submit_order_async(
            symbol=symbol,
            qty=qty,
            side=side.value,
            type=type.value,
            limit_price=limit_price,
            stop_price=stop_price,
            time_in_force=time_in_force.value,
            extended_hours=extended_hours,
            order_class=order_class.value,
            take_profit=None if take_profit is None else take_profit,
            stop_loss=None if stop_loss is None else stop_loss,
            trail_price=trail_price,
            trail_percent=trail_percent,
            instructions=None,  # not documented in alpaca?
        )

        # Mapping
        order_mapper = OrderMapper()
        domain_order = order_mapper.map(order)

        return domain_order

    async def list_orders(self, **kwargs: Any) -> List[DomainOrder]:
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

        # Retrieve order list
        list_orders_async = async_wrap(self.api.list_orders)
        order_list = await list_orders_async(
            status=status, limit=limit, after=after, until=until, direction=direction
        )

        # Map order list to domain order list
        order_mapper = OrderMapper()
        domain_order_list = [order_mapper.map(order) for order in order_list]

        return domain_order_list

    async def get_order(self, order_id: str, **kwargs: Any) -> DomainOrder:
        """Get an order with specific order_id."""
        # Retrieve order
        get_order_async = async_wrap(self.api.get_order)
        order = await get_order_async(order_id=order_id)

        # Map order to domain order
        order_mapper = OrderMapper()
        domain_order = order_mapper.map(order)

        return domain_order

    async def cancel_order(self, order_id: str, **kwargs: Any) -> None:
        """Cancel an order with specific order_id."""
        cancel_order_async = async_wrap(self.api.cancel_order)
        await cancel_order_async(order_id=order_id)

        return None

    async def cancel_all_orders(self, **kwargs: Any) -> None:
        """Cancel all orders."""
        cancel_all_orders_async = async_wrap(self.api.cancel_all_orders)
        await cancel_all_orders_async()

        return None

    async def list_positions(self, **kwargs: Any) -> List[DomainPosition]:
        """Get a list of open positions."""
        # Retrieve positions
        list_positions_async = async_wrap(self.api.list_positions)
        position_list = await list_positions_async()

        # Map position list to domain position list
        position_mapper = PositionMapper()
        domain_position_list = [position_mapper.map(position) for position in position_list]

        return domain_position_list

    async def get_position(self, symbol: str, **kwargs: Any) -> DomainPosition:
        """Get an open position for a symbol."""
        # Retrieve position
        get_position_async = async_wrap(self.api.get_position)
        position = await get_position_async(symbol=symbol)

        # Map positions to domain positions
        position_mapper = PositionMapper()
        domain_position = position_mapper.map(position)

        return domain_position

    async def close_position(self, symbol: str, **kwargs: Any) -> DomainOrder:
        """Liquidates the position for the given symbol at market price."""
        # Get closed position
        close_position_async = async_wrap(self.api.close_position)
        order = await close_position_async(symbol=symbol)

        # Map positions to domain positions
        order_mapper = OrderMapper()
        domain_order = order_mapper.map(order)

        return domain_order

    async def close_all_positions(self, **kwargs: Any) -> List[ClosedPosition]:
        """Liquidates all open positions at market price."""
        # Get list of closed positions
        close_all_positions_async = async_wrap(self.api.close_all_positions)
        closed_positions = await close_all_positions_async()

        # Map position list to domain position list
        closed_position_mapper = ClosedPositionMapper()
        domain_closed_positions_list = [closed_position_mapper.map(closed_position) for closed_position in closed_positions]
        
        return domain_closed_positions_list
