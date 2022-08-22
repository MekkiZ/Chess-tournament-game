"""def create_other_round(self):
    fr1 = self.players_table.search(user.player_score == 1.0 or 2.0 or 3.0 or 4.0)
    fr2 = self.players_table.search(user.player_score == 0.5 or 1.5 or 2.5 or 3.5)
    fr3 = self.players_table.search(user.player_score == 0)
    table_loop = self.players_table.all()
    lenght_players_win = int(len(fr1) / 2)
    lenght_players_draw = int(len(fr2) / 2)
    lenght_players_loose = int(len(fr3) / 2)

    for x in range(0, lenght_players_win):  # trouver la bonne equation pour les faire jouer tous ensemble
        match_round_2_win = fr1[x * 2]["players_name"]
        match_round_2_adversaire_win = fr1[(x * 2) + 1]["players_name"]
        # print(  " vs " )
        print(float(fr1[x * 2]["player_score"]) + float(0.5))

        score, players = round_player(match_round_2_win, match_round_2_adversaire_win)
        match_round2_win = [match_round_2_win, match_round_2_adversaire_win]
        if score == "1":
            print(match_round2_win[0] + " a ganger la la parti ")
            self.players_table.update({'player_score': float(fr1[x * 2]["player_score"]) + float(1)},
                                      user.players_name == str(match_round2_win[0]))
        elif score == "2":
            # print(matchs_tour[1] + " a ganger  la parti ")
            self.players_table.update({'player_score': float(fr1[(x * 2) + 1]["player_score"]) + 1},
                                      user.players_name == str(match_round2_win[1]))
        elif score == "3":
            for i in match_round2_win:
                self.players_table.update({'player_score': float(fr1[(x * 2) + 1]["player_score"]) + 0.5},
                                          user.players_name == str(i))


for x in range(0, lenght_players_draw):  # trouver la bonne equation pour les faire jouer tous ensemble
        match_round_2 = fr2[x * 2]["players_name"]
        match_round_2_adversaire = fr2[(x * 2) + 1]["players_name"]
        # print(  " vs " )
        score, players = round_player(match_round_2, match_round_2_adversaire)
        match_round2 = [match_round_2, match_round_2_adversaire]
        if score == "1":
            print(match_round2[0] + " a ganger la la parti ")
            self.players_table.update({'player_score': float(self.point) + 1},
                                      user.players_name == str(match_round2[0]))
        elif score == "2":
            # print(matchs_tour[1] + " a ganger  la parti ")
            self.players_table.update({'player_score': float(self.point) + 1},
                                      user.players_name == str(match_round2[1]))
        elif score == "3":
            for i in match_round2:
                # print(i)
                self.players_table.update({'player_score': float(self.point / 2) + 0.5},
                                          user.players_name == str(i))

    for x in range(0, lenght_players_loose):  # trouver la bonne equation pour les faire jouer tous ensemble
        match_round_2_loss = fr3[x * 2]["players_name"]
        match_round_2_adversaire_loss = fr3[(x * 2) + 1]["players_name"]
        # print(  " vs " )
        score, players = round_player(match_round_2_loss, match_round_2_adversaire_loss)
        match_round2_loss = [match_round_2_loss, match_round_2_adversaire_loss]
        if score == "1":
            print(match_round2_loss[0] + " a ganger la la parti ")
            self.players_table.update({'player_score': float(self.point)},
                                      user.players_name == str(match_round2_loss[0]))
        elif score == "2":
            # print(matchs_tour[1] + " a ganger  la parti ")
            self.players_table.update({'player_score': float(self.point)},
                                      user.players_name == str(match_round2_loss[1]))
        elif score == "3":
            for i in match_round2_loss:
                # print(i)
                self.players_table.update({'player_score': float(self.point / 2)},
                                          user.players_name == str(i))"""

de = 1

for x in