"""A mapper maps all day."""
from alpaca_trade_api.entity import Position
from domainmodels.position import AssetClass, DomainPosition, Exchange, PositionSide

from mappers.mapper import Mapper


class PositionMapper(Mapper[Position, DomainPosition]):
    """Mapper to map from Position to DomainPosition."""

    def map(self, position: Position) -> DomainPosition:
        """Function to map from Position to DomainPosition."""
        domain_position = DomainPosition()
        domain_position.symbol = position.symbol
        domain_position.qty = position.qty
        domain_position.asset_id = position.asset_id
        domain_position.asset_class = AssetClass(position.asset_class)
        domain_position.side = PositionSide(position.side)

        if hasattr(position, "exchange"):
            domain_position.exchange = Exchange(position.exchange)
        else:
            domain_position.exchange = Exchange.UNKNOWN

        if hasattr(position, "asset_marginable"):
            domain_position.asset_marginable = position.asset_marginable
        else:
            domain_position.asset_marginable = None
    
        if hasattr(position, "avg_entry_price"):
            domain_position.avg_entry_price = position.avg_entry_price
        else:
            domain_position.avg_entry_price = None

        if hasattr(position, "market_value"):
            domain_position.market_value = position.market_value
        else:
            domain_position.market_value = None

        if hasattr(position, "cost_basis"):
            domain_position.cost_basis = position.cost_basis
        else:
            domain_position.cost_basis = None

        if hasattr(position, "unrealized_pl"):
            domain_position.unrealized_pl = position.unrealized_pl
        else:
            domain_position.unrealized_pl = None

        if hasattr(position, "unrealized_plpc"):
            domain_position.unrealized_plpc = position.unrealized_plpc
        else:
            domain_position.unrealized_plpc = None

        if hasattr(position, "unrealized_intraday_pl"):
            domain_position.unrealized_intraday_pl = position.unrealized_intraday_pl
        else:
            domain_position.unrealized_intraday_pl = None

        if hasattr(position, "unrealized_intraday_plpc"):
            domain_position.unrealized_intraday_plpc = position.unrealized_intraday_plpc
        else:
            domain_position.unrealized_intraday_plpc = None

        if hasattr(position, "current_price"):
            domain_position.current_price = position.current_price
        else:
            domain_position.current_price = None

        if hasattr(position, "lastday_price"):
            domain_position.lastday_price = position.lastday_price
        else:
            domain_position.lastday_price = None

        if hasattr(position, "change_today"):
            domain_position.change_today = position.change_today
        else:
            domain_position.change_today = None

        return domain_position
