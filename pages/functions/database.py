import sqlite3
from pages.models import *

def getData():
    db          = sqlite3.connect('ProOnePal.db')
    path        = 'C:\\Users\\Other\\Downloads\\ProOnePalCSV'
    curTable    = 'Teams'
    tables      = ("Teams","Players","Fixtures","Results","Tournaments")
    MakeDb(db,path,curTable,tables)
    for table in tables:
        insertItemsIntoDb(db,path,table)
    
    cosor = db.execute('select * from '+ curTable)
    return list(cosor.fetchall())

def MakeDb(db,path,entity,tables):
        for table in tables:
                db.execute('drop table if exists ' + table)
        
        db.execute('create table Teams (id int,name text, kasi text,imgPath text,Tournament_id int)')
        db.execute('create table Players (id int,name text,age int,position text,imgPath text,teamId int)')
        db.execute('create table Fixtures (id int,stage text,homeTeam text, awayTeam text,date text,pitch text,tournamentId int,time text,fixtureName text,played text)')
        db.execute('create table Results (id int,homeGoals int,awayGoals int,fixtureId int,tournament_id int)')
        db.execute('create table Tournaments (id int,maxGames int,maxTeams int,maxStages int,name text)')
        db.commit()
        
def insertItemsIntoDb(db,path,entity):
        items = getDataFromCsv(path,entity)
        items.remove(items[0])
        if(entity == 'Teams'):
                for item in items:
                        db.execute('insert into '+entity+' (id,name,kasi,imgPath,Tournament_id) values(?,?,?,?,?)',(
                        item.id,item.name,item.kasi,item.imgPath,item.tournament_id))
                print('inserted data into teams table')
        elif(entity == 'Players'):
                for item in items:
                        db.execute('insert into '+entity+' (id,name,age,position,imgPath,teamId) values(?,?,?,?,?,?)',(
                        item.id,item.name,item.age,item.position,item.imgPath,item.teamId))
                print('inserted data into players table')
        elif(entity == 'Results'):
                for item in items:
                        db.execute('insert into '+entity+' (id,homeGoals,awayGoals,fixtureId,tournament_id) values(?,?,?,?,?)',(
                        item.id,item.homeGoals,item.awayGoals,item.fixtureId,item.tournament_id))
                print('inserted data into results table')
        elif(entity == 'Fixtures'):
                for item in items:
                        db.execute('insert into '+entity+' (id,stage,homeTeam,awayTeam,date,pitch,tournamentId,time) values(?,?,?,?,?,?,?,?)',(
                        item.id,item.stage,item.homeTeam,item.awayTeam,item.date,item.pitch,item.tournamentId,item.time))
                print('inserted data into fixtures table')

        elif(entity == 'Tournaments'):
                for item in items:
                        db.execute('insert into '+entity+' (id,maxGames,maxTeams,maxStages,name) values(?,?,?,?,?)',(
                        item.id,item.maxGames,item.maxTeams,item.maxStages,item.name))
                print('inserted data into tournaments table')
        else:
                print('Nothing Added to database')
        db.commit()

def getDataFromCsv(path,entity):
        path = path + "\\dbo." + entity + ".csv"
        fd = open(path)
        List = []
        if (entity == 'Teams'):
                for line in fd:
                        elems = line.split(',')
                        List.append(Team(id = elems[0],name = elems[1],
                        kasi = elems[2],imgPath = elems[3],tournament_id = elems[4]))
                return List                
        elif (entity == 'Players'):
                for line in fd:
                        elems = line.split(',')
                        List.append(Player(id = elems[0],name = elems[1],
                        age = elems[2],position = elems[3],imgPath = elems[4],
                        teamId = elems[5]))
                return List
        elif (entity == 'Fixtures'):
                for line in fd:
                        elems = line.split(',')
                        List.append(Fixture(id = elems[0],stage = elems[1],
                        homeTeam = elems[2],awayTeam = elems[3],date = elems[4],
                        pitch = elems[5],tournamentId = elems[6],time = elems[7],
                        fixtureName = elems[8], played = elems[9]))
                return List
        elif entity == 'Results':
                for line in fd:
                        elems = line.split(',')
                        List.append(Result(id = elems[0],homeGoals = elems[1],
                        awayGoals = elems[2],fixtureId = elems[3],tournamentId = elems[4]))
                return List
        elif entity == 'Tournaments':
                for line in fd:
                        elems = line.split(',')
                        List.append(Tournament(id = elems[0],maxGames = elems[1],
                        maxTeams = elems[2],maxSatges = elems[3],name = elems[4]))
                return List
        else:
                return List
