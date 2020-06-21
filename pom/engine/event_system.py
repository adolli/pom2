from collections import defaultdict
from typing import Dict, List

from pom.engine.event import Event
from pom.engine.event_listener import EventListener


class EventSystem(object):
    def __init__(self):
        super(EventSystem, self).__init__()
        self._listeners: Dict[str, List[EventListener]] = defaultdict(list)  # name -> listeners

    def dispatch(self, event: Event):
        for listener in self._listeners[event.name]:
            try:
                listener.on_trigger(event)
            except Exception as e:
                raise

    def register(self, name, listener: EventListener):
        self._listeners[name].append(listener)
