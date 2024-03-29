"""Base class for trading APIs."""
import os
from abc import ABC, abstractmethod
from collections import OrderedDict
from datetime import datetime
from typing import Any, Dict, List, Optional

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


class BaseApi(ABC):
    """Base class for trading APIs.

    This class was inspired by the methods from alpaca-trade-api-python.
    For reference, please see: https://github.com/alpacahq/alpaca-trade-api-python
    """

    def __init__(self, env_dict: Dict) -> None:
        """Class initialization function."""
        # Check inputs
        is_dict = isinstance(env_dict, dict) or isinstance(env_dict, OrderedDict)
        if not is_dict:
            raise ValueError("env_dict must be a dictionary.")

        values_are_strings = all([isinstance(v, str) for v in env_dict.values()])
        if not values_are_strings:
            raise ValueError("All values in env_dict must be strings.")

        # Set environment variables
        for k, v in env_dict.items():
            os.environ[k] = v

    @abstractmethod
    async def get_account(self) -> DomainAccount:
        """Get the account."""
        pass

    @abstractmethod
    async def get_clock(self) -> DomainClock:
        """Get the clock."""
        pass

    @abstractmethod
    async def get_trading_days(
        self, start: datetime, end: datetime
    ) -> List[TradingDay]:
        """Get the calendars."""
        pass

    @abstractmethod
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
        """
        pass

    @abstractmethod
    async def list_orders(self, **kwargs: Any) -> List[DomainOrder]:
        """Get a list with all orders."""
        pass

    @abstractmethod
    async def get_order(self, order_id: str, **kwargs: Any) -> DomainOrder:
        """Get an order with specific order_id."""
        pass

    @abstractmethod
    async def cancel_order(self, order_id: str, **kwargs: Any) -> None:
        """Cancel an order with specific order_id."""
        pass

    @abstractmethod
    async def cancel_all_orders(self, **kwargs: Any) -> None:
        """Cancel all orders."""
        pass

    @abstractmethod
    async def list_positions(self, **kwargs: Any) -> List[DomainPosition]:
        """Get a list of open positions."""
        pass

    @abstractmethod
    async def get_position(self, symbol: str, **kwargs: Any) -> DomainPosition:
        """Get an open position for a symbol."""
        pass

    @abstractmethod
    async def close_position(self, symbol: str, **kwargs: Any) -> DomainOrder:
        """Liquidates the position for the given symbol at market price."""
        pass

    @abstractmethod
    async def close_all_positions(self, **kwargs: Any) -> List[ClosedPosition]:
        """Liquidates all open positions at market price."""
        pass
