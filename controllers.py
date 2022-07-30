from models import Tournament, Player, Round
from view import add_players, create_tournant, generate_match, enter_results, nombre_tour
from tinydb import TinyDB

db = TinyDB("db.json")

nb_players = 2


class Controller:


    def __init__(self):
        # models

        self.players = []
        self.rondes = []
        self.tournant_data = []


        #view
        #self.view= View

    def add_player(self):

        while len(self.players) < nb_players:
            self.players.append(add_players())
        #print(self.players)



    def add_players_data(self):
        table_save_players= []
        for player in self.players:
            serialized_players = {"players_name" : player.nom,
                           "player_birthday" : player.date_de_naissance,
                           "player_sexe" : player.sexe,
                           "player_rank" : player.rank
                           }
            players_table = db.table("players")
            players_table.truncate()  # clear the table first

            #players_table.all()
            table_save_players.append(serialized_players)
            players_table.insert_multiple(table_save_players)
            print(table_save_players)

        return table_save_players


    def create_tournant(self):
        self.tournant_data.append(create_tournant())
        tournant_save_data =[]

        for tournoi in self.tournant_data:
            serialized_tournoi = {"tournoi_name": tournoi.name,
                                  "tournoi_place": tournoi.place,
                                  "tournoi_date": tournoi.date,
                                  "tournoi_tour": nombre_tour,
                                  "tournoi_time": tournoi.time,
                                  "tournoi_number_round": tournoi.round_number,
                                  "tournoi_desc" : tournoi.description,
                                  }
            tournoi_table = db.table("tournoi")
            tournoi_table.truncate()
            tournant_save_data.append(serialized_tournoi)
            tournoi_table.insert_multiple(tournant_save_data)

        return tournant_save_data

    def round(self):












    def generate_match(self):
        pass










controller = Controller()
controller.add_player()
#controller.create_tournant()
controller.add_players_data()
controller.create_tournant()
