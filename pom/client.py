import time

from pom.display.debug_console import DebugConsole
from pom.game_play.move_component import MoveComponent
from pom.game_play.world import World
from pom.game_play.game_event import PomMoveDownEvent
from pom.game_play.pom_sandbox import PomSandbox
from pom.game_play.pom_sprite import PomSprite
from pom.game_play.pom_sprite_pair import PomSpritePair



if __name__ == '__main__':

    world = World()
    sandbox = PomSandbox()
    p0 = PomSprite()
    p1 = PomSprite()
    p2 = PomSprite()
    pp = PomSpritePair(p1, p2)
    sandbox.put(pp)

    # down = PomMoveDownEvent(sandbox)
    # down2 = PomMoveDownEvent(sandbox)
    # world.event_system.send(down)
    # world.event_system.send(down2)

    display = DebugConsole()
    world.set_display_device(display)

    world.on_start()
    for i in range(10):
        time.sleep(0.033)  # 只用10 frames做测试
        world.on_frame()
        sandbox.print_state()

