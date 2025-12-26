
import pygame
pygame.init()

img_X = pygame.image.load("images/X.PNG")
img_O = pygame.image.load("images/O.png")
screen_width = 900
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont(None, 20)
clock = pygame.time.Clock()
balls = pygame.sprite.Group() # Sprite Group to store all balls
dropper_x = screen_width / 2
dodger_x = screen_width / 2
dodger_life = 10 
last_shot_time = 0
shot_cooldown = 600
winner = None
winning_time = 30000

#  CLONE CLASS
class Ball(pygame.sprite.Sprite):
    def __init__(self, x):
        super().__init__()
        self.image = img_O
        self.rect = self.image.get_rect(center=(x, 50))  # start at dropper height
        self.speed = 4  # falling speed

    def update(self):
        global dodger_life
        self.rect.y += self.speed
        if self.rect.top > screen_height:
            self.kill()  # remove ball, but don't hurt dodger
        elif self.rect.colliderect(dodger_rect):
            self.kill()
            dodger_life = max(0, dodger_life - 1)  # only reduce health if it actually hits
            
#  DROPPER MOVEMENT
def Dropper():
    global dropper_x
    speed = 4
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        dropper_x += speed
    if key[pygame.K_a]:
        dropper_x -= speed
    # keep dropper on screen
    dropper_x = max(0, min(dropper_x, screen_width - img_X.get_width()))
    screen.blit(img_X, (dropper_x, 30))

# DODGER MOVEMENT
def Dodger():
    global dodger_x , dodger_rect
    speed = 3
    dodger_rect = img_X.get_rect(topleft=(dodger_x, 420))
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]:
        dodger_x += speed
    if key[pygame.K_LEFT]:
        dodger_x -= speed
    dodger_x = max(0, min(dodger_x, screen_width - img_X.get_width()))
    screen.blit(img_X,(dodger_x,400))

#  TEXT DISPLAY
def Text_display():
    global winner
    fps_text = font.render(f"{round(clock.get_fps(), 2)}", True, "BLACK")
    dodger_life_text = font.render(f"{dodger_life}", True , "GREEN" if dodger_life >= 7 else "ORANGE" if dodger_life > 3 and dodger_life <=6 else "RED" )
    winner_text = pygame.font.Font(None,60).render(f"{winner} wins!" , True , "BLACK")

    screen.blit(fps_text, (10, 10))
    screen.blit(dodger_life_text, (dodger_x, dodger_rect.y-2))

    if dodger_life <= 0:
        winner = "Dropper"
        screen.blit(winner_text,(screen_width/2-winner_text.get_width()/2,screen_height/2-winner_text.get_height()/2))

    elif current_time >= winning_time :
        winner = "Dodger"
        screen.blit(winner_text,(screen_width/2-winner_text.get_width()/2,screen_height/2-winner_text.get_height()/2))

    elif winner == None:
        temp_text = pygame.font.Font(None,30).render(f"{round(winning_time / 1000 - current_time / 1000)}",True,"BLACK")
        screen.blit(temp_text,(screen_width / 2 - temp_text.get_width()/2, 20))
    else: 
        winner = None

#  MAIN LOOP
playing = True
while playing:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False 
        # SPACE create a new falling ball
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if current_time - last_shot_time > shot_cooldown:
                last_shot_time = current_time
                balls.add(Ball(dropper_x))

    screen.fill("WHITE")
    Dropper()
    Dodger()
    balls.update()
    balls.draw(screen)
    Text_display()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
