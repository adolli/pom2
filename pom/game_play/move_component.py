from typing import Tuple

from pom.engine.component import Component


class MoveComponent(Component):
    def __init__(self, r: float, c: float):
        super(MoveComponent, self).__init__()
        self.r: float = r
        self.c: float = c
        self.velocity: Tuple[float, float] = (-1.0, 0.0)
