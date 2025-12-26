import pygame
from sys import exit
import os

# Initialisation de Pygame
pygame.init()
t = [""] * 9
tour = True
winner = "VIRGIN"

screen_width, screen_height = 300, 300
screen = pygame.display.set_mode((screen_width, screen_height))
cell_size = 100
board_rect = pygame.Rect(0, 0, cell_size * 3, cell_size * 3)


def initGame():
    global t, tour, winner, screen#
    t = [""] * 9
    tour = True
    winner = None
    screen.fill("WHITE")
    pygame.display.update()

def CheckWinner(t):
    # X même et les trois Y
    for x in range(3):
        if t[x * 3] == t[x * 3 + 1] == t[x * 3 + 2] != "":
            return t[x * 3]
    
    # Y meme et les trois X
    for y in range(3):
        if t[y] == t[y + 3] == t[y + 6] != "":
            return t[y]

    # X == Y pour les trois valeurs
    if t[0] == t[4] == t[8] != "":
        return t[0]
    
    # X + Y == 2 pour les trois valeurs de X
    if t[2] == t[4] == t[6] != "":
        return t[2]
    
    for i in range(9):
        if t[i] == "":
            return None  # Le jeu continue

    # Pas de Gagnant
    return "Draw"

def processEvents(Events): 
    global tour
    for event in Events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Si OUI, Mettre à jour le tableau
            pos = event.pos
            if board_rect.collidepoint(pos):
                col = pos[0] // cell_size
                row = pos[1] // cell_size
                index = row * 3 + col
                if t[index] == "":
                    # Le coup est valide
                    if tour:
                        t[index] = "X"
                    else:
                        t[index] = "O"
                    # Au prochain de jouer
                    tour = not tour

def drawBoard():
    pygame.draw.rect(screen, "WHITE", board_rect)
    # Dessiner les lignes
    pygame.draw.line(screen, "BLACK", (board_rect.left + cell_size, board_rect.top), (board_rect.left + cell_size, board_rect.bottom), 5)
    pygame.draw.line(screen, "BLACK", (board_rect.left + 2 * cell_size, board_rect.top), (board_rect.left + 2 * cell_size, board_rect.bottom), 5)
    pygame.draw.line(screen, "BLACK", (board_rect.left, board_rect.top + cell_size), (board_rect.right, board_rect.top + cell_size), 5)
    pygame.draw.line(screen, "BLACK", (board_rect.left, board_rect.top + 2 * cell_size), (board_rect.right, board_rect.top + 2 * cell_size), 5)
    # Dessiner le contenu des cases
    for i in range(9):
        x = (i % 3) * cell_size
        y = (i // 3) * cell_size
        if t[i] == "X":
            drawCell(x, y, "X")
        elif t[i] == "O":
            drawCell(x, y, "O")

    pygame.display.update()

def drawCell(x, y, symbol):
    font = pygame.font.Font(None, 100)
    text = font.render(symbol, True, "BLACK")
    text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
    screen.blit(text, text_rect)

while True:
    # ENTRÉES (Input)
    # Est-ce qu'une HitBox a été touchée ?
    processEvents(pygame.event.get())

    #if winner == None:
        # Vérifier l'état du jeu
    winner = CheckWinner(t)
    if winner != None:
        print(f"Gagnant: {winner} \x07")

    # Afficher le Tableau    
    drawBoard()

