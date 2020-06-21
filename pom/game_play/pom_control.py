from pom.engine.event_listener import EventListener
from pom.engine.event_system import EventSystem
from pom.game_play.game_event import PomMoveDownEvent


class PomMoveDownEventListener(EventListener):
    def on_trigger(self, event: PomMoveDownEvent):
        event.sandbox.move_down()


class PomControlSystem(object):
    def __init__(self, event_system: EventSystem):
        super(PomControlSystem, self).__init__()
        self.event_system = event_system
        self.pom_move_down_listener = PomMoveDownEventListener()
        self.event_system.register('pom-down', self.pom_move_down_listener)
