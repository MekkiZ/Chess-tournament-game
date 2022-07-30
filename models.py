class Tournament:
    def __init__(self, name, place, date, time, round_tourne, description, nb_tour=4):
        self.name = name
        self.place = place
        self.date = date
        self.nb_tour = nb_tour
        self.time = time
        self.round_number = round_tourne
        self.description = description

    def __str__(self):
        return f"{self.name},{self.place},{self.date}"


class Player:
    def __init__(self, nom, date_de_naissance, sexe, rank):
        self.nom= nom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.rank = rank

    def __str__(self):
        return f"{self.nom}, {self.date_de_naissance},{ self.sexe}, {self.rank}"
    def __repr__(self):
        return f"{self.nom}, {self.date_de_naissance},{ self.sexe}, {self.rank}"



class Round:
    def __init__(self, match, results, round_number, date_begin, date_end):
        self.match = match
        self.results = results
        self.round_number = round_number
        self.date_begin = date_begin
        self.date_end = date_end

    def __str__(self):
        return f"{self.match},{self.results},{self.round_number},{self.date_begin}, {self.date_end}"

