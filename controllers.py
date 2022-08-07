from view import add_players, create_tournant, enter_results, nombre_tour

from tinydb import TinyDB, Query
import random
from operator import itemgetter

db = TinyDB("db.json")

nb_players = 4
nb_player_for_swiss = int(nb_players / 2)
ration_result_match = 2


class Controller:

    def __init__(self):
        # models

        self.tournant_data = []
        self.data_rank_players = []
        self.data_name_players = []
        self.tournant_save_data = []
        self.table_save_players = []
        self.players_information = []
        self.tours = []
        self.tournoi_table = db.table("tournoi")
        self.players_table = db.table("players")

        # view
        # self.view= View

    def add_player(self):

        while len(self.players_information) < nb_players:
            self.players_information.append(add_players())
        # print(self.players)

    def add_players_data(self):

        for player in self.players_information:
            serialized_players = {"players_name": player.nom,
                                  "player_birthday": player.date_de_naissance,
                                  "player_sexe": player.sexe,
                                  "player_rank": player.rank
                                  }

            self.players_table.truncate()  # clear the table first

            # players_table.all()
            self.table_save_players.append(serialized_players)
            self.players_table.insert_multiple(self.table_save_players)
        # print(self.table_save_players)

        return self.table_save_players

    def create_tournant(self):
        self.tournant_data.append(create_tournant())

        for tournoi in self.tournant_data:
            serialized_tournoi = {"tournoi_name": tournoi.name,
                                  "tournoi_place": tournoi.place,
                                  "tournoi_date": tournoi.date,
                                  "tournoi_tour": nombre_tour,
                                  "tournoi_time": tournoi.time,
                                  "tournoi_number_round": tournoi.round_number,
                                  "tournoi_desc": tournoi.description,
                                  }

            self.tournoi_table.truncate()
            self.tournant_save_data.append(serialized_tournoi)
            self.tournoi_table.insert_multiple(self.tournant_save_data)

        return self.tournant_save_data

    def get_data_player(self):
        get_date_from_list = self.table_save_players
        self.data_name_players = [d['players_name'] for d in get_date_from_list]
        # print(self.data_name_players)

        return self.data_name_players

    def get_rank_players(self):
        # print(self.table_save_players)

        for player in self.table_save_players:
            self.data_rank_players.insert(player["player_rank"] - 1, player)  # trier par rangs
            # print(player["player_rank"])

        self.data_rank_players = sorted(self.data_rank_players, key=itemgetter('player_rank'))
        # print(self.data_rank_players)

    def get_data_score(self):

        match = ([self.data_name_players[0] + " : " + str(enter_results())],
                 [self.data_name_players[1] + " : " + str(enter_results())])

    def create_sys_swiss_paring(self):

        for x in range(0, nb_player_for_swiss):  # create first tour of tournemant
            match_round_1 = self.data_rank_players[x]["players_name"]
            match_round_1_adversaire = self.data_rank_players[x + nb_player_for_swiss]["players_name"]
            print("{} vs {}".format(match_round_1, match_round_1_adversaire))





controller = Controller()
controller.add_player()
controller.add_players_data()
# controller.create_tournant()
controller.get_data_player()
# controller.get_data_score()
controller.get_rank_players()
controller.create_sys_swiss_paring()
