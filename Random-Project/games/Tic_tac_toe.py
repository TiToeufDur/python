import pygame
from sys import exit
import os

pygame.init()
pygame.display.set_caption("Tic-Tac-Toe")
screen = pygame.display.set_mode((300, 400))
Title_text = pygame.font.Font(None, 50).render("Tic Tac Toe", True, "BLACK")
recommencer_text = pygame.font.Font(None, 20).render("Recommencer", True, "BLACK")
recommencer_hitbox = pygame.Rect(0, 380, 93, 20)
image_x = pygame.image.load("images/X.PNG")
image_o = pygame.image.load("images/O.png")
touched = {1: [], 2: []}
win = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7],
]
winner = None


class Cell:
    def __init__(self, col, row, x, y, size=70):
        self.col = col
        self.row = row
        self.rect = pygame.Rect(x, y, size, size)
        self.colour = "WHITE"
        self.symbol = None

    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect)
        if self.symbol == "x":
            screen.blit(image_x, self.rect)
        elif self.symbol == "o":
            screen.blit(image_o, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def toching(self):
        return self.col * 3 + self.row + 1


class Turn:
    def __init__(self, turn):
        self.turn = turn

    def is_turn_valid(self, turn_oposite):
        for _ in touched[self.turn]:
            if _ in touched[turn_oposite]:
                print(f"{_}: Invalid(played)")
                touched[self.turn].pop()
                return False
            else:
                print(f"inspecter:{_}")
        return "Valide"

    def turn_oposite_turn(self):
        oposite_turn = self.turn + 1
        if oposite_turn > 2:
            oposite_turn = 1
        return oposite_turn

    def turn_counter(self):
        self.turn += 1
        if self.turn > 2:
            self.turn = 1
        return self.turn


def draw_lines():
    global ligne_1, ligne_2, ligne_3, ligne_4
    ligne_1 = pygame.Rect(97.5, 100, 5, 210)
    ligne_2 = pygame.Rect(167.5, 100, 5, 210)
    ligne_3 = pygame.Rect(30, 167.5, 210, 5)
    ligne_4 = pygame.Rect(30, 237.5, 210, 5)
    pygame.draw.rect(screen, "BLACK", ligne_1)
    pygame.draw.rect(screen, "BLACK", ligne_2)
    pygame.draw.rect(screen, "BLACK", ligne_3)
    pygame.draw.rect(screen, "BLACK", ligne_4)


def hitboxes(coord):
    cells = []
    coordonates = []
    for row in range(3):
        for col in range(3):
            x = 30 + col * 70
            y = 100 + row * 70
            coordonates.append((row, col))
            cells.append(Cell(row, col, x, y))
    if not coord:
        return cells
    return coordonates


def clear_terminal():
    # Check the operating system to use the correct command
    if os.name == "nt":  # For Windows
        os.system("cls")
    else:  # For macOS and Linux
        os.system("clear")


cells = hitboxes(False)
coordonates = hitboxes(True)
turn = Turn(1)
turn_text = Turn(0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            clear_terminal()
            pos = event.pos
            if winner == None:
                for cell in cells:
                    if cell.is_clicked(pos):
                        # print(f"Click sur col={Cell.col}, row={Cell.row}")
                        toching = cell.toching()
                        print(f"player{turn.turn}'s turn")
                        print(f"toching: {toching}")
                        # Vérifie si la case a déjà été jouée par ce joueur
                        if toching in touched[turn.turn]:
                            print(f"{touched[turn.turn]}:Invalid(exists)")
                        else:
                            touched[turn.turn].append(
                                toching
                            )  # Ajoute à la bonne liste selon le joueur courant
                            turn_oposite = (
                                turn.turn_oposite_turn()
                            )  # configure la variabe avec la classe
                            is_valid = turn.is_turn_valid(
                                turn_oposite
                            )  # vérifie si le tour est valable en regardant si il existe deja dans les variables qui enregistre les tour passé
                            print(is_valid)
                            if is_valid:
                                print(f"joueur1:{touched[1]}  joueur2:{touched[2]}")
                                cell.symbol = "x" if turn.turn == 1 else "o"
                                for combo in win:
                                    if all(c in touched[turn.turn] for c in combo):
                                        winner = "x" if turn.turn == 1 else "o"
                                        winner_text = pygame.font.Font(None, 30).render(
                                            f"{winner} wins!", True, "BLACK"
                                        )
                                turn_value = (
                                    turn.turn_counter()
                                )  # Incrémente le tour après avoir ajouté
                            # Check for tie (if all 9 cells are played and no winner)
                            if winner is None and len(touched[1]) + len(touched[2]) == 9:
                                winner = "tie"
                                winner_text = pygame.font.Font(None, 30).render(
                                    "Match nul!", True, "BLACK"
                                )

            else:
                if recommencer_hitbox.collidepoint(pos) == True:
                    winner = None
                    touched[1].clear()
                    touched[2].clear()
                    for cell in cells:
                        cell.symbol = None
                        cell.colour = "WHITE"
                    turn.turn = 1

    screen.fill("WHITE")
    screen.blit(Title_text, (screen.get_width() / 2 - Title_text.get_width() / 2, 20))
    if winner != None or winner == "tie":
        pygame.draw.rect(screen, "White", recommencer_hitbox)
        screen.blit(winner_text, (0, 0))
        screen.blit(
            recommencer_text, (0, screen.get_height() - recommencer_text.get_height())
        )

    for Cell in cells:
        Cell.draw(screen)
    draw_lines()
    pygame.display.update()
