def shopping_weapon(player, weapon):
    weapon.show_inventory()
    str_id = input("Enter weapon number: ")
    item_id = int(str_id)
    strength, price = weapon.purchase_weapon(item_id, player.money)
    player.shopping_weapon(strength, price)

def shopping_armor(player, armor):
    armor.show_inventory()
    str_id = input("Enter armor number: ")
    item_id = int(str_id)
    defense, price = armor.purchase_armor(item_id, player.money)
    player.shopping_armor(defense, price)

def shopping_potion(player, potion):
    potion.show_inventory()
    str_id = input("Enter potion number: ")
    item_id = int(str_id)
    strength, price = potion.purchase_potion(item_id, player.money)
    player.shopping_potions(strength, price)   

def start_shopping(player, weapon, armor, potion):
    # Create item type to function mapping
    item_functions = {
        'w': (shopping_weapon, (player, weapon)),
        'a': (shopping_armor, (player, armor)),
        'p': (shopping_potion, (player, potion))
    }
    
    # Get item type from user
    item_type = input("Enter w -> weapon, a -> armor, p -> portion: ")
    
    # Get function for item type
    item_function, args = item_functions.get(item_type.lower(), (None, None))
    
    # Call function if it exists
    if item_function:
        item_function(*args)
    else:
        print("Please come back again!")

def inquire_shopping(player, weapon, armor, potion) :
    if not player.can_shop:
        return

    player.update_shopping_status(False)
    shop = input("Enter shop to go shopping: ")
    if shop.lower() == 'shop':
        start_shopping(player, weapon, armor, potion)