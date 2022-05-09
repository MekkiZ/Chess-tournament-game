from tinydb import TinyDB, Query

db = TinyDB('db.json')
User = Query()

class Tournament:

    def __init__(self, name, place, date, nb_tour=4):
        self.name = name
        self.place = place
        self.date = date
        self.nb_tour = nb_tour

    def __str__(self):
        return f"{self.name},{self.place},{self.date}"



class Player:
    def __init__(self, nom, prenom, date_de_naissance, sexe, classement):
            self.nom = nom
            self.prenom = prenom
            self.date_de_naissance = date_de_naissance
            self.sexe = sexe
            self.classmeent = classement






