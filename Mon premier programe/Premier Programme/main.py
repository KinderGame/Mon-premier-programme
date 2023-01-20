nom = input("Quel est votre nom ? ")


age = 0
while age == 0:
    age_str = input("Quel est votre age ? ")
    try:
        age = int(age_str)
    except:
        print("ERREUR: Vous devez renter un nombre pour l'age")

# print("fin de la boucle")
        
print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans")
print("L'an prochain vous aurez " + str(age+1) + " ans")


"""
    while (age n'est pas correct)
        demander l'age

    afficher la suite
"""
