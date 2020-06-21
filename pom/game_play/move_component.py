from pom.engine.component import Component


class MoveComponent(Component):
    def __init__(self, r: int, c: int):
        super(MoveComponent, self).__init__()
        self.r = r
        self.c = c
        self.velocity = 0.0
