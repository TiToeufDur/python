import pygame

pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mouse Click Detection")

# Object properties
object_color = (255, 0, 0)  # Red
object_rect = pygame.Rect(300, 200, 100, 50)  # x, y, width, height

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position from the event
            mouse_pos = event.pos

            # Check if the mouse position collides with the object's rectangle
            if event.button == 1:
                if object_rect.collidepoint(mouse_pos):
                    print(f"Object clicked at {mouse_pos}")
                    # Add your desired action here, e.g., change color, trigger function

    # Drawing
    screen.fill((255, 255, 255))  # White background
    pygame.draw.rect(screen, object_color, object_rect)  # Draw the object

    pygame.display.flip()

pygame.quit()