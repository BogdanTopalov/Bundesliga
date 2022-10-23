from django.urls import path

from core.api.views import ListTeams, AllSeasonMatches, NextUpcomingMatches, GamedayMatches, SelectedTeam


urlpatterns = [
    path('teams/', ListTeams.as_view()),
    path('teams/<int:pk>', SelectedTeam.as_view()),
    path('all_season_matches_by_rounds/', AllSeasonMatches.as_view()),
    path('next_upcoming_matches/', NextUpcomingMatches.as_view()),
    path('gameday_matches/', GamedayMatches.as_view()),
]
