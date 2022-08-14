class Tournament:
    def __init__(self, name, place, date, time, round, description, nb_tour=4):
        self.name = name
        self.place = place
        self.date = date
        self.nb_tour = nb_tour
        self.time = time
        self.round_number = round
        self.description = description


    def __str__(self):
        return f"{self.name},{self.place},{self.date}"


class Player:
    def __init__(self, nom, date_de_naissance, sexe, rank, score):
        self.nom = nom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.rank = rank
        self.score = score

    def __str__(self):
        return f"{self.nom}, {self.date_de_naissance},{self.sexe}, {self.rank}"

    def __repr__(self):
        return f"{self.nom}, {self.date_de_naissance},{self.sexe}, {self.rank}"


class Round:

    def __init__(self, round_number, match,  date_begin, date_end):
        self.round_number = round_number
        self.match = match
        self.date_begin = date_begin
        self.date_end = date_end


    def __str__(self):
        return f"{self.match},{self.round_number},{self.date_begin}, {self.date_end}"

