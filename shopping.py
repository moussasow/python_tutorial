class Weapons():
    weapons = [{"name": "Sword", "strength": 10, "price": 100},
               {"name": "Axe", "strength": 15, "price": 120},
               {"name": "Bow", "strength": 8, "price": 80},
               {"name": "Spear", "strength": 12, "price": 110},
               {"name": "Dagger", "strength": 5, "price": 50}]

    def __init__(self):
        print("Welcome to weaponery!")

    #w = Weapons()
	#strength, price = w.purchase_weapon("Sword")
    def purchase_weapon(self, name, amount):
        for weapon in self.weapons:
            if weapon["name"] == name:
                strength = weapon["strength"]
                price = weapon["price"]
                if amount < price:
                    print("You don't have enough money.")
                    return None, None
                self.weapons.remove(weapon)
                print(f"{name} has been purchased for {price}.")
                return strength, price
        print(f"{name} not found in the inventory.")
        return None, None

    def show_inventory(self):
        print("Welcome to weaponery!")
        for weapon in self.weapons:
            print(f"{weapon['name']}: Strength - {weapon['strength']}, Price - {weapon['price']}")