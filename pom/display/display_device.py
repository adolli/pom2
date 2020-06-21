from abc import ABC


class DisplayDevice(ABC):
    def flush_buffer(self):
        raise NotImplementedError

    def render(self):
        raise NotImplementedError
