inventory = ['El Caballero', 'RPG-7', 'Supercharger', '.308 Carbine', 'Tostador', 'La Clavadora']

rarity = {

    'El Caballero' : 92,
    'RPG-7' : 94,
    'Supercharger' : 97,
    '.308 Carbine' : 91,
    'Tostador' : 93,
    'La Clavadora' : 99
}

sort_inventory = sorted(inventory, key=rarity.__getitem__, reverse=True)

print (sort_inventory)

print(rarity.__getitem__('El Caballero'))