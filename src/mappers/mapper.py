""""""
from abc import abstractmethod
from typing import Generic, TypeVar

Tin = TypeVar("Tin")
Tout = TypeVar("Tout")


class Mapper(Generic[Tin, Tout]):
    """The Mapper base class.

    Args:
        Generic (Generic): The types of the two models.
    """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def map(self, obj_a: Tin) -> Tout:
        pass
