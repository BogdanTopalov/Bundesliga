from rest_framework.response import Response
from rest_framework.views import APIView

from core.football_data.bundesliga_data import \
    get_bundesliga_teams_info, get_all_season_matches_info_by_rounds,\
    get_next_upcoming_matches, get_gameday_matches, get_selected_team_info


class ListTeams(APIView):
    def get(self, request):
        data = get_bundesliga_teams_info()
        return Response(data=data)


class AllSeasonMatches(APIView):
    def get(self, request):
        data = get_all_season_matches_info_by_rounds()
        return Response(data=data)


class NextUpcomingMatches(APIView):
    def get(self, request):
        data = get_next_upcoming_matches()
        return Response(data=data)


class GamedayMatches(APIView):
    def get(self, request):
        data = get_gameday_matches()
        return Response(data=data)


class SelectedTeam(APIView):
    def get(self, request, pk):
        data = get_selected_team_info(pk)
        return Response(data=data)
