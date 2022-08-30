# Chess project

## Description
This app generate tournament with height players ( number by default ) with Swiss system.
## Setup
Create a virtualenv for the project with Python 3.9.10
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
# Run the script

Run this command :
```
python3 main.py
```
Now you have this :
```
=========================
Sélectionner votre choix: 
1. Créer un tournoi
2. Modifier le rang d'un joueur
3. Quitter le jeu
=========================
S'il vous plait faite un choix >>  

```
You have two features; you can creat a tournament  and enter all information's player
and start the matchs.

After finish the four rounds you have to put 'q' word to stop the game:
```
sélectionner votre round ( indiquer la lettre 'q' pour arrêter le tournoi ): q

```
# Report with FLAKE8
You can verify the code and make sure there is no mistakes, on folders :   
flake-report / index.html. Just click on file html.

# What I learned with this project
For the beginning,  I created a script without PEP8 convention.
I realised that the PEP8 convention was great to improve the quality of my code.
I learned how make sub function, each function has specific purpose.
Use a different pattern : MVC.
