# debut de la partie
import random

nom_joueur_1 = input("Joueur 1 : ")
nom_joueur_2 = input("Joueur 2 : ")
print("Bienvenue dans la faille de l'invocateur ! ")
print("C'est à toi", nom_joueur_1)

print("Lancer de 5 dés :")
i = 0
de = 0
score1 = 0
score_total_1 = 0
score_total_2 = 0
score_final = 0
score_final_2 = 0  #

while i < 5:
    de = random.randint(1, 6)
    i = i + 1
    if de == 1:
        score1 = score1 + 100
    elif de == 5:
        score1 = score1 + 50
    print(de)
score_total_1 = score_total_1 + score1
print(score_total_1, "pts,score du tour", score_total_1, 'pts')

score1 = 0
i = 0
reponse = input("relancer 3 dés ?")
if reponse == "oui":
    while i < 3:
        de = random.randint(1, 6)
        i = i + 1
        if de == 1:
            score1 = score1 + 100
        elif de == 5:
            score1 = score1 + 50
        print(de)
score_total_2 = + score_total_2 + score1
if score_total_2 == 0:
    print("0 pts, tour perdu.")
else:
    score_final = score_total_1 + score_total_2
    print(score_final, "pts en totalité.")

print(nom_joueur_1, "marque", score_final, "pts")

print("Score :", nom_joueur_1, "=", score_final, nom_joueur_2, "= 0")

print("A ton tour", nom_joueur_2, ".")

i = 0

while i < 5:
    de = random.randint(1, 6)
    i = i + 1
    if de == 1:
        score1 = score1 + 100
    elif de == 5:
        score1 = score1 + 50
    print(de)
score_total_1 = score_total_1 + score1
print(score_total_1, "pts,score du tour", score_total_1, 'pts')

score1 = 0
i = 0

reponse = input("relancer 3 dés ?")
if reponse == "oui":
    while i < 3:
        de = random.randint(1, 6)
        i = i + 1
        if de == 1:
            score1 = score1 + 100
        elif de == 5:
            score1 = score1 + 50
        print(de)
score_total_2 = + score_total_2 + score1
if score_total_2 == 0:
    print("0 pts, tour perdu. ")
else:
    score_final_2 = score_total_1 + score_total_2
    print(score_final_2, "pts en totalité.")

print(nom_joueur_2, "marque", score_final, "pts")

print("Score :", nom_joueur_1, "=", score_final, nom_joueur_2, "=", score_final_2)
