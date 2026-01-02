import pygame
import random
pygame.init()
pygame.display.set_caption("Pokemon Game")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 28)

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
    def __init__(self, name, ptype, hp, shield, attacks, image_path, position =(0,0)):
 
        self.name = name
        self.type = ptype
        self.hp = hp
        self.max_hp = hp
        self.shield = shield
        self.max_shield = shield
        self.attacks = attacks
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=position)
    def attack_target(self,attack,target): 
        log = []
        if missed_attack():
            return f"{self.name}'s {attack.name} missed!"
        
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
        
        target.hp = max(target.hp - damage, 0)

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
    if defending in immune and attacking in immune[defending]:  return 0.0
    if defending in super_effective.get(attacking, set()):  return 2.0
    if defending in not_effective.get(attacking, set()):    return 0.5
    return 1.0  
def effectiveness_text(mult):
    if mult == 0:   return "No effect!"
    if mult == 2:   return "It's super effective!"
    if mult == 0.5:return "It's not very effective..."
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
    return Pokemon("Pikachu", "electric", 100, 40, [thunderbolt, quick_attack], "pokemon_project/Pokemon_images/pikachu.png")
def create_bulbasaur():
    return Pokemon("Bulbasaur", "grass", 120, 45, [vine_whip,tackle], "pokemon_project/Pokemon_images/bulbasaur.png")
def create_charmander():
    return Pokemon("Charmander", "fire", 95, 30, [ember, scratch], "pokemon_project/Pokemon_images/charmander.png")
def create_squirtle():
    return Pokemon("Squirtle", "water", 110, 50, [water_gun, tackle], "pokemon_project/Pokemon_images/squirtle.png")
pokemon_pools = [create_pikachu, create_bulbasaur, create_charmander, create_squirtle]
player = random.choice(pokemon_pools)()
bot = random.choice(pokemon_pools)()


player.rect.topleft = (100, 300)
bot.rect.topleft = (500, 100)
selected_attack = 0
player_turn = True
message = ""
running = True
while running:
    screen.fill((255,255,255))
    screen.blit(player.image, (100, 300))
    screen.blit(bot.image, (500, 100))  
    if bot.hp <= 0:
        message = "You win!"

    if player.hp <= 0:
        message = "You lost!"
        
    if player.hp <= 0 or bot.hp <= 0:
        running = False
    for p in [player, bot]:
        # HP bar
        pygame.draw.rect(screen, (255,0,0), (p.rect.x, p.rect.y - 20, 100, 10))
        pygame.draw.rect(screen, (0,255,0), (p.rect.x, p.rect.y - 20, 100 * (p.hp/p.max_hp), 10))
        # Shield bar
        pygame.draw.rect(screen, (128,128,128), (p.rect.x, p.rect.y - 10, 100, 5))
        shield_ratio = p.shield / p.max_shield if p.max_shield > 0 else 0
        pygame.draw.rect(screen, (0,0,255),(p.rect.x, p.rect.y - 10, 100 * shield_ratio, 5))

    # Draw attack list
    if player_turn:
        for i, atk in enumerate(player.attacks):
            color = (255,0,0) if i == selected_attack else (0,0,0)
            text = font.render(f"{i+1}. {atk.name} (Power:{atk.power})", True, color)
            screen.blit(text, (50,50 + i*30))


    msg_surface = font.render(message, True, (0,0,0))
    screen.blit(msg_surface, (50, 10))
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and player_turn:
            if event.key == pygame.K_DOWN:
                selected_attack = (selected_attack + 1) % len(player.attacks)
            elif event.key == pygame.K_UP:
                selected_attack = (selected_attack - 1) % len(player.attacks)
            elif event.key == pygame.K_RETURN:
                message = player.attack_target(player.attacks[selected_attack], bot)
                player_turn = False

    if not player_turn:
        pygame.time.delay(500)
        message = bot.attack_target(random.choice(bot.attacks), player)
        player_turn = True

    clock.tick(30)

pygame.quit()