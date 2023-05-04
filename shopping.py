class Weapons():
    weapons = [{"id": 1, "name": "Sword", "strength": 10, "price": 100},
               {"id": 2, "name": "Axe", "strength": 15, "price": 120},
               {"id": 3, "name": "Bow", "strength": 8, "price": 80},
               {"id": 4, "name": "Spear", "strength": 12, "price": 110},
               {"id": 5, "name": "Dagger", "strength": 5, "price": 50}]

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