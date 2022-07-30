from models import Tournament, Player, Round
import random, datetime

nombre_tour = 4

def create_tournant():

    print('tournoir numero 1')
    name = str(input("Renseigner un nom pour le tournoi "))
    place = input("Renseigner un nom pour le lieu ")
    date = input("entrer la date sous le format 'dd/mm/yy' : ")
    day, month, year = date.split('/')
    is_validate = True

    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_validate = False

    if (is_validate):
        pass
    else:
        print("Input date is not valid..")

    time = input("Renseigner le temps ")
    description = input("Renseigner une description ")
    round_tourne = input("Renseigner le chiffre rounds" )
    tournament = Tournament(name, place, date, time, round_tourne, description)

    return tournament



def add_players():
    print('nouveau joueur')
    name = input("Renseigner votre nom ")
    date_de_naissance = input("Renseigner votre date de naissance ")
    sexe = input("Renseigner votre genre")
    rank = input("Renseigner votre classement ")
    players = Player(name, date_de_naissance, sexe, rank)


    return players



def generate_match():
    """
    algo suisse
    """




def enter_results():

    enter_results_input = input("Entrer vos résultat : ")


def main_menu():
    pass



def run():

    create_tournant()
    add_players()






if __name__ == "__main__":
    run()
