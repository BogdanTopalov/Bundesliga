from rest_framework import generics

from OpenLigaDbApi.api import API


class ListGames(generics.ListAPIView):
    pass


class GameDetails(generics.RetrieveAPIView):
    pass
