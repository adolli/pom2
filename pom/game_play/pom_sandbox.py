from typing import List, Optional

from pom.game_play.errors.game_play_error import GamePlayIllegalStateError
from pom.game_play.pom_sprite import PomSprite


class PomSandbox(object):
    def __init__(self):
        super(PomSandbox, self).__init__()
        self.width = 8  # cols
        self.height = 16  # rows
        self.container: List[List[Optional[PomSprite]]] = [[None for _ in range(self.width)] for _ in range(self.height)]

    def add(self, pom: PomSprite, r: int, c: int):
        if pom is None:
            raise ValueError("`sprite` object should not be None")
        if self.container[r][c] is not None:
            raise GamePlayIllegalStateError
        self.container[r][c] = pom

    def full(self) -> bool:
        raise NotImplementedError

