"""A mapper maps all day."""
from alpaca_trade_api.entity import Order
from domainmodels.order import (
    DomainOrder,
    OrderSide,
    StopLoss,
    TakeProfit,
    TimeInForce,
    Type,
)

from mappers.mapper import Mapper


class OrderMapper(Mapper[Order, DomainOrder]):
    """Mapper to map from Order to DomainOrder."""

    def map(self, order: Order) -> DomainOrder:
        """Function to map from Order to DomainOrder."""  # Order
        domain_order = DomainOrder(order.symbol)

        domain_order.id = order.id
        domain_order.qty = order.qty
        domain_order.side = OrderSide(order.side)
        domain_order.type = Type(order.type)
        domain_order.time_in_force = TimeInForce(order.time_in_force)
        domain_order.limit_price = order.limit_price
        domain_order.stop_price = order.stop_price
        domain_order.extended_hours = order.extended_hours
        domain_order.trail_price = order.trail_price
        domain_order.trail_percent = order.trail_percent
        domain_order.notional = order.notional

        # Take Profit
        try:
            take_profit = TakeProfit()
            take_profit.limit_price = (
                order.take_profit and order.take_profit.limit_price
            )
            domain_order.take_profit = take_profit
        except AttributeError:
            domain_order.take_profit = None

        # Stop Loss
        try:
            stop_loss = StopLoss()
            stop_loss.limit_price = order.stop_loss and order.stop_loss.limit_price
            stop_loss.stop_price = order.stop_loss and order.stop_loss.stop_price
            domain_order.stop_loss = stop_loss
        except AttributeError:
            domain_order.stop_loss = None

        return domain_order
