from pom.engine.entity import Entity
from pom.game_play.move_component import MoveComponent
from pom.game_play.pom_sprite import PomSprite


class PomSpritePair(Entity):
    def __init__(self, p1: PomSprite, p2: PomSprite):
        super(PomSpritePair, self).__init__()
        self.move_component = MoveComponent(0, 0)
        self.sprites = [p1, p2]

    @property
    def id(self):
        return id(self)

    def update(self, dt: float):
        pass

    def get_components(self):
        return [
            self.move_component
        ]