from models import Tournament, Player, Round

import datetime

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
    round_tourne = input("Renseigner le chiffre rounds")
    tournament = Tournament(name, place, date, time, round_tourne, description)

    return tournament


def add_players():
    print('nouveau joueur')
    name = input("Renseigner votre nom ")
    date_de_naissance = input("Renseigner votre date de naissance ")
    sexe = input("Renseigner votre genre")
    rank = int(input("Renseigner votre classement "))
    score = int(input("Renseigner le score de commencement "))
    players = Player(name, date_de_naissance, sexe, rank, score)

    return players


def enter_results():
    enter_results_input = input("Entrer vos résultat : ")
    return enter_results_input


def round_player(player_1, player_2):
    round_number = input("renseigner le numero du tours joué : ")
    date_begin = input(" entrer le debut du round en renseignement l'heure et la date( xx:xx XX/XX/XX) : ")
    date_end = input(" entrer la fin du round en renseignement l'heure et la date( xx:xx XX/XX/XX) : ")
    score = input(player_1 + " vs " + player_2 + "  tape le chiffre correspond du vainqueur ou de l'égalité? \n 1-" +
                  player_1 + "\n 2 - " + player_2 + " \n 3 - egalité  \n")

    return score

