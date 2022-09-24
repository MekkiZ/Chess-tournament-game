"""system module."""


class Tournament:
    """Creat models tournante for dbb."""

    def __init__(self, name, place, date, time, rounds, description, status, nb_tour=4):
        """We creat models for with parameters for dbb."""
        self.name = name
        self.place = place
        self.date = date
        self.nb_tour = nb_tour
        self.time = time
        self.round_number = rounds
        self.description = description
        self.status = status

    def __str__(self):
        """The function returns a user-friendly description of an object."""
        return f"{self.name},{self.place},{self.date}"


class Player:
    """Creat models players for dbb."""

    def __init__(self, nom, date_de_naissance, sexe, rank, score):
        """We creat models for with parameters for dbb."""
        self.nom = nom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.rank = rank
        self.score = score

    def __str__(self):
        """The function returns a user-friendly description of an object."""
        return f"{self.nom}, {self.date_de_naissance},{self.sexe}, {self.rank}"

    def __repr__(self):
        """Return string representation of option."""
        return f"{self.nom}, {self.date_de_naissance},{self.sexe}, {self.rank}"


class Round:
    """Creat models round for dbb."""

    def __init__(self, round_number, match, date_begin, date_end):
        """We creat models for with parameters for dbb."""
        self.round_number = round_number
        self.match = match
        self.date_begin = date_begin
        self.date_end = date_end

    def __str__(self):
        """The function returns a user-friendly description of an object."""
        return f"{self.match},{self.round_number},{self.date_begin}, {self.date_end}"

    def __repr__(self):
        """Return string representation of option."""
        return f"{self.match},{self.round_number},{self.date_begin}, {self.date_end}"
