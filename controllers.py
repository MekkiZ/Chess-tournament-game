from models import Tournament, Player, Round
from view import add_players, create_tournant, generate_match, enter_results, nombre_tour
from tinydb import TinyDB, Query

db = TinyDB("db.json")

nb_players = 2
ration_result_match = 2

class Controller:

    def __init__(self):
        # models

        self.results_data = []
        self.data_name_players = []
        self.tournant_save_data = []
        self.table_save_players = []
        self.players_information = []

        self.tournant_data = []
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

        return self.data_name_players

    def get_results_data(self):
        pass
        
    def creat_round(self):
        """
        un tour est une liste de match
        1re tour = 4 matchs
        2tr = 2 matchs
        3tr = 1 match
        """

        match = (self.data_name_players, [str(enter_results())])
        #print(match)


controller = Controller()
controller.add_player()
controller.add_players_data()
# controller.create_tournant()
controller.get_data_player()
controller.get_results_data()
controller.creat_round()
