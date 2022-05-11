from models import Tournament, Player, Tours, Matchs
from tinydb import TinyDB, Query

db = TinyDB('db.json')
User = Query()


def create_tournat():
    print('tournoir numero 1')
    name = input("Renseigner un nom pour le tournoir")
    place = input("Renseigner un nom pour le lieu")
    date = input("Renseigner un nom pour la date")
    tournament = Tournament(name, place, date)
    print(tournament)


def add_players():
    print('nouveau joueur')
    nom = input("Renseigner votre nom ")
    prenom = input("Renseigner votre prénom ")
    date_de_naissance = input("Renseigner votre date de naissance ")
    sexe = input("Renseigner votre genre")
    classement = input("Renseigner votre classement ")
    players = Player(nom, prenom, date_de_naissance, sexe, classement)
    print(players)




def generate_match():
    print('match fight')



def enter_results():
    print('entrez vos reslt')



def run():

    create_tournat()

    add_players()

    #Répétez les étapes 3 et 4 pour les tours suivants jusqu'à ce que tous les tours soient joués, et que le tournoi soit terminé.
    generate_match()

    enter_results()


if __name__ == "__main__":
    run()
