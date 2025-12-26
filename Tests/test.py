import pygame

pygame.init
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("First")







running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    screen.fill("WHITE")
    pygame.display.flip()
pygame.quit