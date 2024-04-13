"""
the most successful solution, passes 4/5 test cases
"""


def update_score(current_score, called_trump, alone, tricks):
    # Count number of tricks for each team
    team1_tricks = tricks.count(1)
    team2_tricks = tricks.count(2)

    # Determine points for the team that called trump
    trump_points = 0
    if called_trump == 1:
        if alone:
            if team1_tricks == 5:
                trump_points = 4
        else:
            if team1_tricks <= 2:
                trump_points = 2
            elif team1_tricks <= 4:
                trump_points = 1
            elif team1_tricks == 5:
                trump_points = 2
    elif called_trump == 2:
        if alone:
            if team2_tricks == 5:
                trump_points = 4
        else:
            if team2_tricks <= 2:
                trump_points = 2
            elif team2_tricks <= 4:
                trump_points = 1
            elif team2_tricks == 5:
                trump_points = 2

    # Update the score
    new_score = [current_score[0], current_score[1]]
    if called_trump == 1:
        new_score[0] += trump_points
    elif called_trump == 2:
        new_score[1] += trump_points

    return new_score
