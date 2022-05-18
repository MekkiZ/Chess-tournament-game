class Tournament:

    def __init__(self, name, place, date, time, description,  nb_tour=4):
        self.name = name
        self.place = place
        self.date = date
        self.nb_tour = nb_tour
        self.time = time
        self.description = description

    def __str__(self):
        return f"{self.name},{self.place},{self.date}"


class Player:
    def __init__(self, nom, prenom, date_de_naissance, sexe, classement):
            self.nom = nom
            self.prenom = prenom
            self.date_de_naissance = date_de_naissance
            self.sexe = sexe
            self.classement = classement

    def __str__(self):
        return f"{self.nom},{self.prenom},{self.date_de_naissance},{self.sexe},{self.classement}"




class Tours:
    def __init__(self, players):
        self.players = players
        match = ([players], [results])

 def __str__(self):
        return f"{self.player_in_game},{self.results}"


class Match(Tours):
    def __init__(self, players, results):
        super().__init__(players)
        self.results = results


