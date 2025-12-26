import pygame
import random

class MyClone(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = random.randint(1, 5) # Example: add some random movement

    def update(self):
        # Example: make clones move downwards
        self.rect.y += self.speed
        if self.rect.top > pygame.display.get_surface().get_height():
            self.kill() # Remove clone if it goes off-screen

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Clones")

# Create a sprite group to hold all clones
all_clones = pygame.sprite.Group()

# Example: Create 5 clones at different random positions
for _ in range(5):
    x = random.randint(50, screen_width - 50)
    y = random.randint(50, screen_height - 50)
    clone = MyClone("images/O.png", x, y) # Replace "your_image.png"
    all_clones.add(clone)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw all clones
    all_clones.update()
    screen.fill("WHITE") # Clear screen
    all_clones.draw(screen)
    pygame.display.flip()

pygame.quit()