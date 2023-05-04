import urllib.request
from urllib.error import URLError
import json
import random

POTION = "🧴"
MONEY = "Glems"

class Hero() :
    def __init__(self, name, life) :
        self.name = name
        self.life = life
        self.level = 0
        self.kills = 0
        self.hero_life = life
        self.potion_count = 1
        self.monster_count = 0
        self.stage = 0
        self.money = 0

    def update_life(self):
        self.life = self.hero_life

    def update_potion(self, count):
        self.potion_count += count

    def update_money(self, money):
        self.money += money

    def use_potion(self, potions):
        if self.potion_count < potions:
            print("You don't have enough potions")
            return

        healing = 20 + (10 * self.stage)
        self.life += healing * potions
        self.potion_count -= potions
        if self.life > self.hero_life:
            self.life = self.hero_life

        print("Your life is", self.life)

    def receive_damage(self, attack) :
        self.life -= attack
        print("You suffered", attack, "damage!")

    def update_kills(self) :
        self.kills += 1
        self.monster_count += 1

    def level_up(self) :
        self.level += 1
        self.hero_life += 20 + (10 * self.stage)
        reward_potions = random.randint(0, self.level)
        self.potion_count += reward_potions
        print("########################")
        print("Level up!")
        print("♥♥♥♥♥♥♥♥♥♥")
        print(f"Your reward is {reward_potions}{POTION}")

    def update_stage(self, stage):
        self.stage = stage    

    def print_info(self) :
        print(f"{self.name}, Level:{self.level} HP:{self.life} Money:{self.money} {MONEY}")

    def game_over(self) :
        print("Your level is", self.level, " and defeated", self.kills, "monsters!")

class Foe() :
    def __init__(self, life) :
        self.life = life
        self.max_drop = life
        first, last, country = self.generate_name()
        self.name = f"{first} {last}"
        self.country = country
    
    def update_life(self, attack) :
        self.life -= attack
        print("You inflicted", attack, "damage!")
    
    def print_info(self) :
        print("-----------------------")
        print("Opponent information")
        print("Name:", self.name)
        print("HP:", self.life)
        print("Country:", self.country)
        print("-----------------------")

    def potion_drop(self):
        drop = 0
        chance = random.randint(0,10)
        if chance % 3:
            drop = random.randint(0, 2)
            if drop >= 1:
                print("♥♥♥♥♥♥♥♥♥♥")
                print(self.name, "has dropped", drop, POTION)
                print("♥♥♥♥♥♥♥♥♥♥")

        return drop

    def money_drop(self):
        money = random.randint(1, self.max_drop)
        print(f"{self.name} has dropped {money} {MONEY}")
        return money

    def generate_name(self) -> list:
        try:
            with urllib.request.urlopen('https://randomuser.me/api/') as f:
                text = f.read()
                json_dict = json.loads(text)
                results = json_dict['results']
                for item in results:
                    full_name = item['name']
                    first = full_name['first']
                    last = full_name['last']
                    location = item['location']
                    country = location['country']

                return [first, last, country]
        except URLError as e:
            print(f'An error occurred: {e}')
            return ["Server", "error", "Japan"]
