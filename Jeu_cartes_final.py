import time
import random

#RANDOM LISTS
deckuser = [1, 2, 3, 4, 5, 6, 7, 8, 9]
deckpcu = [1, 2, 3, 4, 5, 6, 7, 8, 9]


#VALUES
user = 0
pcu = 0

#MES DEFS

def tour():
    
    global deck_usercalcul
    global deck_pcucalcul
    global pcu
    global user
    
    if user == 4:
        print()
        time.sleep(1)
        uservictoire()
    if pcu == 4:
        print()
        time.sleep(1)
        pcuvictoire()
    if deck_usercalcul > deck_pcucalcul:
        victoireusertour()
    if deck_usercalcul < deck_pcucalcul:
        pcuvictoiretour()
    if deck_usercalcul == deck_pcucalcul:
        print()
        egal()
    else:
        print()

# victoire final USER      
def uservictoire():
    
    global deck_usercalcul
    global deck_pcucalcul
    global pcu
    global user
    
    print('Vous avez remporter la partie !')
    time.sleep(3)
    quit()

# égalité
def egal():
    
    global deck_usercalcul
    global deck_pcucalcul
    global pcu
    global user
    
    print('Égalité sur ce tour !')
    
#victoire final PCU
def pcuvictoire():
    
    global deck_usercalcul
    global deck_pcucalcul
    global pcu
    global user
    
    print('Votre adversaire remporte la partie !')
    time.sleep(3)
    quit()

# PCU victoire tour
def pcuvictoiretour():
    
    global deck_usercalcul
    global deck_pcucalcul
    global pcu
    global user
    
    print('Votre Adversaire remporte ce tour')
    pcu = pcu + 1
    print()
    time.sleep(1)

# USER victoire tour    
def victoireusertour():
    
    global deck_usercalcul
    global deck_pcucalcul
    global pcu
    global user
    
    print('Vous avez remporté ce tour')
    user = user + 1
    print()
    time.sleep(1)
    
# Victorycheck ( apres avoir accorder 1 point)
def victorycheck():
    
    global deck_usercalcul
    global deck_pcucalcul
    global pcu
    global user
    
    if user == 4:
        print()
        time.sleep(1)
        uservictoire()
    if pcu == 4:
        print()
        time.sleep(1)
        pcuvictoire()
    else :
        print()
    
    

    
#déroulement 
print()
print()
print('Bienvenue dans SUPER BATAILLE')
print()
time.sleep(2)
print('tirez 4 cartes contre un adversaire, le plus haut chiffre gagne. Il faut 4 victoires pour remporter le jeu')
print()
a1 = input('Appuyez ENTER pour commencer :  ') 
print()
time.sleep(2)
deck_usercalcul = random.choice(deckuser)
deck_pcucalcul = random.choice(deckuser)

print()
print()
print('                     Votre score                      Votre adversaire              ')
print('                                                                                    ')
print('                       0000000                             0000000                  ')
print("                       0     0                             0     0                  ")
print('                       0 ', deck_usercalcul, ' 0                             0 ', deck_pcucalcul,' 0                ')
print("                       0     0                             0     0                  ")
print('                       0000000                             0000000                  ')
print()
print()


time.sleep(2)

tour()

a1 =input('Appuyez sur ENTER pour le deuxième tour : ')
print()
deck_usercalcul = random.choice(deckuser)
deck_pcucalcul = random.choice(deckuser)

print()
print()
print('                     Votre score                      Votre adversaire              ')
print('                                                                                    ')
print('                       0000000                             0000000                  ')
print("                       0     0                             0     0                  ")
print('                       0 ', deck_usercalcul, ' 0                             0 ', deck_pcucalcul,' 0                ')
print("                       0     0                             0     0                  ")
print('                       0000000                             0000000                  ')
print()
print()

time.sleep(2)

tour()
victorycheck()

a1 =input('Appuyez sur ENTER pour le troisième tour : ')
print()
deck_usercalcul = random.choice(deckuser)
deck_pcucalcul = random.choice(deckuser)

print()
print()
print('                     Votre score                      Votre adversaire              ')
print('                                                                                    ')
print('                       0000000                             0000000                  ')
print("                       0     0                             0     0                  ")
print('                       0 ', deck_usercalcul, ' 0                             0 ', deck_pcucalcul,' 0                ')
print("                       0     0                             0     0                  ")
print('                       0000000                             0000000                  ')
print()
print()

time.sleep(2)

tour()
victorycheck()

a1 =input('Appuyez sur ENTER pour le quatrième tour : ')
print()
deck_usercalcul = random.choice(deckuser)
deck_pcucalcul = random.choice(deckuser)

print()
print()
print('                     Votre score                      Votre adversaire              ')
print('                                                                                    ')
print('                       0000000                             0000000                  ')
print("                       0     0                             0     0                  ")
print('                       0 ', deck_usercalcul, ' 0                             0 ', deck_pcucalcul,' 0                ')
print("                       0     0                             0     0                  ")
print('                       0000000                             0000000                  ')
print()
print()

time.sleep(2)

tour()
victorycheck()

a1 =input('Appuyez sur ENTER pour le cinquième tour : ')
print()
deck_usercalcul = random.choice(deckuser)
deck_pcucalcul = random.choice(deckuser)

print()
print()
print('                     Votre score                      Votre adversaire              ')
print('                                                                                    ')
print('                       0000000                             0000000                  ')
print("                       0     0                             0     0                  ")
print('                       0 ', deck_usercalcul, ' 0                             0 ', deck_pcucalcul,' 0                ')
print("                       0     0                             0     0                  ")
print('                       0000000                             0000000                  ')
print()
print()

time.sleep(2)

tour()
victorycheck()

a1 =input('Appuyez sur ENTER pour le sixième tour : ')
print()
deck_usercalcul = random.choice(deckuser)
deck_pcucalcul = random.choice(deckuser)

print()
print()
print('                     Votre score                      Votre adversaire              ')
print('                                                                                    ')
print('                       0000000                             0000000                  ')
print("                       0     0                             0     0                  ")
print('                       0 ', deck_usercalcul, ' 0                             0 ', deck_pcucalcul,' 0                ')
print("                       0     0                             0     0                  ")
print('                       0000000                             0000000                  ')
print()
print()

time.sleep(2)

tour()
victorycheck()

a1 =input('Appuyez sur ENTER pour le septième tour : ')
print()
deck_usercalcul = random.choice(deckuser)
deck_pcucalcul = random.choice(deckuser)

print()
print()
print('                     Votre score                      Votre adversaire              ')
print('                                                                                    ')
print('                       0000000                             0000000                  ')
print("                       0     0                             0     0                  ")
print('                       0 ', deck_usercalcul, ' 0                             0 ', deck_pcucalcul,' 0                ')
print("                       0     0                             0     0                  ")
print('                       0000000                             0000000                  ')
print()
print()

time.sleep(2)

tour()
victorycheck()

a1 =input('Appuyez sur ENTER pour le huitième our : ')
print()
deck_usercalcul = random.choice(deckuser)
deck_pcucalcul = random.choice(deckuser)

print()
print()
print('                     Votre score                      Votre adversaire              ')
print('                                                                                    ')
print('                       0000000                             0000000                  ')
print("                       0     0                             0     0                  ")
print('                       0 ', deck_usercalcul, ' 0                             0 ', deck_pcucalcul,' 0                ')
print("                       0     0                             0     0                  ")
print('                       0000000                             0000000                  ')
print()
print()

time.sleep(2)

tour()
victorycheck()

a1 =input('Appuyez sur ENTER pour le neuvième our : ')
print()
deck_usercalcul = random.choice(deckuser)
deck_pcucalcul = random.choice(deckuser)

print()
print()
print('                     Votre score                      Votre adversaire              ')
print('                                                                                    ')
print('                       0000000                             0000000                  ')
print("                       0     0                             0     0                  ")
print('                       0 ', deck_usercalcul, ' 0                             0 ', deck_pcucalcul,' 0                ')
print("                       0     0                             0     0                  ")
print('                       0000000                             0000000                  ')
print()
print()

time.sleep(2)

tour()
victorycheck()
       
    
    