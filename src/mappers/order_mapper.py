from alpaca_trade_api.entity import Order
from domainmodels.order import (
    DomainOrder,
    LimitPrice,
    Side,
    StopLoss,
    StopPrice,
    TakeProfit,
    TimeInForce,
    Type,
)

from mappers.mapper import Mapper


class OrderMapper(Mapper[Order, DomainOrder]):
    def map(self, order: Order) -> DomainOrder:

        # Order
        domain_order = DomainOrder(order.symbol)

        domain_order.id = order.client_order_id
        domain_order.qty = order.qty
        domain_order.side = Side[order.side]
        domain_order.type = Type[order.type]
        domain_order.time_in_force = TimeInForce[order.time_in_force]
        domain_order.limit_price = LimitPrice[order.limit_price]
        domain_order.stop_price = StopPrice[order.stop_price]
        domain_order.extended_hours = order.extended_hours
        domain_order.trail_price = order.trail_price
        domain_order.trail_percent = order.trail_percent
        domain_order.notional = order.notional

        # Take Profit
        take_profit = TakeProfit()
        take_profit.limit_price = order.take_profit.limit_price
        domain_order.take_profit = take_profit

        # Stop Loss
        stop_loss = StopLoss()
        stop_loss.limit_price = order.stop_loss.limit_price
        stop_loss.stop_price = order.stop_loss.stop_price
        domain_order.stop_loss = stop_loss

        return domain_order
