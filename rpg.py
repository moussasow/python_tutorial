import random
import time
from character import Hero
from character import Foe
from stages import Stage
from shopping import Weapons

LEVEL_UP_KILLS = 5
kills = 0
weapon = Weapons()

input("Click any key to start the game! ")
name = input("Enter character name: ")
player = Hero(name, 100)
print(f"Welcome {player.name}!")

def get_monster_attack(m_life) :
    weapon = int(m_life/10)
    ma = 10 + (weapon * 3)
    ma += random.randint(0,weapon)
    return ma

def get_hero_attack(p_level) :
    attack = 10
    if p_level == 0:
        attack += random.randint(0,5)
    else:
        attack += p_level * 5
        attack += random.randint(p_level ,10 * p_level)

    return attack

def stage_change_animation():
    message = "Stage changed!"
    for i in range(len(message) + 1):
        print("\r" + message[:i], end="")
        time.sleep(0.2)
    print()

def set_stage(m_count):
    levels = Stage.get_levels_per_stage() 
    stage_count = levels * (Stage.current_stage + 1)
    if m_count == stage_count:
        Stage.stage_change_animation()
        Stage.update_stage()
        print(f"Entering stage:{Stage.current_stage}")
        print("♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪♪")
        player.update_shopping_status(True)

def shopping_weapon():
    weapon.show_inventory()
    str_id = input("Enter weapon number: ")
    id = int(str_id)
    strength, price = weapon.purchase_weapon(id, player.money)
    player.shopping_weapon(strength, price)

def start_shopping():
    # Create item type to function mapping
    item_functions = {
        'w': shopping_weapon,
        'a': lambda: print("armor"),
        'p': lambda: print("potion")
    }
    
    # Get item type from user
    item_type = input("Enter w -> weapon, a -> armor, p -> portion: ")
    
    # Get function for item type
    item_function = item_functions.get(item_type.lower())
    
    # Call function if it exists
    if item_function:
        item_function()
    else:
        print("Please come back again!")

def inquire_shopping() :
    if not player.can_shop:
        return

    player.update_shopping_status(False)
    shop = input("Enter shop to go shopping: ")
    if shop.lower() == 'shop':
        start_shopping()


input("Press any key to continue ")
while player.life > 0 :
    Stage.init_stages()
    set_stage(player.level)
    current_stage = Stage.current_stage
    player.update_stage(current_stage)
    health = Stage.stages[current_stage].get_health(player.level)

    inquire_shopping()

    monster = Foe(health)
    print("You met:")
    #print(f"current_stage = {current_stage}")
    monster.print_info()

    print(f"HP: {player.life} Potions: {player.potion_count}")
    use_potion = input("Press p to use potion: ")
    if use_potion.lower() == "p":
        use_count = input("How many? ")
        try:
            val = int(use_count)
            player.use_potion(val)
        except ValueError:
            pass

    while monster.life > 0:
        input("Click any key to attack: ")
        m_attack = get_monster_attack(monster.life)
        p_attack = get_hero_attack(player.level)
        monster.update_life(p_attack)
        player.receive_damage(m_attack)

        if monster.life <= 0 :
            print("You won!")
            kills += 1
            player.update_kills()
            drop = monster.potion_drop()
            money = monster.money_drop()
            player.update_potion(drop)
            player.update_money(money)
        elif player.life <= 0:
            print("You Lost!")
            break
    
    if kills >= LEVEL_UP_KILLS :
        player.level_up()
        player.update_life()
        kills = 0
        player.update_shopping_status(True)
        player.print_info()
else:
    print("Game over!")
    player.game_over()

input("Entry any key to quit!")
