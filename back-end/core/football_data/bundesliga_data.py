from OpenLigaDbApi.api import API


BUNDESLIGA = 'bl1'
SEASON_2022 = '2022'

a = API()

current_round = a.getCurrentGroupOrderID(BUNDESLIGA)

bundesliga_teams_data = a.getTeamsByLeagueSaison(BUNDESLIGA, SEASON_2022)['Team']

all_season_matches_data = a.getMatchdataByLeagueSaison(BUNDESLIGA, SEASON_2022)['Matchdata']


def get_all_season_matches_info():
    """
    Optimized all season matches data.
    """

    all_season_matches_info = []

    for match in all_season_matches_data:
        match_datetime = match['matchDateTime']
        match_date = f'{match_datetime.date()}'
        match_time = f'{match_datetime.time().hour}:{match_datetime.time().minute}'

        match_is_finished = match['matchIsFinished']

        home_team_goals = match['pointsTeam1'] if match_is_finished else '-'
        away_team_goals = match['pointsTeam2'] if match_is_finished else '-'

        winner_id = None
        loser_id = None

        # Set winning and losing team.
        if home_team_goals != '-' and home_team_goals != away_team_goals:
            if home_team_goals > away_team_goals:
                winner_id = match['idTeam1']
                loser_id = match['idTeam2']
            else:
                winner_id = match['idTeam2']
                loser_id = match['idTeam1']

        match_info = {
            'matchRound': match['groupOrderID'],
            'matchID': match['matchID'],
            'matchDate': match_date,
            'matchTime': match_time,
            'matchIsFinished': match_is_finished,
            'homeTeamID': match['idTeam1'],
            'homeTeamName': match['nameTeam1'],
            'homeTeamIconURL': match['iconUrlTeam1'],
            'homeTeamGoals': home_team_goals,
            'awayTeamID': match['idTeam2'],
            'awayTeamName': match['nameTeam2'],
            'awayTeamIconURL': match['iconUrlTeam2'],
            'awayTeamGoals': away_team_goals,
            'winnerID': winner_id,
            'loserID': loser_id,
        }
        all_season_matches_info.append(match_info)

    return all_season_matches_info


def get_all_season_matches_info_by_rounds():
    """
    Sort all bundesliga matches by their rounds.
    """

    all_season_matches_info = get_all_season_matches_info()
    all_season_matches_info_by_rounds = []

    for round_number in range(1, 35):
        all_season_matches_info_by_rounds.append({
            'roundNumber': round_number,
            'roundMatches': [
                match
                for match in all_season_matches_info
                if match['matchRound'] == round_number
            ]
        })

    return all_season_matches_info_by_rounds


def get_next_upcoming_matches():
    """
    All upcoming matches following gameday.
    """

    all_season_matches_info_by_rounds = get_all_season_matches_info_by_rounds()

    next_upcoming_matches = [
        r
        for r in all_season_matches_info_by_rounds
        if r['roundNumber'] > current_round
    ]

    return next_upcoming_matches


def get_bundesliga_teams_info():
    """
    Optimized bundesliga teams info. Including Win/Loss ratio.
    """

    all_season_matches_info = get_all_season_matches_info()

    bundesliga_teams_info = []

    for team in bundesliga_teams_data:
        team_id = team['teamID']
        team_name = team['teamName']
        team_icon_url = team['teamIconURL']

        wins = 0
        losses = 0

        # Calculate Win/Loss ratio of each team this season.
        for m in all_season_matches_info:
            if m['matchIsFinished']:
                if team_id == m['winnerID']:
                    wins += 1
                elif team_id == m['loserID']:
                    losses += 1

        win_loss_ratio = round((wins / losses), 2)

        team_info = {
            'teamID': team_id,
            'teamInfo': {
                'teamName': team_name,
                'teamIconURL': team_icon_url,
                'winLossRatio': win_loss_ratio
            }
        }
        bundesliga_teams_info.append(team_info)

    return bundesliga_teams_info


def get_gameday_matches():
    all_season_matches_info_by_rounds = get_all_season_matches_info_by_rounds()

    gameday_matches = all_season_matches_info_by_rounds[current_round - 1]

    return gameday_matches


def get_selected_team_info(pk):
    bundesliga_teams_info = get_bundesliga_teams_info()
    all_season_matches = get_all_season_matches_info()

    team = [
        team
        for team in bundesliga_teams_info
        if team['teamID'] == pk
    ][0]

    team_matches = [
        match
        for match in all_season_matches
        if match['homeTeamID'] == pk or match['awayTeamID'] == pk
    ]

    team_info = {
        'teamInfo': team['teamInfo'],
        'teamMatches': team_matches,
    }

    return team_info
