import random
super_effective = {
    "normal": set(),
    "fire": {"grass", "ice", "bug", "steel"},
    "water": {"fire", "ground", "rock"},
    "electric": {"water", "flying"},
    "grass": {"water", "ground", "rock"},
    "ice": {"grass", "ground", "flying", "dragon"},
    "fighting": {"normal", "ice", "rock", "dark", "steel"},
    "poison": {"grass", "fairy"},
    "ground": {"fire", "electric", "poison", "rock", "steel"},
    "flying": {"grass", "fighting", "bug"},
    "psychic": {"fighting", "poison"},
    "bug": {"grass", "psychic", "dark"},
    "rock": {"fire", "ice", "flying", "bug"},
    "ghost": {"psychic", "ghost"},
    "dragon": {"dragon"},
    "dark": {"psychic", "ghost"},
    "steel": {"ice", "rock", "fairy"},
    "fairy": {"fighting", "dragon", "dark"},
}
not_effective = {
    "normal": {"rock", "steel"},
    "fire": {"fire", "water", "rock", "dragon"},
    "water": {"water", "grass", "dragon"},
    "electric": {"electric", "grass", "dragon"},
    "grass": {"fire", "grass", "poison", "flying", "bug", "dragon", "steel"},
    "ice": {"fire", "water", "ice", "steel"},
    "fighting": {"poison", "flying", "psychic", "bug", "fairy"},
    "poison": {"poison", "ground", "rock", "ghost"},
    "ground": {"grass", "bug"},
    "flying": {"electric", "rock", "steel"},
    "psychic": {"psychic", "steel"},
    "bug": {"fire", "fighting", "poison", "flying", "ghost", "steel", "fairy"},
    "rock": {"fighting", "ground", "steel"},
    "ghost": {"dark"},
    "dragon": {"steel"},
    "dark": {"fighting", "dark", "fairy"},
    "steel": {"fire", "water", "electric", "steel"},
    "fairy": {"fire", "poison", "steel"},
}
immune = {
    "normal": {"ghost"},
    "ghost": {"normal", "fighting"},
    "ground": {"electric"},
    "flying": {"ground"},
    "dark": {"psychic"},
    "steel": {"poison"},
    "fairy": {"dragon"},
}

class Pokemon:
    def __init__(self,name,ptype,hp,shield,attacks):
 
        self.name = name
        self.type = ptype
        self.hp = hp
        self.shield = shield
        self.attacks = attacks
        
    def attack_target(self,attack,target): 
        if missed_attack():
            print(f"{self.name} used {attack.name} on {target.name} but it missed!\n")
            return
        
        mult = effectiveness(attack.type , target.type) 
        stab = STAB(self.type, attack.type)
        crit = critical_hit()

        damage = int(attack.power * mult * stab * crit)
        damage_soaked = 0

        if target.shield > 0:
            if damage <= target.shield:
                damage_soaked = damage
                target.shield -= damage
                damage = 0
            else:
                damage_soaked = target.shield
                damage -= target.shield
                target.shield = 0
        
        target.hp -= damage
        target.hp = max(target.hp, 0)

        text_effect = effectiveness_text(mult)
        text_crit = "A critical hit!" if crit > 1.0 else ""

        print(f"{self.name} uses {attack.name} on {target.name}!")
        if text_crit:
            print(text_crit)
        if text_effect:
            print(text_effect)

        print(f"{damage} damage and {damage_soaked} damage soaked by shield.")
        print(f"Hp: {target.hp} Shield: {target.shield}\n")

    def pokemon_info(self,i):
        return f"\n{i} - {self.name} (Type: {self.type}, HP: {self.hp}, Shield: {self.shield}) \n    ATTACKS: " + ", ".join([f"\n    {atk.name} (Type: {atk.type}, Power: {atk.power})" for atk in self.attacks])
class Attack:
    def __init__(self,name,ptype,power):
        self.name = name
        self.type = ptype
        self.power = power

def effectiveness(attacking, defending):
    if defending in immune and attacking in immune[defending]:
        return 0.0
    if defending in super_effective.get(attacking, set()):
        return 2.0
    if defending in not_effective.get(attacking, set()):
        return 0.5
    return 1.0  
def effectiveness_text(mult):
    if mult == 0:
        return "No effect!"
    if mult == 2:
        return "It's super effective!"
    if mult == 0.5:
        return "It's not very effective..."
    return ""
def critical_hit():
    return 1.5 if random.random() < (1/24) else 1.0
def STAB(attacker_type, attack_type):
    return 1.5 if attacker_type == attack_type else 1.0
def missed_attack():
    return random.random() < 0.05 


# Attacks
quick_attack = Attack("Quick Attack", "normal",30)  #Normal
tackle = Attack("Tackle", "normal", 35)             #Normal
scratch = Attack("Scratch", "normal", 35)           #Normal
ember = Attack("Ember", "fire", 50)                 #Fire
water_gun = Attack("Water Gun", "water", 40)        #Water
thunderbolt = Attack("Thunderbolt", "electric", 90) #Electric
vine_whip = Attack("Vine Whip", "grass", 45)        #Grass

# Pokemon 
def create_pikachu():
    return Pokemon("Pikachu", "electric", 100, 40, [thunderbolt, quick_attack])
def create_bulbasaur():
    return Pokemon("Bulbasaur", "grass", 120, 45, [vine_whip,tackle])
def create_charmander():
    return Pokemon("Charmander", "fire", 95, 30, [ember, scratch])
def create_squirtle():
    return Pokemon("Squirtle", "water", 110, 50, [water_gun, tackle])
pokemon_pools = [create_bulbasaur, create_charmander, create_squirtle]


# Game loop
def game_loop(player_pokemon, bot_pokemon):
    print(f"You chose  {player_pokemon.name}!")
    print(f"The bot was given {bot_pokemon.name}!\n")
    turn = 1
    while True :
        if player_pokemon.hp <= 0:
            print(f"{player_pokemon.name} has been defeated!\n\nYou lose!\n")
            return
        if bot_pokemon.hp <= 0:                                              # Switch break to return if i want restart support
            print(f"{bot_pokemon.name} has been defeated!\n\nYou win!\n")
            return 

        if turn == 1:
            print("Your turn!")
            for i, attack in enumerate(player_pokemon.attacks, 1):
                print(f"{attack.name} - {i}")
                print(f"  Type: {attack.type}, Power: {attack.power}")
            try:
                choice = int(input("Enter the attack number : ")) - 1
                selected_attack = player_pokemon.attacks[choice]
                player_pokemon.attack_target(selected_attack, bot_pokemon)
                
            except (ValueError, IndexError):
                print("Invalid choice, try again.")
                continue
            
        else:
            print(f"{bot_pokemon.name}'s turn!")
            bot_pokemon.attack_target(random.choice(bot_pokemon.attacks), player_pokemon)

        input("Press Enter to continue...\n")
        turn = 1 - turn

# Start Game
while True:
    for i, pokemon in enumerate(pokemon_pools, 1):
        print(pokemon().pokemon_info(i))
    try:
        choice = int(input("Choose your Pokemon with the corresponding number: ")) - 1
        player_pokemon = pokemon_pools[choice]()
        bot_pokemon = random.choice(pokemon_pools)()
    except (ValueError, IndexError):
        print("Invalid choice, try again.")
        continue
    game_loop(player_pokemon, bot_pokemon)
    replay = input("Play again? (y/n): ").strip().lower()
    if replay != 'y' and replay != 'yes':
        break
