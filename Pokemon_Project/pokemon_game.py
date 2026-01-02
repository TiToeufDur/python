import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pokemon Game")
pokemons = pygame.sprite.Group()

class Pokemon(pygame.sprite.Sprite):
    def __init__(self, name, ptype, hp, shield, attacks, image_path=None):
        super().__init__()
        self.name = name
        self.type = ptype
        self.hp = hp
        self.shield = shield
        self.attacks = attacks



def create_bulbasaur():
    attacks = {
        "Tackle": {"damage": 10, "type": "Normal"},
        "Vine Whip": {"damage": 15, "type": "Grass"},
    }
    bulbasaur = Pokemon("Bulbasaur", "Grass/Poison", 45, 5, attacks, "images/bulbasaur.png")
    return bulbasaur





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))
    pygame.display.flip()