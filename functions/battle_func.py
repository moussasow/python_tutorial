import random

LEVEL_UP_KILLS = 5

def get_monster_attack(m_life) :
    weapon = int(m_life/10)
    ma = 10 + (weapon * 3)
    ma += random.randint(0,weapon)
    return ma

def get_hero_attack(p_level, p_weapon) :
    attack = 10
    if p_level == 0:
        attack += random.randint(0,5)
    else:
        attack += p_level * 5
        attack += random.randint(p_level ,10 * p_level)

    return attack + p_weapon

def attack_monster(player, monster):
    m_attack = get_monster_attack(monster.life)
    p_attack = get_hero_attack(player.level, player.weapon)
    monster.update_life(p_attack)
    player.receive_damage(m_attack)

def check_battle_status(player, monster):
    if monster.life <= 0:
        print("You won!")
        player.update_kills()
        drop = monster.potion_drop()
        money = monster.money_drop()
        player.update_potion(drop)
        player.update_money(money)
        return True
    elif player.life <= 0:
        print("You Lost!")
        return False
    return None

def level_up(player):
    if player.kills >= LEVEL_UP_KILLS:
        player.level_up()
        player.update_life()
        player.kills = 0
        player.update_shopping_status(True)
        player.print_info()
