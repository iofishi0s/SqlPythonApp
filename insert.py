from sindesi import get_connection

def insert_book(author,publication_year,genre):
    connection = get_connection()
    cursor = connection.cursor()
    query = "insert into books(author,publication_year,genre) values"
    values = (author,publication_year,genre)
    cursor.execute(query, values)
    print("To vivlio prostethike")
    cursor.close()
    connection.close

author = input("dwse ton author: ")
publication_year=input("eisagetai etos: ")
genre=input("eiasgetai eidos: ")

insert_book(author,publication_year,genre)
