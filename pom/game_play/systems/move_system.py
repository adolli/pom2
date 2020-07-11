from typing import Iterable

from pom.game_play.move_component import MoveComponent


class MoveSystem(object):
    def __init__(self):
        super(MoveSystem, self).__init__()

    def update_components(self, dt: float, components: Iterable[MoveComponent]):
        print(dt)
        for com in components:
            vr, vc = com.velocity
            com.c += dt * vc
            com.r += dt * vr
