def print_best_weapon(weapon_list):
    best_weapon = ""
    max_damage = -1
    
    for weapon in weapon_list:
        name = weapon[0]
        damage = weapon[1]
        
        if damage > max_damage:
            max_damage = damage
            best_weapon = name
            
    print(best_weapon)

weapon1 = ("blade", 10)
weapon2 = ("sabre", 35)
weapon3 = ("sword", 50)
meele_weapon = [weapon1, weapon2, weapon3]

print_best_weapon(meele_weapon)