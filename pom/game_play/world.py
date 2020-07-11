import traceback
from _weakref import ReferenceType
from collections import defaultdict
from typing import Dict, Set, Optional

import six
import time

from pom.display.display_device import DisplayDevice
from pom.engine.component import ComponentRegistry
from pom.engine.entity import Entity, EntityRegistry
from pom.engine.event_system import EventSystem
from pom.game_play.move_component import MoveComponent
from pom.game_play.pom_control import PomControlSystem
from pom.game_play.systems.move_system import MoveSystem
from pom.utils.singleton import Singleton


@six.add_metaclass(Singleton)
class World(object):
    def __init__(self):
        super(World, self).__init__()
        self.entities = EntityRegistry()
        self.component_registry = ComponentRegistry()
        self.move_system = MoveSystem()
        self.event_system = EventSystem()
        self.pom_control_system = PomControlSystem(self.event_system)
        self.display_device: Optional[DisplayDevice] = None
        self._prev_ts = 0

    def on_start(self):
        self._prev_ts = time.time()

    def on_frame(self):
        # refresh components
        now = time.time()
        dt = now - self._prev_ts
        mc = self.component_registry.get(MoveComponent)
        try:
            self.move_system.update_components(dt, mc)
        except Exception as e:
            traceback.print_exc()

        # refresh entities
        for e in self.entities.get():
            now = time.time()
            dt = now - self._prev_ts
            try:
                e.update(dt)
            except Exception as e:
                traceback.print_exc()

    def set_display_device(self, d):
        self.display_device = d
