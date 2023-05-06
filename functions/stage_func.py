import time
from stages import Stage

def stage_change_animation():
    message = "Stage changed!"
    for i in range(len(message) + 1):
        print("\r" + message[:i], end="")
        time.sleep(0.2)
    print()

def set_stage(player):
    levels = Stage.get_levels_per_stage() 
    stage_count = levels * (Stage.current_stage + 1)
    if player.level == stage_count:
        Stage.stage_change_animation()
        Stage.update_stage()
        next_stage = Stage.current_stage + 1
        print(f"Entering stage:{next_stage}")
        print("♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪")
        player.update_shopping_status(True)

def initialize_stage(player):
    Stage.init_stages()
    set_stage(player)
    current_stage = Stage.current_stage
    player.update_stage(current_stage)
    return current_stage