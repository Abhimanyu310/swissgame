#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("delete from matches")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("delete from records")
    c.execute("delete from players")
    db.commit()
    db.close()

def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("select count(*) from players")
    count = c.fetchone()[0];
    db.commit()
    db.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute("insert into players(name) values(%s)", (name,)) 
    db.commit()
    c.execute("select * from players where name = %s", (name,))
    result = c.fetchall()
    this_id = result[(len(result) - 1)][0]
    c.execute("insert into records(id,name,wins,played) values(%s,%s,0,0)", (this_id, name, ))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c =db.cursor()
    c.execute("select * from standings")
    result = c.fetchall()
    db.commit()
    db.close()
    return result

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c =db.cursor()
    c.execute("update records set wins=records.wins+1,played=records.played+1 where id=%s", (winner,))
    c.execute("update records set played=records.played+1 where id=%s", (loser,))
    c.execute("insert into matches(id1,id2,winner) values (%s,%s,%s)", (winner, loser, winner,))
    db.commit()
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db = connect()
    c =db.cursor()    
    c.execute("select * from standings")
    standings = c.fetchall();
    for i in range(0, len(standings), 2):
        c.execute("insert into pairings(id1,name1,id2,name2) values(%s,%s,%s,%s)", 
            (standings[i][0], standings[i][1], standings[i+1][0], standings[i+1][1],)) 
    db.commit()
    c.execute("select id1,name1,id2,name2 from pairings")
    pairs = c.fetchall()
    db.close()
    return pairs