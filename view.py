from models import Tournament, Player, Tours
import random

players_i = 8

def create_tournat():
    print('tournoir numero 1')
    name = input("Renseigner un nom pour le tournoi")
    place = input("Renseigner un nom pour le lieu")
    date = input("Renseigner un nom pour la date")
    time = input("Renseigner le temps")
    description = input("Renseigner une description")
    round_tourne = input("Renseigner le nombre de rounds de ce tournoi" )
    tournament = Tournament(name, place, date, time, round_tourne, description)




def add_players():
    list_player = []
    print('nouveau joueur')
    nom = input("Renseigner votre nom ")
    prenoms = input("Renseigner votre prénom ")
    date_de_naissance = input("Renseigner votre date de naissance ")
    sexe = input("Renseigner votre genre")
    rank = input("Renseigner votre classement ")
    players = Player(nom, prenoms, date_de_naissance, sexe, rank)

    return players


#def generate_match()
        ##add_players()



def enter_results():
    enter_results_input = input("Entrer vos résultat : ")


def main_menu():
    pass



def run():

    create_tournat()

    add_players()






if __name__ == "__main__":
    run()
