from pprint import pprint
from typing import List, Optional

from pom.engine.component import Component
from pom.engine.entity import Entity
from pom.game_play.errors.game_over import GameOver
from pom.game_play.errors.game_play_error import GamePlayIllegalStateError
from pom.game_play.pom_sprite import PomSprite
from pom.game_play.pom_sprite_pair import PomSpritePair


class PomSandbox(Entity):
    def __init__(self):
        super(PomSandbox, self).__init__()
        self.width = 7  # cols
        self.height = 12  # rows
        self.container: List[List[Optional[PomSprite]]] = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.floating: Optional[PomSpritePair] = None

    def settle(self):
        pair = self.floating
        if pair is None:
            raise GamePlayIllegalStateError

        # 检查pair自身越界
        r = pair.move_component.r
        c = pair.move_component.c
        if r < 0 or r + 1 >= self.height:
            raise ValueError(f"row under/overflow r={r}")
        if c < 0 or c >= self.width:
            raise ValueError(f"col under/overflow c={c}")

        # 检查是否被阻挡
        if self.container[r][c] is not None or self.container[r + 1][c] is not None:
            raise GamePlayIllegalStateError

        # 检查游戏结束
        if self.full:
            raise GameOver
        self.container[r][c] = pair.sprites[0]
        if self.full:
            raise GameOver
        self.container[r + 1][c] = pair.sprites[1]
        self.floating = None
        self.eliminate()

    def can_settle(self) -> bool:
        if self.floating is None:
            raise GamePlayIllegalStateError
        r = self.floating.move_component.r
        c = self.floating.move_component.c

        # 已经达到底部
        if r == 0:
            return True

        # 下面有了
        if self.container[r - 1][c] is not None:
            return True
        return False

    @property
    def full(self) -> bool:
        raise NotImplementedError

    def eliminate(self):
        raise NotImplementedError

    def put(self, pair: PomSpritePair):
        pair.move_component.r = self.height - 1
        pair.move_component.c = self.width // 2
        self.floating = pair

    def move_down(self):
        if self.floating is not None:
            self.floating.move_component.r -= 1
            if self.can_settle():
                self.settle()

    @property
    def id(self):
        return id(self)

    def update(self, dt: float):
        pass

    def get_components(self) -> List[Component]:
        pass

    def print_state(self):
        import copy
        container = copy.deepcopy(self.container)
        for r, row in enumerate(container):
            for c, pom in enumerate(row):
                if pom is not None:
                    container[r][c] = "x"
                else:
                    container[r][c] = " "
        f = self.floating.move_component
        container[f.r][f.c] = "F"
        container[f.r + 1][f.c] = "F"
        pprint(list(reversed(container)))
