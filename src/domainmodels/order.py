"""An Order."""
from enum import Enum
from typing import Optional


class Side(str, Enum):
    """The side of the order."""

    BUY = "buy"
    SELL = "sell"


class Type(str, Enum):
    """The type of the order."""

    MARKET = "market"
    LIMIT = "limit"
    STOP = "stop"
    STOP_LIMIT = "stop_limit"
    TRAILING_STOP = "trailing_stop"


class TimeInForce(str, Enum):
    """The time in force of the order."""

    DAY = "day"
    GOOD_TILL_CANCELLED = "gtc"
    MARKET_ON_OPEN = "opg"
    MARKET_ON_CLOSE = "cls"
    IMMIDIATE_OR_CANCEL = "ioc"
    FILL_OR_KILL = "fok"


class OrderClass(str, Enum):
    """The order class."""

    SIMPLE = "simple"
    BRACKET = "bracket"
    ONE_CANCELS_ORDER = "oco"
    ONE_TRIGGERS_ORDER = "oto"


class TakeProfit:
    """The take profit."""

    limit_price: float


class StopLoss:
    """The stop loss."""

    stop_price: float
    limit_price: float


class DomainOrder:
    """The domain order."""

    id: Optional[str] = None
    symbol: str
    qty: int
    side: Side = Side.BUY
    type: Type = Type.MARKET
    time_in_force: TimeInForce = TimeInForce.DAY
    limit_price: Optional[float] = None
    stop_price: Optional[float] = None
    extended_hours: Optional[bool] = None
    order_class: Optional[OrderClass] = None
    take_profit: Optional[TakeProfit] = None
    stop_loss: Optional[StopLoss] = None
    trail_price: Optional[float] = None
    trail_percent: Optional[float] = None
    notional: Optional[float] = None

    def __init__(self, symbol: str) -> None:
        """Class initiator function."""
        self.symbol = symbol
