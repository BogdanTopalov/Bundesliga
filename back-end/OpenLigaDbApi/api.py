'''
Created on 31.01.2014
@author: Dirk Rother
@contact: dirrot@web.de
@license: GPL
@version: 0.1
GitHub: https://github.com/Dirrot/python-openligadb-api
'''

from suds.client import Client


class API(object):
    '''
    This class is a wrapper class for the openligadb api.
    '''

    API_PATH = "http://www.openligadb.de/Webservices/Sportsdata.asmx?WSDL"

    def info(self):
        '''
        Informations about the SOAP API.
        '''
        return self._getClient()

    def getAvailGroups(self, leagueShortcut, leagueSaison):
        ''' No.1
        Gibt eine Liste der bereits eingetragenen Spiel-Einteilungen
        (Spieltag, Vorrunde, Finale, ...) der als Parameter zu
        uebergebenden Liga + Saison zurueck.
        '''
        response = self._getClient().service.GetAvailGroups(leagueShortcut, leagueSaison)
        return response

    def getAvailLeagues(self):
        ''' No.2
        Gibt eine Struktur aller verfuegbaren Ligen zurueck! Erwartet
        keine Parameter. Das Ergebnis dieser Abfrage unterliegt
        einem serverseitigen Cache von 600 Sekunden.
        '''
        response = self._getClient().service.GetAvailLeagues()
        return response

    def getAvailLeaguesBySports(self, sportID):
        ''' No.3
        Gibt eine Struktur aller verfuegbaren Ligen fuer die zu
        uebergebende SportID zurueck. Diese ist aus 'GetAvailSports()'
        zu entnehmen!
        '''
        response = self._getClient().service.GetAvailLeaguesBySports(sportID)
        return response

    def getAvailSports(self):
        ''' No.4
        Gibt eine Liste der verfuegbaren Sportarten, fuer welche gueltige
        Ligen bestehen, zurueck. Erwartet keine Parameter
        '''
        response = self._getClient().service.GetAvailSports()
        return response

    def getCurrentGroup(self, leagueShortcut):
        ''' No.5
        Gibt die aktuelle Group (entspricht z.B. bei der
        Fussball-Bundesliga dem 'Spieltag') des als Parameter zu
        uebergebenden leagueShortcuts (z.B. 'bl1') aus. Der aktuelle
        Spieltag wird jeweils zur Haelfte der Zeit zwischen dem letzten
        Spiel des letzten Spieltages und dem ersten Spiel des naechsten
        Spieltages erhoeht.
        '''
        response = self._getClient().service.GetCurrentGroup(leagueShortcut)
        return response

    def getCurrentGroupOrderID(self, leagueShortcut):
        ''' No.6
        Gibt die aktuelle groupOrderID (entspricht z.B. bei der Fussball-Bundesliga
        dem 'Spieltag') des als Parameter zu uebergebenden leagueShortcuts
        (z.B. 'bl1') aus. Der aktuelle Spieltag wird jeweils zur Haelfte der Zeit
        zwischen dem letzten Spiel des letzten Spieltages und dem ersten Spiel des
        naechsten Spieltages erhoeht.
        '''
        response = self._getClient().service.GetCurrentGroupOrderID(leagueShortcut)
        return response

    def getFussballdaten(self, spieltag, liga, saison, userkennung):
        ''' No.7 - deprecated
        Gibt eine Struktur deutscher Fussball-Spieldaten zurueck. Diese Methode steht
        nur noch aus Gruenden der Kompatibilitaet zu aelteren Applikationen zur Verfuegung.
        Bitte nutzen sie vorrangig die GetMatchdata... - Methoden!
        '''
        pass;

    def getGoalGettersByLeagueSaison(self, leagueShortcut, leagueSaison):
        ''' No.8
        Gibt eine Liste der GoalGetter der als Parameter zu uebergebenden Liga
        + Saison zurueck.
        '''
        response = self._getClient().service.GetGoalGettersByLeagueSaison(leagueShortcut, leagueSaison)
        return response

    def getGoalsByLeagueSaison(self, leagueShortcut, leagueSaison):
        ''' No.9
        Gibt eine Liste aller Goals der als Parameter zu uebergebenden Liga
        + Saison zurueck.
        '''
        response = self._getClient().service.GetGoalsByLeagueSaison(leagueShortcut, leagueSaison)
        return response

    def getGoalsByMatch(self, matchID):
        ''' No.10
        Gibt eine Liste aller Goals des als Parameter zu uebergebenden Match zurueck.
        '''
        response = self._getClient().service.GetGoalsByMatch(matchID)
        return response

    def getLastChangeDateByGroupLeagueSaison(self, groupOrderID, leagueShortcut, leagueSaison):
        ''' No.11
        Gibt das Datum der letzten Aenderung in der als Parameter zu uebergebenden Liga
        + Saison zurueck. Kann verwendet werden, um clientseitg unnoetige Abfragen
        zu vermeiden (Cache)
        '''
        response = self._getClient().service.GetLastChangeDateByGroupLeagueSaison(groupOrderID, leagueShortcut,
                                                                                  leagueSaison)
        return response

    def getLastChangeDateByLeagueSaison(self, leagueShortcut, leagueSaison):
        ''' No.12
        Gibt das Datum der letzten Aenderung in der als Parameter zu uebergebenden Liga
        + Saison zurueck. Kann verwendet werden, um clientseitg unnoetige Abfragen
        zu vermeiden (Cache)
        '''
        response = self._getClient().service.GetLastChangeDateByLeagueSaison(leagueShortcut, leagueSaison)
        return response

    def getLastMatch(self, leagueShortcut):
        ''' No.13
        Gibt eine Struktur des zuletzt ausgetragenen Spieles der als Parameter zu
        uebergebenden Liga zurueck.
        '''
        response = self._getClient().service.GetLastMatch(leagueShortcut)
        return response

    def getLastMatchByLeagueTeam(self, leagueId, teamId):
        ''' No.14
        Gibt eine Struktur des zuletzt ausgetragenen Spieles des als Parameter zu
        uebergebenden Teams der ebenfalls zu uebergebenen Liga zurueck.
        '''
        response = self._getClient().service.GetLastMatchByLeagueTeam(leagueId, teamId)
        return response

    def getMatchByMatchID(self, matchID):
        ''' No.15
        Gibt eine Struktur des Spieles der als Parameter zu uebergebenden MatchID
        zurueck.
        '''
        response = self._getClient().service.GetMatchByMatchID(matchID)
        return response

    def getMatchdataByGroupLeagueSaison(self, groupOrderID, leagueShortcut, leagueSaison):
        ''' No.16
        Gibt eine Struktur von Sport-Spieldaten zurueck. Als Parameter werden eine
        groupOrderID (zu entnehmen aus GetAvailGroups, entspricht z.B. bei der
        Fussball-Bundesliga dem Spieltag), der Liga-Shortcut (z.B. 'bl1') sowie die
        Saison (aus GetAvailLeagues, z.B. '2009') erwartet. Das Ergebnis dieser
        Abfrage unterliegt einem serverseitigen Cache von 120 Sekunden.
        '''
        response = self._getClient().service.GetMatchdataByGroupLeagueSaison(groupOrderID, leagueShortcut, leagueSaison)
        return response

    def getMatchdataByGroupLeagueSaisonJSON(self, groupOrderID, leagueShortcut, leagueSaison):
        ''' No.17
        Gibt einen serialisiertes JSON-Objekt von Sport-Spieldaten zurueck. Als
        Parameter werden eine groupOrderID (zu entnehmen aus GetAvailGroups,
        entspricht z.B. bei der Fussball-Bundesliga dem Spieltag), der Liga-Shortcut
         (z.B. 'bl1') sowie die Saison (aus GetAvailLeagues, z.B. '2009') erwartet.
         Das Ergebnis dieser Abfrage unterliegt einem serverseitigen Cache von 120
        Sekunden.
        '''
        response = self._getClient().service.GetMatchdataByGroupLeagueSaisonJSON(groupOrderID, leagueShortcut,
                                                                                 leagueSaison)
        return response

    def getMatchdataByLeagueDateTime(self, fromDateTime, toDateTime, leagueShortcut):
        ''' No.18
        Gibt eine Struktur von Sport-Spieldaten zurueck. Die Beginn-Zeit der
        ausgegebenen Spieldaten liegt zwischen den als Parameter zu
        uebergebenen DateTime-Werten. (fromDateTime <= matchBeginDateTime
        < toDateTime)Als weiterer Parameter wird der Liga-Shortcut (z.B. 'bl1')
         erwartet.
        '''
        response = self._getClient().service.GetMatchdataByLeagueDateTime(fromDateTime, toDateTime, leagueShortcut)
        return response

    def getMatchdataByLeagueSaison(self, leagueShortcut, leagueSaison):
        ''' No.19
        Gibt eine Struktur von Sport-Spieldaten aller Spiele der Liga pro Saison
        zurueck. Als Parameter werden der Liga-Shortcut (z.B. 'bl1') sowie die
        Saison (aus GetAvailLeagues, z.B. '2007') erwartet. Das Ergebnis dieser
        Abfrage unterliegt einem serverseitigen Cache von 300 Sekunden.
        '''
        response = self._getClient().service.GetMatchdataByLeagueSaison(leagueShortcut, leagueSaison)
        return response

    def getMatchdataByTeams(self, teamID1, teamID2):
        ''' No.20
        Gibt eine Struktur von Matches zurueck, bei welchen die als Parameter
        uebergebenen Teams gegeneinander spielten.
        '''
        response = self._getClient().service.GetMatchdataByTeams(teamID1, teamID2)
        return response

    def getNextMatch(self, leagueShortcut):
        ''' No.21
        Gibt eine Struktur des naechsten anstehenden Spieles der als Parameter
        zu uebergebenden Liga zurueck.
        '''
        response = self._getClient().service.GetNextMatch(leagueShortcut)
        return response

    def getNextMatchByLeagueTeam(self, leagueId, teamId):
        ''' No.22
        Gibt eine Struktur des naechsten anstehenden Spieles des als Parameter zu
        uebergebenden Teams der ebenfalODls zu uebergebenen Liga zurueck.
        '''
        response = self._getClient().service.GetNextMatchByLeagueTeam(leagueId, teamId)
        return response

    def getTeamsByLeagueSaison(self, leagueShortcut, leagueSaison):
        ''' No.23
        Gibt eine Liste aller Teams der als Parameter zu uebergebenden Liga + Saison
        zurueck.
        '''
        response = self._getClient().service.GetTeamsByLeagueSaison(leagueShortcut, leagueSaison)
        return response

    def _getClient(self):
        '''
        Wrapper method
        '''
        return Client(self.API_PATH)
