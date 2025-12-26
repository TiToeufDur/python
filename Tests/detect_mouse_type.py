import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mouse Click Detection")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # event.button indicates which button was pressed:
            # 1: Left mouse button
            # 2: Middle mouse button (scroll wheel)
            # 3: Right mouse button
            # 4: Scroll wheel up
            # 5: Scroll wheel down
            if event.button == 1:
                print(f"Left mouse button pressed at {event.pos}")
            elif event.button == 3:
                print(f"Right mouse button pressed at {event.pos}")
            elif event.button == 4:
                print("Mouse wheel scrolled up")
            elif event.button == 5:
                print("Mouse wheel scrolled down")

    screen.fill((0, 0, 0)) # Clear the screen
    pygame.display.flip()

pygame.quit()