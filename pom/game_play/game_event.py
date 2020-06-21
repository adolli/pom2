from abc import ABC

from pom.engine.event import Event
from pom.game_play.pom_sandbox import PomSandbox


class GameEvent(Event, ABC):
    pass


class NoopEvent(GameEvent):
    def __init__(self):
        super(NoopEvent, self).__init__()


class PomMoveDownEvent(GameEvent):
    def __init__(self, sandbox: PomSandbox):
        super(PomMoveDownEvent, self).__init__()
        self.sandbox = sandbox

    @property
    def name(self) -> str:
        return 'pom-down'


class PomMoveLeftEvent(GameEvent):
    def __init__(self):
        super(PomMoveLeftEvent, self).__init__()


class PomMoveRightEvent(GameEvent):
    def __init__(self):
        super(PomMoveRightEvent, self).__init__()
