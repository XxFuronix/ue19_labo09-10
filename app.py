# Importation du module
import requests


def get_free_game():
    url = "https://www.freetogame.com/api/games?platform=pc"

    try:
        reponse = requests.get(url)
        # Vérifie si la requête a réussi
        reponse.raise_for_status()
        donnee = reponse.json()

        if donnee and 'games' in donnee:
            # Récupère le nom du premier jeu gratuit de la liste
            first_game = donnee['games'][0]['title']
            return first_game
        else:
            return "Aucun jeu gratuit n'a été trouvé"

    except requests.exceptions.RequestException as i:
        return f"Erreur : {i}"


if __name__ == "__main__":
    free_game = get_free_game()
    # Affiche le(s) jeu(x) gratuit(s)
    print(f"Voici le(s) jeu(x) actuellement gratuit(s) : {free_game}")
