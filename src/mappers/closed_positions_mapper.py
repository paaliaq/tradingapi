"""A mapper maps all day."""
from typing import Any

from domainmodels.closed_position import ClosedPosition, ClosedPositionError
from mappers.mapper import Mapper


class ClosedPositionMapper(Mapper[Any, ClosedPosition]):
    """Mapper to map from Any to ClosedPosition."""

    def map(self, position: Any) -> ClosedPosition:
        """Function to map from Any to ClosedPosition."""
        closed_position = ClosedPosition()
        closed_position.symbol = position.symbol
        closed_position.http_status_code = int(position.status)

        try:
            closed_position.order = position.body
        except:
            closed_position.order = None

        try:
            closed_position.error = ClosedPositionError()

            closed_position.error.available = int(position.body.available)
            closed_position.error.code = int(position.body.available)
            closed_position.error.existing_qty = int(position.body.existing_qty)
            closed_position.error.held_for_orders = int(position.body.held_for_orders)
            closed_position.error.message = position.body.held_for_orders.message
            closed_position.error.symbol = position.body.symbol
        except:
            closed_position.error = None

        return closed_position
