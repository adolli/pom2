from collections import defaultdict
from queue import Queue
from threading import Lock
from typing import Dict, List

from pom.engine.event import Event
from pom.engine.event_listener import EventListener


class EventSystem(object):
    def __init__(self):
        super(EventSystem, self).__init__()
        self._listeners: Dict[str, List[EventListener]] = defaultdict(list)  # name -> listeners
        self._events = Queue()
        self._event_queue_mutex = Lock()

    def _dispatch(self, event: Event):
        for listener in self._listeners[event.name]:
            try:
                listener.on_trigger(event)
            except Exception as e:
                raise

    def dispatch_queued_events(self):
        with self._event_queue_mutex:
            q = self._events
            self._events = Queue()
        for e in q.get():
            self._dispatch(e)

    def register(self, name, listener: EventListener):
        self._listeners[name].append(listener)

    def send(self, event: Event):
        self._events.put(event)
