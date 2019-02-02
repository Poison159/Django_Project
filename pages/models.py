from django.db import models

# Create your models here.
class Team:
    def __init__(self,**kwargs):
        self.id             = kwargs.get('id', None)
        self.name           = kwargs.get('name', None)
        self.kasi           = kwargs.get('kasi', None)
        self.imgPath        = kwargs.get('imgPath', None)
        self.tournament_id  = kwargs.get('Tournament_id', None)
        
class Player:
    def __init__(self,**kwargs):
        self.id         = kwargs.get('id',None)
        self.name       = kwargs.get('name',None)
        self.age        = kwargs.get('age',None)
        self.position   = kwargs.get('position',None)
        self.imgPath    = kwargs.get('imgPath',None)
        self.teamId     = kwargs.get('id',None)
        self.Tournament_id  = kwargs.get('Tournament_id', None)

class Result:
    def __init__(self,**kwargs):
        self.id             = kwargs.get('id',None)
        self.homeGoals      = kwargs.get('homeGoals',None)
        self.awayGoals      = kwargs.get('awayGoals',None)
        self.fixtureId      = kwargs.get('fixtureId',None)
        self.tournament_id  = kwargs.get('tournament_id',None)

class Fixture:
    def __init__(self,**kwargs):
        self.id             = kwargs.get('id',None)
        self.stage          = kwargs.get('stage',None)
        self.homeTeam       = kwargs.get('homeTeam',None)
        self.awayTeam       = kwargs.get('awayTeam',None)
        self.date           = kwargs.get('date',None)
        self.pitch          = kwargs.get('pitch',None)
        self.tournamentId   = kwargs.get('tournamentId',None)
        self.time           = kwargs.get('time',None)
        self.fixturName     = kwargs.get('fixtureName',None)
        self.played         = kwargs.get('played',None)

class Tournament:
    def __init__(self,**kwargs):
        self.id         = kwargs.get('id',None)
        self.maxGames   = kwargs.get('maxGames',None)
        self.maxTeams   = kwargs.get('maxTeams',None)
        self.maxStages  = kwargs.get('maxStages',None)
        self.name       = kwargs.get('name',None)
