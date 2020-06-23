import weakref
from _weakref import ReferenceType
from collections import defaultdict
from threading import Lock
from typing import Set, Dict

import six

from pom.utils.singleton import Singleton


class Component(object):
    def __init__(self):
        super(Component, self).__init__()
        registry = ComponentRegistry()
        registry.add(self)


@six.add_metaclass(Singleton)
class ComponentRegistry(object):
    def __init__(self):
        super(ComponentRegistry, self).__init__()
        self.components: Dict[str, Set[ReferenceType]] = defaultdict(set)
        self.mutex = Lock()

    def add(self, c: Component):
        name = c.__class__.__name__
        ref = weakref.ref(c)
        self.components[name].add(ref)

    def remove(self, c: Component):
        name = c.__class__.__name__
        ref = weakref.ref(c)
        self.components[name].discard(ref)

    def get(self, cls):
        ret = []
        with self.mutex:
            alive = []
            refs = self.components[cls.__name__]
            for r in refs:
                c = r()
                if c is not None:
                    ret.append(c)
                    alive.append(r)
            self.components[cls.__name__] = set(alive)
        return ret
