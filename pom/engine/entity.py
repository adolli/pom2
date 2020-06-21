from abc import ABC
from typing import List

from pom.engine.component import Component


class Entity(ABC):
    @property
    def id(self):
        raise NotImplementedError

    def update(self, dt: float):
        raise NotImplementedError

    def get_components(self) -> List[Component]:
        raise NotImplementedError

