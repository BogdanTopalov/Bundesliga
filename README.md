# Bundesliga


Django REST framework + ReactJS website that displays Bundesliga season information (teams + matches).


## Quick look

<img src="https://i.postimg.cc/jqGVXCvD/Bundesliga.gif"/>


## How to start it?

**Back-end steps:**
1. cd to the **back-end** folder.
2. Execute `python -m venv venv` in the terminal to create venv.
3. Activate venv.
4. Execute `pip install -r requirements.txt` in the terminal.
5. Execute `python manage.py runserver`.

**Front-end steps:**
1. cd to **front-end/app** folder.
2. Execute `npm install` in the terminal.
3. Execute `npm start` in the terminal and access it at **http://localhost:3000**.


## Django REST framework API

The main data is provided with the help of this api -> https://github.com/Dirrot/python-openligadb-api

**Main url**: http://127.0.0.1:8000/

**Paths:**
- `teams/` - returns list of objects with all bundesliga teams information  
Example: 
```
[
    {
        "teamID": 65,
        "teamInfo": {
            "teamName": "1. FC Köln",
            "teamIconURL": "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/FC_Cologne_logo.svg/1200px-FC_Cologne_logo.svg.png",
            "winLossRatio": 1.33
        }
    },
    {
        "teamID": 80,
        "teamInfo": {
            "teamName": "1. FC Union Berlin",
            "teamIconURL": "https://www.fc-union-berlin.de/cache/1-FC-Union-Berlin-e979b4b72734cc0af9d1b159719235b9.png",
            "winLossRatio": 7.0
        }
    },
    ...
]
```

- `teams/<int:pk>/` - returns object with the selected team information  
Example:
```
{
    "teamInfo": {
        "teamName": "Bayer Leverkusen",
        "teamIconURL": "https://upload.wikimedia.org/wikipedia/de/thumb/f/f7/Bayer_Leverkusen_Logo.svg/1200px-Bayer_Leverkusen_Logo.svg.png",
        "winLossRatio": 0.33
    },
    "teamMatches": [
        {
            "matchRound": 1,
            "matchID": 63867,
            "matchDate": "2022-08-06",
            "matchTime": "18:30",
            "matchIsFinished": true,
            "homeTeamID": 7,
            "homeTeamName": "Borussia Dortmund",
            "homeTeamIconURL": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/67/Borussia_Dortmund_logo.svg/560px-Borussia_Dortmund_logo.svg.png",
            "homeTeamGoals": 1,
            "awayTeamID": 6,
            "awayTeamName": "Bayer Leverkusen",
            "awayTeamIconURL": "https://upload.wikimedia.org/wikipedia/de/thumb/f/f7/Bayer_Leverkusen_Logo.svg/1200px-Bayer_Leverkusen_Logo.svg.png",
            "awayTeamGoals": 0,
            "winnerID": 7,
            "loserID": 6
        },
      ...
    ]
}
```
- `all_season_matches_by_rounds/` - returns list of objects with each round matches information  
Example:
```
[
    {
        "roundNumber": 1,
        "roundMatches": [
            {
                "matchRound": 1,
                "matchID": 63864,
                "matchDate": "2022-08-05",
                "matchTime": "20:30",
                "matchIsFinished": true,
                "homeTeamID": 91,
                "homeTeamName": "Eintracht Frankfurt",
                "homeTeamIconURL": "https://i.imgur.com/X8NFkOb.png",
                "homeTeamGoals": 1,
                "awayTeamID": 40,
                "awayTeamName": "FC Bayern München",
                "awayTeamIconURL": "https://i.imgur.com/jJEsJrj.png",
                "awayTeamGoals": 6,
                "winnerID": 40,
                "loserID": 91
            },
            {
                "matchRound": 1,
                "matchID": 63865,
                "matchDate": "2022-08-06",
                "matchTime": "15:30",
                "matchIsFinished": true,
                "homeTeamID": 95,
                "homeTeamName": "FC Augsburg",
                "homeTeamIconURL": "https://i.imgur.com/sdE62e2.png",
                "homeTeamGoals": 0,
                "awayTeamID": 112,
                "awayTeamName": "SC Freiburg",
                "awayTeamIconURL": "https://i.imgur.com/r3mvi0h.png",
                "awayTeamGoals": 4,
                "winnerID": 112,
                "loserID": 95
            },
            ...
        ]
    },
    {
        "roundNumber": 2,
        "roundMatches": [...]
    },
    ...
            
```

- `next_upcoming_matches/` - returns list of objects with upcoming matches information (following Gameday)  
Example:
```
Same as the above one with the exception that the list contains only upcoming rounds information.
```


- `gameday_matches/` - returns object with gameday matches information  
Example:
```
{
    "roundNumber": 11,
    "roundMatches": [
        {
            "matchRound": 11,
            "matchID": 63963,
            "matchDate": "2022-10-21",
            "matchTime": "20:30",
            "matchIsFinished": true,
            "homeTeamID": 81,
            "homeTeamName": "1. FSV Mainz 05",
            "homeTeamIconURL": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Logo_Mainz_05.svg/1200px-Logo_Mainz_05.svg.png",
            "homeTeamGoals": 5,
            "awayTeamID": 65,
            "awayTeamName": "1. FC Köln",
            "awayTeamIconURL": "https://upload.wikimedia.org/wikipedia/en/thumb/5/53/FC_Cologne_logo.svg/1200px-FC_Cologne_logo.svg.png",
            "awayTeamGoals": 0,
            "winnerID": 81,
            "loserID": 65
        },
        ...
    ]
}
```

