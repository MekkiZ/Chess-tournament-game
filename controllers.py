from view import add_players, create_tournant, nombre_tour, round_player, enter_round_number
import re
from tinydb import TinyDB, Query
import random
from operator import itemgetter
from models import Round

db = TinyDB("db.json")
user = Query()

nb_players = 4
nb_player_for_swiss = int(nb_players / 2)
ration_result_match = 2


class Controller:

    def __init__(self):
        # models

        self.point = float(1)
        self.result = []
        self.tournant_data = []
        self.data_rank_players = []
        self.data_name_players = []
        self.tournant_save_data = []
        self.table_save_players = []
        self.players_information = []
        self.tours = []
        self.score = []
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
                                  "player_rank": player.rank,
                                  "player_score": player.score
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
                                  "tournoi_number_round": [],
                                  "tournoi_desc": tournoi.description,
                                  }

            self.tournoi_table.truncate()
            self.tournant_save_data.append(serialized_tournoi)
            self.tournoi_table.insert(self.tournant_save_data)

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

    def create_sys_swiss_paring_first_tour(self):  # mettre le numero de tour pour comprendre quels algo mettre
        self.point = 1
        for x in range(0, nb_player_for_swiss):  # create first tour of tournemant
            # score = [input('rensienger les resulta')]
            match_round_1 = self.data_rank_players[x]["players_name"]
            # print(match_round_1)
            match_round_1_adversaire = self.data_rank_players[x + nb_player_for_swiss]["players_name"]
            # print(match_round_1_adversaire)
            # show_match = ("{} vs {}".format(match_round_1, match_round_1_adversaire))
            matchs_tour = [match_round_1, match_round_1_adversaire]
            self.tours.append(matchs_tour)
            score = round_player(match_round_1, match_round_1_adversaire)
            if score == "1":
                print(matchs_tour[0] + " a ganger la la parti ")
                self.players_table.update({'player_score': float(self.point)}, user.players_name == str(matchs_tour[0]))
            elif score == "2":
                # print(matchs_tour[1] + " a ganger  la parti ")
                self.players_table.update({'player_score': float(self.point)}, user.players_name == str(matchs_tour[1]))
            elif score == "3":
                for i in matchs_tour:
                    # print(i)
                    self.players_table.update({'player_score': float(self.point / 2)}, user.players_name == str(i))

                # print(f"cette parti est controller condition 3  {matchs_tour}")
        self.create_other_round()
        # print(self.tours)
        return self.tours

    def random(self, param1, param2):
        for x in range(0, param1):  # trouver la bonne equation pour les faire jouer tous ensemble
            match_round_2_win = param2[x * 2]["players_name"]
            match_round_2_adversaire_win = param2[(x * 2) + 1]["players_name"]
            # print(  " vs " )

            score = round_player(match_round_2_win, match_round_2_adversaire_win)
            match_round2_win = [match_round_2_win, match_round_2_adversaire_win]
            print("ici nous somme dans la fnction random et ceci montre le score du joeuur : " +
                  str(param2[x * 2]["player_score"]) + " " + str(param2[x * 2]["players_name"]))

            if score == "1":
                score_update = float(param2[x * 2]["player_score"] + 1)
                print(match_round2_win[0] + " a ganger la la parti ")

                self.players_table.update({'player_score': score_update},
                                          user.players_name == str(match_round2_win[0]))
            elif score == "2":
                # print(matchs_tour[1] + " a ganger  la parti ")
                self.players_table.update({'player_score': float(param2[(x * 2) + 1]["player_score"] + 1)},
                                          user.players_name == str(match_round2_win[1]))
            elif score == "3":
                for i in match_round2_win:
                    self.players_table.update({'player_score': float(param2[(x * 2) + 1]["player_score"] + 0.5)},
                                              user.players_name == str(i))

    def create_other_round(self):

        fr1 = self.players_table.search((user.player_score == 1.0) |
                                        (user.player_score == 2.0) |
                                        (user.player_score == 3.0))
        fr2 = self.players_table.search((user.player_score == 0.5) |
                                        (user.player_score == 1.5) |
                                        (user.player_score == 2.5))
        fr3 = self.players_table.search(user.player_score == 0)
        table_loop = self.players_table.all()
        lenght_players_win = int(len(fr1) / 2)
        lenght_players_draw = int(len(fr2) / 2)
        lenght_players_loose = int(len(fr3) / 2)
        nb = 1
        while nb <= 4:
            nb = int(input("nombre du tours :"))
            self.random(lenght_players_win, fr1)

            self.random(lenght_players_draw, fr2)

            self.random(lenght_players_loose, fr3)

    def created_round(self):
        for tours in self.tours:
            sereliaze_tours = {
                "tour_number": tours.round_number,
                "tour_matchs": self.tours,
                "tour_debut": tours.date_begin,
                "tour_fin": tours.date_end,
                "tours_score": tours.score
            }


controller = Controller()
controller.add_player()
controller.add_players_data()
# controller.create_tournant()
controller.get_data_player()
# controller.get_data_score()
controller.get_rank_players()
controller.create_sys_swiss_paring_first_tour()
"""controller.create_other_round()"""
