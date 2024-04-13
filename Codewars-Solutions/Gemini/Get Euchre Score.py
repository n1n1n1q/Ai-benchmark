def update_score(current_score, called_trump, alone, tricks):
    calling_team, other_team = current_score
    team_tricks = tricks[called_trump - 1]
    other_tricks = 5 - team_tricks

    # Points earned by each team (default: 0)
    calling_team_points = 0
    other_team_points = 0

    # Determine points based on calling team
    if called_trump == 1:
        # Team 1 called trump
        if team_tricks <= 2:
            other_team_points = 2  # Team 1 euchred
        elif team_tricks == 3 or team_tricks == 4:
            calling_team_points = 1
        elif team_tricks == 5 and not alone:
            calling_team_points = 2
        elif team_tricks == 5 and alone:
            calling_team_points = 4
    else:
        # Team 2 called trump
        if other_tricks <= 2:
            calling_team_points = 2  # Team 2 euchred
        elif other_tricks == 3 or other_tricks == 4:
            other_team_points = 1

    # Update score for both teams
    return [calling_team + calling_team_points, other_team + other_team_points]
