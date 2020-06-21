from abc import ABC

from pom.engine.event import Event


class InputEvent(Event, ABC):
    pass
