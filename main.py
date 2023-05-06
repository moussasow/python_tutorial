import random
from character import Hero
from character import Foe
from stages import Stage
from shopping import Weapons, Armors, Potions
from functions.battle_func import *
from functions.shop_func import *
from functions.stage_func import initialize_stage, set_stage, stage_change_animation

weapon = Weapons()
armor = Armors()
potion = Potions()

def use_potion(player):
    print(f"HP: {player.life} Potions: {player.potion_count}")
    use_potion = input("Press p to use potion: ")
    if use_potion.lower() == "p":
        use_count = input("How many? ")
        try:
            val = int(use_count)
            player.use_potion(val)
        except ValueError:
            pass

def init_monster(current_stage, p_level):
    health = Stage.stages[current_stage].get_health(p_level)
    monster = Foe(health)
    print("Next opponent:")
    monster.print_info()
    return monster

input("Click any key to start the game! ")
name = input("Enter character name: ")
player = Hero(name, 100)
print(f"Welcome {player.name}!")

input("Press any key to continue ")
while player.life > 0 :
    current_stage = initialize_stage(player)
    if current_stage == Stage.number_of_stages:
        player.game_cleared()
        break

    inquire_shopping(player, weapon, armor, potion)

    monster = init_monster(current_stage, player.level)

    use_potion(player)

    while monster.life > 0:
        input("Click any key to attack: ")
        attack_monster(player, monster)
        battle_status = check_battle_status(player, monster)
        if battle_status is not None:
            break

    level_up(player)

else:
    player.game_over()

input("Entry any key to quit!")
