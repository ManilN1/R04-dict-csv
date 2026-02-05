import os
os.chdir(os.path.dirname(__file__)) # cette ligne change le répertoire courant pour qu'il devienne celui où ce trouve le fichier actuel.

# Q1  Imprimez le répertoire courant
print(f"Q1{'_'*60}")
repertoire_courant=os.getcwd()
print(repertoire_courant)


# Q2   Imprimez la variable d'environnement USERPROFILE (utilisez la méthode .get() de l'objet os.environ)
print(f"Q2{'_'*60}")
info_user=os.environ
username:str=info_user.get("USERPROFILE")
print(username)

# Q3 Déplacez-vous sur le répertoire 'Documents' et imprimez le répertoire courant
#       Attention : n'utilisez pas un chemin relatif.
print(f"Q3{'_'*60}")
repertoire=username +'\\Documents'
os.chdir(repertoire)
repertoire_changé=os.getcwd()
print(repertoire_changé)

    # NOTE : On ne peut pas écrire c:\\Users\\..... parce que ca ne fonctionnerait pas sur votre ordinateur à la maison

# Q4   Imprimez la liste des répertoires et des fichiers qu'il y a dans 'Document'
print(f"Q4{'_'*60}")
liste=os.listdir(repertoire)
print(liste)

# Q5   Créez un répertoire OS-ExercQ5
#       Réimprimez les répertoires et les fichiers dans 'Document'
print(f"Q5{'_'*60}")
os.makedirs(f"{repertoire}\\OS-ExercQ5")
liste=os.listdir(repertoire)
print(liste)

# Q6   Créez les répertoires OS-ExercQ6/Subdir1 avec une seule instruction
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
print(f"Q6{'_'*60}")
os.makedirs(f"{repertoire}\\OS-ExercQ6\\Subdir1")
liste=os.listdir(repertoire)
print(liste)



#Q7   Renommez le répertoire Subdir1 pour qu'il s'appelle Sous_repertoire
print(f"Q6{'_'*60}")
os.rename(f"{repertoire}\\OS-ExercQ6\\Subdir1",f"{repertoire}\\OS-ExercQ6\\Sous_repertoire")
# Q8   suppression du répertoire OS-ExercQ6 et de son contenu
os.rmdir(f"{repertoire}\\OS-ExercQ6\\Sous_repertoire")
os.rmdir(f"{repertoire}\\OS-ExercQ6") 
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
print(f"Q6{'_'*60}")
liste=os.listdir(repertoire)
print(liste)



