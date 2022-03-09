"""A mapper maps all day."""
from alpaca_trade_api.entity import Position
from domainmodels.position import AssetClass, DomainPosition, Exchange, PositionSide

from mappers.mapper import Mapper


class PositionMapper(Mapper[Position, DomainPosition]):
    """Mapper to map from Position to DomainPosition."""

    def sa(
        self, domain_position: DomainPosition, position: Position, attr: str
    ) -> DomainPosition:
        """Auxilary function to set attribute in domain_position if it's in position."""
        if hasattr(position, attr):
            new_val = getattr(position, attr)
            setattr(domain_position, attr, new_val)
        else:
            setattr(domain_position, attr, None)
        return domain_position

    def map(self, position: Position) -> DomainPosition:
        """Function to map from Position to DomainPosition."""
        domain_position = DomainPosition()
        domain_position.symbol = position.symbol
        domain_position.qty = position.qty
        domain_position.asset_id = position.asset_id
        domain_position.asset_class = AssetClass(position.asset_class)
        domain_position.side = PositionSide(position.side)

        # Special case
        if hasattr(position, "exchange"):
            domain_position.exchange = Exchange(position.exchange)
        else:
            domain_position.exchange = Exchange.UNKNOWN

        # General cases
        domain_position = self.sa(domain_position, position, "asset_marginable")
        domain_position = self.sa(domain_position, position, "avg_entry_price")
        domain_position = self.sa(domain_position, position, "market_value")
        domain_position = self.sa(domain_position, position, "cost_basis")
        domain_position = self.sa(domain_position, position, "unrealized_pl")
        domain_position = self.sa(domain_position, position, "unrealized_plpc")
        domain_position = self.sa(domain_position, position, "unrealized_intraday_pl")
        domain_position = self.sa(domain_position, position, "unrealized_intraday_plpc")
        domain_position = self.set_attr(domain_position, position, "current_price")
        domain_position = self.set_attr(domain_position, position, "lastday_price")
        domain_position = self.set_attr(domain_position, position, "change_today")

        return domain_position
