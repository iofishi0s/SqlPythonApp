from sindesi1 import get_connection

def update_game(id,GameName=None,year=None,CompanyName=None):
    connection = get_connection()
    cursor = connection.cursor()

    updates = [] #updates = [title = %s, year = %s...]
    values =[] # values = ['book 3,2000]

    if GameName:
        updates.append("GameName = %s")
        values.append(GameName)

    if year:
        updates.append("year = %s")
        values.append(year)

    if CompanyName:
        updates.append("CompanyName = %s")
        values.append(CompanyName)

    if updates:
        sql = f"UPDATE games SET {','.join(updates)} WHERE id = %s"
        values.append(id)
        cursor.execute(sql,tuple(values))
        connection.commit()

        if cursor.rowcount > 0:
            print("To update egine")
        else:
            print("den vrethike")

    cursor.close()
    connection.close()

try:
    id = int(input("Eisagete to id an thelete na to allaksete: "))
    GameName = input("Eisagete to GameName an thelete na to allaksete: ")
    year = int(input("Eisagete to year an thelete na to allaksete: "))
    CompanyName = input("Eisagete to CompanyName an thelete na to allaksete: ")
    update_game(id,GameName or None,year or None, CompanyName or None)
except ValueError:
    print("dwse egiro id ")