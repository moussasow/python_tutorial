class Weapons():
    weapons = [{"id": 1, "name": "Sword", "strength": 10, "price": 10000},
               {"id": 2, "name": "Axe", "strength": 15, "price": 12000},
               {"id": 3, "name": "Bow", "strength": 8, "price": 8000},
               {"id": 4, "name": "Spear", "strength": 12, "price": 11000},
               {"id": 5, "name": "Dagger", "strength": 5, "price": 2500},
               {"id": 6, "name": "Club", "strength": 2, "price": 500}]

    def __init__(self):
        pass

    #w = Weapons()
	#strength, price = w.purchase_weapon("Sword")
    def purchase_weapon(self, id, amount):
        for weapon in self.weapons:
            if weapon["id"] == id:
                strength = weapon["strength"]
                price = weapon["price"]
                if amount < price:
                    print("You dont have enough money.")
                    return 0, 0
                self.weapons.remove(weapon)
                print(f"{weapon['name']} has been purchased for {price}.")
                return strength, price
        print(f"Weapon with id {id} not found in the inventory.")
        return 0, 0

    def show_inventory(self):
        print("Welcome to weaponery!")
        for weapon in self.weapons:
             print(f"{weapon['id']}: {weapon['name']}: Strength - {weapon['strength']}, Price - {weapon['price']}")


class Armors():
    armors = [{"id": 1, "name": "Leather Armor", "defense": 5, "price": 5000},
              {"id": 2, "name": "Chainmail Armor", "defense": 10, "price": 10000},
              {"id": 3, "name": "Plate Armor", "defense": 15, "price": 15000},
              {"id": 4, "name": "Dragon Scale Armor", "defense": 20, "price": 20000}]

    def __init__(self):
        pass

    def purchase_armor(self, id, amount):
        for armor in self.armors:
            if armor["id"] == id:
                defense = armor["defense"]
                price = armor["price"]
                if amount < price:
                    print("You dont have enough money.")
                    return 0, 0
                self.armors.remove(armor)
                print(f"{armor['name']} has been purchased for {price}.")
                return defense, price
        print(f"Armor with id {id} not found in the inventory.")
        return 0, 0

    def show_inventory(self):
        print("Welcome to the armory!")
        for armor in self.armors:
            print(f"{armor['id']}: {armor['name']}: Defense - {armor['defense']}, Price - {armor['price']}")        

class Potions():

    potions = [{"id": 1, "name": "Health Potion", "healing": 10, "price": 100},
               {"id": 2, "name": "Mana Potion", "mana": 10, "price": 100},
               {"id": 3, "name": "Stamina Potion", "stamina": 10, "price": 100}]

    def __init__(self):
        pass

    def show_inventory(self):
        print("Welcome to the potion shop!")
        for potion in self.potions:
            if 'healing' in potion:
                print(f"{potion['id']}: {potion['name']}: Healing - {potion['healing']}, Price - {potion['price']}")
            elif 'mana' in potion:
                print(f"{potion['id']}: {potion['name']}: Mana - {potion['mana']}, Price - {potion['price']}")
            elif 'stamina' in potion:
                print(f"{potion['id']}: {potion['name']}: Stamina - {potion['stamina']}, Price - {potion['price']}")

    def purchase_potion(self, id, amount):
        for potion in self.potions:
            if potion["id"] == id:
                price = potion["price"]
                if amount < price:
                    print("You dont have enough money.")
                    return 0,0
                self.potions.remove(potion)
                print(f"{potion['name']} has been purchased for {price}.")
                return id, price
        print(f"Potion with id {id} not found in the inventory.")
        return 0,0        