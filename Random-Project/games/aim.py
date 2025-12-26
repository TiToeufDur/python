import pygame 
import tkinter
import random
pygame.init

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
screen = pygame.display.set_mode((width,height))
ball_image = pygame.image.load("images/ball.png")
balls = pygame.sprite.Group()


class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = ball_image
        self.rect = self.image.get_rect(center=(x,y))

    def update(self):
        if self.rect.collidepoint(mouse_pos):
            self.kill()

for _ in range(2):
    balls.add(Ball(random.randint(0,width),random.randint(0,height)))

playing = True
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if event.button == 1:
                balls.update()
                
                    
    screen.fill("BLACK")
    balls.draw(screen)
    pygame.display.flip()