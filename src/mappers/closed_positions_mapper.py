"""A mapper maps all day."""
from typing import Any

from domainmodels.closed_position import ClosedPosition, ClosedPositionError

from mappers.mapper import Mapper


# noinspection PyBroadException
class ClosedPositionMapper(Mapper[Any, ClosedPosition]):
    """Mapper to map from Any to ClosedPosition."""

    def map(self, position: Any) -> ClosedPosition:
        """Function to map from Any to ClosedPosition."""
        closed_position = ClosedPosition()
        closed_position.symbol = position.symbol
        closed_position.http_status_code = int(position.status)
        closed_position.error = None

        try:
            closed_position.order = position.body
        except Exception:
            closed_position.order = None

            closed_position.error = ClosedPositionError()

            # These two fields seem wrong as well
            closed_position.error.available = int(position.body.available)
            closed_position.error.code = 0
            closed_position.error.existing_qty = int(position.body.existing_qty)
            closed_position.error.held_for_orders = int(position.body.held_for_orders)
            closed_position.error.message = position.body.held_for_orders.message
            closed_position.error.symbol = position.body.symbol

        return closed_position
