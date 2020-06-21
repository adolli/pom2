from abc import ABC
from typing import Optional

from pom.input.input_event import InputEvent


class InputDevice(ABC):
    def read(self) -> Optional[InputEvent]:
        raise NotImplementedError

