from sindesi1 import get_connection

def view_games():
    connection = get_connection
    cursor = connection.cursor()
    sql="SELECT * FROM games"
    cursor.execute(sql)
    games = cursor.fetchall()

    if games:
        print("lista games")
        for game in games:
            print(f"id: {game[0]},GameName: {game[1]},year{game[2]},CompanyName{game[3]}")
    else:
        print ("den yparxoun games")
    cursor.close()
    connection.close()

view_games()