import random
import time

class Stage:
    stages = []
    current_stage = 0  # Add a new class variable to hold the current stage
    levels_per_stage = 0
    number_of_stages = 0

    def __init__(self, level_ranges):
        self.level_ranges = level_ranges
        Stage.levels_per_stage = len(level_ranges)

    @classmethod
    def init_stages(cls):
        from game_config import stage1, stage2, stage3, stage4, stage5, stage6, stage7, stage8, stage9, stage10, stage11
        cls.stages = [stage1,
                      stage2,
                      stage3,
                      stage4,
                      stage5,
                      stage6,
                      stage7,
                      stage8,
                      stage9,
                      stage10,
                      stage11]

        cls.number_of_stages = len(cls.stages)

    def get_health(self, player_level):
        levels_stage = len(self.level_ranges)
        level_index = player_level % levels_stage
        down, up = self.level_ranges[level_index]
        health = random.randint(down, up)
        return health

    @classmethod
    def update_stage(cls):
        cls.current_stage += 1  # Update current stage

    @classmethod
    def get_levels_per_stage(cls):
        return cls.levels_per_stage

    @classmethod
    def stage_change_animation(cls):
        message = "♪♪♪♪♪♪♪♪♪♪"
        for i in range(len(message) + 1):
            print("\r" + message[:i], end="")
            time.sleep(0.2)
        print()