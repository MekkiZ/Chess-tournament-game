from models import Tournament, Player, Tours
from view import add_players

nb_players = 2


class Controller:
    def __init__(self):
        # models
        self.players = []

        #view
        #self.view= View

    def add_player(self):

        while len(self.players) < nb_players:
            self.players.append(add_players())

        print(self.players)





