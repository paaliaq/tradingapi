"""A mapper maps all day."""
from alpaca_trade_api.entity import Position
from domainmodels.position import AssetClass, DomainPosition, Exchange, Side

from mappers.mapper import Mapper


class PositionMapper(Mapper[Position, DomainPosition]):
    """Mapper to map from Position to DomainPosition."""

    def map(self, position: Position) -> DomainPosition:
        """Function to map from Position to DomainPosition.""" 

        domain_position = DomainPosition(position.symbol)
        domain_position.asset_id = position.asset_id 
        domain_position.asset_marginable = position.asset_marginable
        domain_position.qty = position.qty
        domain_position.avg_entry_price = position.avg_entry_price
        domain_position.market_value = position.market_value
        domain_position.cost_basis = position.cost_basis
        domain_position.unrealized_pl = position.unrealized_pl
        domain_position.unrealized_plpc = position.unrealized_plpc
        domain_position.unrealized_intraday_pl = position.unrealized_intraday_pl
        domain_position.unrealized_intraday_plpc = position.unrealized_intraday_plpc
        domain_position.current_price = position.current_price
        domain_position.lastday_price = position.lastday_price
        domain_position.change_today = position.change_today

        domain_position.exchange = Exchange(position.exchange)
        domain_position.asset_class = AssetClass(position.asset_class)
        domain_position.side = Side(position.side)

        return domain_position
