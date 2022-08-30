"""system module."""

import sys
import logging
from operator import itemgetter
from tinydb import TinyDB, Query
from view import add_players, create_tournant, round_player, main_interface, date_begin_and_end
from models import Round

# We’ll start by setting up a TinyDB database.
db = TinyDB("db.json")
user = Query()

# Variable global immutable.
nb_players = 2
nb_player_for_swiss = int(nb_players / 2)
nombre_tour = 4


class Controller:
    """Controller Part : data traitement from view and Models."""

    def __init__(self):
        """Global variables."""
        # models
        self.rank_save_for_replace = ""
        self.name_player_switch_rank = ""
        self.point = float(1)
        self.tournant_data = []
        self.data_rank_players = []
        self.tournant_save_data = []
        self.table_save_players = []
        self.players_information = []
        self.tours = []
        self.match = []
        self.tournoi_table = db.table("tournoi")
        self.players_table = db.table("players")
        self.table_round = db.table("round")

    def interface_main_manu(self):
        """
        Function to verify response from user ( View ).

        We confirm 3 choices: 1 - creat_tournant
                              2 - change rank players
                              3 - shutdown the program.
        """
        choix_option = main_interface()
        if choix_option == "1":
            self.add_player()
        elif choix_option == "2":
            self.admin_power_change_rank()
        elif choix_option == "3":
            sys.exit()

    def add_player(self):
        """Function create while to save data and append the player's information in table."""
        try:
            while len(self.players_information) < nb_players:
                self.players_information.append(add_players())
        except ValueError:
            logging.info("une erreur est survenu veuillez recommencez svp")

    def add_players_data(self):
        """
        Function has a purpose to serialized_players for DBB.

        :return: Table to sorte rank or point, another way to avoid query always.
        """
        for player in self.players_information:
            serialized_players = {
                "players_name": player.nom,
                "player_birthday": player.date_de_naissance,
                "player_sexe": player.sexe,
                "player_rank": player.rank,
                "player_score": player.score,
            }

            self.players_table.truncate()  # clear the table first
            self.table_save_players.append(serialized_players)
            self.players_table.insert_multiple(self.table_save_players)

        return self.table_save_players

    def create_tournant(self):
        """
        Function serialized_tournant.

        :return: Return data for traitement for the other version.
        """
        self.tournant_data.append(create_tournant())
        for tournoi in self.tournant_data:
            serialized_tournoi = {
                "tournoi_name": tournoi.name,
                "tournoi_place": tournoi.place,
                "tournoi_date": tournoi.date,
                "tournoi_tour": nombre_tour,
                "tournoi_time": tournoi.time,
                "tournoi_number_round": [],
                "tournoi_desc": tournoi.description,
            }

            self.tournoi_table.truncate()
            self.tournoi_table.insert(serialized_tournoi)

        return self.tournant_save_data

    def get_rank_players(self):
        """Function create loop to sorte the players by their ranks."""
        for player in self.table_save_players:
            self.data_rank_players.insert(
                player["player_rank"] - 1, player
            )  # trier par rangs
        self.data_rank_players = sorted(
            self.data_rank_players, key=itemgetter("player_rank")
        )

    def create_sys_swiss_paring(self):
        """
        Function create Swiss Sys.

        1 - At first tours, make pair to sorte all players by their rank.
        2 - Make play "player 1 with player 5" - "player 2 with player 6".
        3 - For other tours sorte the match with their points, on after the other
            "player 1 with player 2" - "player 3 with player 4".

        We enter the round number, and we work with statement.
        Each Round have an algorithm.

        :return: False if the error has been detected.
        """
        try:
            while True:
                nb_round = input(str("sélectionner votre round "
                                     "( indiquer la lettre 'q' pour arrêter le tournoi ): "))
                if nb_round == "q":
                    break
                if nb_round == "1":
                    print(f"round {nb_round}")
                    date_begin, date_end = date_begin_and_end()
                    for x in range(0, nb_player_for_swiss):
                        match_round_1 = self.data_rank_players[x]["players_name"]
                        match_round_1_adversaire = self.data_rank_players[
                            x + nb_player_for_swiss]["players_name"]
                        matchs_tour = [match_round_1, match_round_1_adversaire]
                        matchs_tour_score_swiss_start = (
                            self.data_rank_players[x],
                            self.data_rank_players[x + nb_player_for_swiss],
                        )

                        self.body_algo_match(
                            match_round_1,
                            match_round_1_adversaire,
                            matchs_tour,
                            matchs_tour_score_swiss_start,
                            0,
                        )
                        rounds = Round(nb_round, matchs_tour, date_begin, date_end)
                        self.tours.append(rounds)
                else:
                    date_begin, date_end = date_begin_and_end()
                    self.create_other_round(nb_round, date_begin, date_end)
        except Exception as ex:
            logging.error(ex)
            return False

    def body_algo_match(self, param1, param2, param3, param4, param5):
        """
        Function creat body for the algorithm with statement.

        :param1: Player's name for player 1.
        :param2: Player's name for player 2.
        :param3: Take name player's name for print it and for the query in dbb and change his score.
        :param4: Take player's score, and we concatenate the new point we this old score.
        :param5: The second round until fourth we take old score only with query.
        """
        score = round_player(param1, param2)
        if score == "1":
            print(str(param3[0]) + " a ganger la la parti ")
            self.players_table.update(
                {"player_score": float(param4[0]["player_score"]) + float(1)},
                user.players_name == str(param3[0]),
            )
        elif score == "2":
            self.players_table.update(
                {"player_score": float(param4[1]["player_score"]) + float(1)},
                user.players_name == str(param3[1]),
            )
            print(str(param3[1]) + " a ganger la la parti ")
        elif score == "3":
            for i in param3:
                self.players_table.update(
                    {"player_score": float(param5) + float(0.5)},
                    user.players_name == str(i),
                )
                print(str(i) + " ont fais match null ")

    def create_other_round(self, Round_number, DateBegin, DateEnd):
        """
        Function creat the algorithm for second until fourth rounds.

        Parameters are only here to register in database.

        param Round_number: Take the integer input for database.
        param DateBegin: take input for date tournante begin.
        param DateEnd: take input for date tournante End.

        """
        players = sorted(
            self.players_table.all(), key=lambda k: k["player_score"], reverse=True
        )
        lenght = int(len(players))
        for x in range(1, lenght, 2):
            player_1 = players[x - 1]["players_name"]
            player_2 = players[x]["players_name"]
            player_score_for_function = players[x]["player_score"]
            matchs_tours_other_name = player_1, player_2
            matchs_tours_other_score = players[x - 1], players[x]
            rounds_other = Round(
                Round_number, list(matchs_tours_other_name), DateBegin, DateEnd
            )
            self.tours.append(rounds_other)
            self.body_algo_match(
                player_1,
                player_2,
                matchs_tours_other_name,
                matchs_tours_other_score,
                player_score_for_function,
            )

    def created_round(self):
        """
        Function has a purpose to serialized_round for DBB.

        :variable self.tours: table for data with all players, scores and dates.
        """
        for tours in self.tours:
            serialized_tours = {
                "tour_number": tours.round_number,
                "tour_matchs": tours.match,
                "tour_debut": tours.date_begin,
                "tour_fin": tours.date_end,
            }
            self.table_round.truncate()
            self.match.append(serialized_tours)
            self.table_round.insert_multiple(self.match)

    def admin_power_change_rank(self):
        """
        This function has purpose to change rank player with his name.

        This code serve to switch the rank of players to avoid same rank
        """
        nom_joueur = input("veuillez entrer le nom du joeur concerné : ")
        # search  in ddb
        name_for_take_rank = self.players_table.search(user.players_name == nom_joueur)
        for i in name_for_take_rank:
            self.rank_save_for_replace = i["player_rank"]
        rang_modif = int(input("quel est le rang que vous vouliez lui mettre :  "))
        search_rank = self.players_table.search(user.player_rank == rang_modif)
        for name_player_search in search_rank:
            self.name_player_switch_rank = name_player_search["players_name"]
        self.players_table.update(
            {"player_rank": self.rank_save_for_replace},
            user.players_name == str(self.name_player_switch_rank),
        )
        self.players_table.update(
            {"player_rank": rang_modif}, user.players_name == nom_joueur
        )


def main():
    """Principal function to run all program."""
    controller = Controller()
    controller.interface_main_manu()
    controller.add_player()
    controller.add_players_data()
    controller.create_tournant()
    controller.get_rank_players()
    controller.create_sys_swiss_paring()
    controller.created_round()
