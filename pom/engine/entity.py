import weakref
from _weakref import ReferenceType
from abc import ABC
from threading import Lock
from typing import List, Dict, Set

import six

from pom.engine.component import Component
from pom.utils.singleton import Singleton


class Entity(ABC):
    def __init__(self):
        super(Entity, self).__init__()
        registry = EntityRegistry()
        registry.add(self)

    def update(self, dt: float):
        raise NotImplementedError

    def get_components(self) -> List[Component]:
        raise NotImplementedError


@six.add_metaclass(Singleton)
class EntityRegistry(object):
    def __init__(self):
        super(EntityRegistry, self).__init__()
        self.entities: Set[ReferenceType] = set()
        self.mutex = Lock()

    def add(self, e: Entity):
        ref = weakref.ref(e)
        self.entities.add(ref)

    def remove(self, e: Entity):
        ref = weakref.ref(e)
        self.entities.discard(ref)

    def get(self):
        ret = []
        with self.mutex:
            alive = []
            for r in self.entities:
                e = r()
                if e is not None:
                    ret.append(e)
                    alive.append(r)
            self.entities = set(alive)
        return ret
