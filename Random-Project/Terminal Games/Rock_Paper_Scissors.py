import random
winner = None
score = []
choix = ["roche","papier","ciseaux"]


def Winning(bot,joueur):
    global winner
    if bot == joueur:
        print("Nul !") 
    elif (bot == 0 and joueur == 1) or (bot == 1 and joueur == 2) or (bot == 2 and joueur == 0):
        score.append("joueur")
        print("Point à joueur")
    else:
        score.append("bot")
        print("Point à bot")

    if score.__len__() >=3:
        winner = "bot" if score.count("bot") > score.count("joueur") else "joueur"
    if score.__len__() == 2:    
        print("Point de match!")
    
while True:
    if winner == None:
        try:
            choisi = input("Que choisissez-vous? \n").strip().lower()
            index = choix.index(choisi)
            bot = random.randint(0,2)
            print(f"Le bot prend: {choix[bot]}")
            Winning(bot,index)
        except ValueError:
            print("Choix invalide. Options :", ", ".join(choix))
    else: 
        print(f"{winner} gagne!")
        break