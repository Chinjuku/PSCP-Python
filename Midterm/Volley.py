"""Volleyball"""
def main():
    """Volleyball"""
    text = input()
    team_a_score = 0
    team_b_score = 0
    team_a_win = 0
    team_b_win = 0
    game_set = 25
    deal = 24
    game = 1
    for i in text:
        if i == "A":
            team_a_score += 1
        if i == "B":
            team_b_score += 1
        if game == 5:
            game_set = 15
            deal = 14
        if ((team_a_score == game_set or team_b_score == game_set) and \
            (abs(team_a_score-team_b_score) >= 2)) or ((team_a_score > deal or \
                team_b_score > deal) and abs(team_a_score-team_b_score) == 2):
            print("Set %d: A (%d) | B (%d)" %(game, team_a_score, team_b_score))
            game += 1
            if team_a_score > team_b_score:
                team_a_win += 1
            else:
                team_b_win += 1
            team_a_score = team_b_score = 0
    if team_a_win == 3:
        print("A won %d:%d set" %(team_a_win, team_b_win))
    elif team_b_win == 3:
        print("B won %d:%d set" %(team_b_win, team_a_win))
    else:
        print("Set %d: A (%d) | B (%d)" %(game, team_a_score, team_b_score))
        print("The game has not finished yet.")
main()
