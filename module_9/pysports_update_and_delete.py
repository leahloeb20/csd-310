from distutils.command.config import config
import mysql.connector 
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "MYSQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def display_players(cursor,title):
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()

    print("\n  -- {} --".format(title))

    for player in players:
        print("  Player ID:  {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0],player[1],player[2],player[3]))

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    new_player = ("INSERT INTO player (first_name, last_name, team_id)" "Values('Smeagol', 'Shire Folk', 1)")

    cursor.execute(new_player)

    display_players(cursor, "-- DISPLAYING PLAYERS AFTER INSERT --")

    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    
    cursor.execute(update_player)
    
    display_players(cursor, "-- DISPLAYING PLAYERS AFTER UPDATE --")

    delete_player = ("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute(delete_player)

    display_players(cursor, "-- DISPLAYING PLAYERS AFTER DELETE --")
    
    input("\n\n Press any key to continue... ")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
        
    else:
        print(err)
finally:
    db.close()