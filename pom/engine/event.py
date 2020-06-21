from abc import ABC


class Event(ABC):
    @property
    def name(self) -> str:
        raise NotImplementedError

    @property
    def payload(self):
        return None
