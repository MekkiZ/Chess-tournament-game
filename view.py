"""system module."""
import logging
import random
import datetime

from models import Tournament, Player


def main_interface():
    """
    Create main interface for user with input function.

    The administrator can create tournant or modify players rank.

    :return: multiple variable for controllers part
            1 : option for creat tournant
            2 : option to modify player rank
            3 : commande for exit the game
            4 : return data for traitement
    """
    print("=========================")
    print("Sélectionner votre choix: ")
    print("1. Créer un tournoi")
    print("2. Modifier le rang d'un joueur")
    print("3. Rependre un tournoi ")
    print("4. Quitter le jeu ")
    print("=========================")
    choix_option = input("S'il vous plait faite un choix >>  ")
    return choix_option


def create_tournant():
    """
    User create tournante and Models instance for the database (tinydb).

    :return : Instance for serialized_tournant in controller part.
    """
    logging.info("tournoi numéro 1")
    name = str(input("Renseigner un nom pour le tournoi: "))
    place = input("Renseigner un nom pour le lieu: ")

    # condition for verify date has true.
    date = input("entrer la date sous le format 'dd/mm/yy' : ")
    day, month, year = date.split("/")
    is_validate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        is_validate = False
    if is_validate:
        pass
    else:
        logging.info("la saisie n'est pas valide")
        return create_tournant()

    time = input(
        "Renseigner le contrôle du temps ( bullet, blitz ou un coup rapide ) : "
    )
    description = input("Renseigner une description: ")
    round_tourne = input("Renseigner le chiffre rounds: ")
    status = input("Renseignez le status du tournoi ( 'debut' ou 'fin': ) ")

    # instance for model ddb
    tournament = Tournament(name, place, date, time, round_tourne, description, status)

    return tournament


def add_players():
    """
    User create players profil for tournant create previously.

    He or she has to enter information about players.

    :return: instance for serialized_player for tinyDB.
    """
    print("nouveau joueur")
    nom = str(input("Renseigner votre nom "))
    date_b = input("entrer votre date de naissance 'dd/mm/yy' : ")
    jour, mois, ans = date_b.split("/")
    is_validate = True
    try:
        datetime.datetime(int(ans), int(mois), int(jour))
    except ValueError:
        is_validate = False
    if is_validate:
        pass
    else:
        logging.info("la saisie n'est pas valide")
        return add_players()
    sexe = str(input("Renseigner votre genre ( H ou F ):"))
    if nom and date_b and sexe:
        try:
            rank = int(input("Renseigner votre classement "))
            score = int(input("Renseigner le score de commencement "))
            players = Player(nom, date_b, sexe, rank, score)
            return players
        except ValueError:
            logging.info(
                "veuillez renseigner le classement et le score de commencement en chiffre "
            )

    return None


def round_player(player_1, player_2):
    """
    Function has for purpose to creat round player and show on terminal.

    :return: Data for controllers part to treat update point and matchs pair .
    """
    color = ["blanc", "noire"]
    color_reverse = ["noir", "blanc"]
    score = input(
        f"{player_1}  {random.choice(color)} vs {player_2} {random.choice(color_reverse)}"
        f" tape le chiffre correspond du vainqueur ou de l'égalité? \n "
        f"1-{player_1} \n 2 - {player_2}  \n"
        f" 3 égalité  \n"
    )

    return score


def date_begin_and_end():
    """Function to creat date for match"""
    date_begin = input(
        " entrer le debut du round en renseignement "
        " la date(XX/XX/XX) : "
    )
    date_end = input(
        " entrer la fin du round en renseignement "
        " la date( XX/XX/XX) : "
    )

    return date_begin, date_end
