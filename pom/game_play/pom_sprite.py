from pom.engine.entity import Entity


class PomSprite(Entity):
    def __init__(self):
        super(PomSprite, self).__init__()

    def update(self, dt: float):
        pass

    def get_components(self):
        return []
