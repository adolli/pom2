from typing import Dict

import six

from pom.engine.entity import Entity
from pom.engine.event_system import EventSystem
from pom.game_play.pom_control import PomControlSystem
from pom.utils.singleton import Singleton


@six.add_metaclass(Singleton)
class World(object):
    def __init__(self):
        super(World, self).__init__()
        self.entities: Dict[int, Entity] = {}  # id -> Entity
        self.event_system = EventSystem()
        self.pom_control_system = PomControlSystem(self.event_system)
