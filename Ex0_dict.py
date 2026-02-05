# Les dictionnaires permettent d'associer des valeurs à des données-clés
# L'équivalent des HashMap ou Associative Arrays dans d'autres languages

# Nous avons ici un dictionnaire qui contient des données sur un étudiant
etudiant:dict = {'nom': 'Vincent', 'age':18, 'cours': ['Reseau 1', 'Prog 2 en Python']}
print(f"Le dictionnaire étudiant est au départ: {etudiant}")


# C'est vraiment comme un dictionnaire dans la vraie vie
# Les clés nous permettent de rechercher une valeur


print(f"Q1{80*'_'}")
# Q1:  on veut savoir la valeur du nom de l'étudiant en utilisant les f string
#      Dans le terminal, on aura: "Le nom de l'étudiant est : Vincent"  
nom_etudiant:str=etudiant['nom']
print(f"Le nom de l'étudiant est: {nom_etudiant}")



print(f"Q2{80*'_'}")
# Q2: Ajoutez une nouvelle paire clé:valeur dans notre dictionnaire
#  Ajoutez le courriel comme clé et '2112344@cegepmontpetit.ca'
#  Dans le terminal on veut avoir: Voici le courriel de l'étudiant : 2112344@cegepmontpetit.ca
etudiant["courriel"]="2112344@cegepmontpetit.ca"
print(f"Voici le courriel de l'étudiant: {etudiant['courriel']}")






print(f"Q3{80*'_'}")
# Q3: Changez la valeur du courriel de l'étudiant
# la nouvelle valeur '2000000@cegepmontpetit.ca'
#  Dans le terminal on veut avoir: Voici le nouveau courriel de l'étudiant: 2000000@cegepmontpetit.ca
etudiant['courriel']="2000000@cegepmontpetit.ca"
print(f"Voici le nouveau courriel de l'étudiant: {etudiant['courriel']}")














print(f"Q5{80*'_'}")
# Utilisez la méthode pop qui en plus d'enlever la clé, vous retourne la valeur qu'on enlève
# Q5: Enlevez la clé 'age' de l'étudiant, mais imprimez la valeur qu'elle avait
#      Dans le terminal on veut: On a enlevé l'âge de l'étudiant, sa valeur était: 17
valeur_enlevée:int=etudiant.pop('age')
print(f"On a enlevé l'âge de l'étudiant, sa valeur était: {valeur_enlevée}")





print(f"Q6{80*'_'}")
# On peut obtenir le nombre de paires clés:valeurs dans notre dictionnaire avec la méthode len
# Q6: Combient de paires clés:valeurs avons-nous maintenant dans notre dictionnaire?
#      Dans le terminal: Nous avons maintenant X paires clés valeurs.
nb_paires=len(etudiant)
print(f"Nous avons maintenant {nb_paires} paires clés valeurs")
