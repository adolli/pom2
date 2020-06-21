from abc import ABC

from pom.engine.event import Event


class EventListener(ABC):
    def on_trigger(self, event: Event):
        raise NotImplementedError
