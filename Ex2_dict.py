# Q1
def obtenir_liste_noms(p_data:list[dict]) -> list[str] :
    """Retourne une liste des noms complets .
    Chaque indexe contient le prénom et nom du client"""
    # créée une liste vide de str
    liste_nomcomplets:list[str]=[]
    # pour chaque valeur dans p_data
    for valeur in p_data:
        nom_client=valeur["nom"]
        prenom_client=valeur["prenom"]
        nom_complet_client=f"{prenom_client} {nom_client}"
        liste_nomcomplets.append(nom_complet_client)
    return liste_nomcomplets
    #       créée 1 str contenant le nom complète du client NOTE : Il est possible que VSCode ne soit pas capable de suggéré les clefs du dict.
    #       ajouté le nouveau nom à la liste de noms
    # retournée la liste de noms

# Q2 : Créez la fonction "obtenir_solde_moyen", qui doit retourner un float.
def obtenir_solde_moyen(p_data:list[dict]) -> float:
            # On peut savoir le nombre de client avec la fonction len()
    nb_clients:int=len(p_data)
    solde_total:int=0
    solde_moyen:float=0
            # Si je veux avoir le solde moyen de tous mes clients, je vais devoir en premier calculer le solde total
    for personne in p_data:
        solde_total+=personne["solde"]
            # Et après, diviser le solde total par le nombre de clients
        solde_moyen=solde_total/nb_clients
    return solde_moyen



# Q3 : Créez la fonction "obtenir_stats".
#   Cette fonction doit retourner 3 valeurs, le total des soldes, la moyenne des soldes, et le nombre de clients
def obtenir_stats(p_data:list[dict]) -> float:
    nb_clients:int=len(p_data)
    solde_total:int=0
    solde_moyen:float=0
    for personne in p_data:
        solde_total+=personne["solde"]
        solde_moyen=solde_total/nb_clients
    return nb_clients,solde_moyen,solde_total








if __name__ == "__main__" :
    # Suite à une requête a notre basse de données, on obtient les données suivantes
    # Il s'agit d'une liste de dictionnaires, chaque dictionnaire correspond à 1 client
    donnees_json:list[dict] =[
                                {"id":0,"prenom":"Hélène","nom":"Boucher","solde":8160},
                                {"id":1,"prenom":"Thérèse","nom":"Tessier","solde":7038},
                                {"id":2,"prenom":"Benjamin","nom":"Savard","solde":3163},
                                {"id":3,"prenom":"Jean","nom":"Tremblay","solde":411},
                                {"id":41,"prenom":"Hugues","nom":"Pelletier","solde":96}
                            ]




    print(f"Q1{80*'_'}")
    # Q1 : On veut écrire un message de bienvenu aux employés 
    # Complètez la fonction "obtenir_liste_employe()"
    # Apellez la fonction, capturez le résultat et l'afficher
    #     Résultat attendu dans le terminal : "Voici la liste des clients: [ Hélène Boucher, Thérèse Tessier, Benjamin Savard, Jean Tremblay, Hugues Pelletier ]"
    liste_nomcomplets=obtenir_liste_noms(donnees_json)
    print(f"Voici la liste des clients: {liste_nomcomplets}")


    print(f"Q2{80*'_'}")
    # Q2: Je veux avoir le solde moyen de mes clients
    # La fonction "obtenir_solde_moyen" n'extiste pas ! C'est à vous de la crée.
    # Vous devez l'appeler et capturer son retour puis imprimer le solde moyen.
    #       Résultat attendu dans le terminal:  "Le solde moyen de mes clients est: 3773.6 $"
    solde_moyen=obtenir_solde_moyen(donnees_json)
    print(f"Le solde moyen de mes clients est: {solde_moyen}")

    print(f"Q3{80*'_'}")
    # Q2 : La fonction précédente était un peu simpliste.
    # Crée la fonction "obtenir_stats" qui doit prendre la liste de dictionnaires en paramètre
    # et doit retourner trois valeurs :
    #   le total des soldes
    #   la moyenne des soldes
    #   le nombre de clients
    # Vous devez l'appeler et capturer son retour puis l'imprimer
    #       Résultat attendu dans le terminal:  "Total : 18868 $, moy : 3773.6 $, nombre de clients : 5"
solde_total=obtenir_stats(donnees_json)
print(f"Total: {solde_total[2]}, moyenne: {solde_total[1]}, nombre de clients: {solde_total[0]}")