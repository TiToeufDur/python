import pygame
pygame.init()

screen = pygame.display.set_mode((800, 800))


def bon():
    num = {"y":[], "x":[]}
    len_x = line_x.width
    len_y = line_y.height
    jump_x = len_x / 20 
    jump_y = len_y / 20
    for _ in range(20):
        num["x"].append(int(jump_x*_))
        num["y"].append(int(jump_y*_))
  
        if _ != 0: 
            jump_rect_x = pygame.rect.Rect(num["x"][_]+10,screen.get_height()/2 -6,2,14)
            jump_rect_y = pygame.rect.Rect(screen.get_width()/2 - 6,num["y"][_]+10,14,2)
            pygame.draw.rect(screen,"BLACK",jump_rect_x)
            pygame.draw.rect(screen,"BLACK",jump_rect_y)
    
    


        
def diagram_line():
    global line_x,line_y
    line_x = pygame.rect.Rect(10,screen.get_height()/2,screen.get_width()-20,0)
    line_y = pygame.rect.Rect(screen.get_width()/2,10,0,screen.get_height()-20)
    pygame.draw.line(screen,"BLACK",line_x.topleft, line_x.bottomright, 2)
    pygame.draw.line(screen,"BLACK",line_y.topleft, line_y.bottomright, 2)




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("WHITE")
    diagram_line()
    bon()
    
    pygame.display.flip()

pygame.quit()