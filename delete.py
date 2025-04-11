from connection import get_connection

def delete_game(id):
    connection = get_connection()
    cursor = connection.cursor()
    sql = "DELETE FROM games WHERE id = %s"
    cursor.execute(sql,(id,))
    connection.commit()

    if cursor.rowcount > 0:
        print ("diagraftike ")
    else: 
        print ("den vrethike ")

    cursor.close()
    connection.close()

try:
    id = int(input("eisagete to id: "))
    delete_game(id)
except ValueError:
    print ("Den vrethike egiro id ")