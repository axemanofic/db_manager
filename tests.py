from pyDBmanager.db_classes import SqliteDB, MysqlDB

sqlite_db = SqliteDB(db_name="assets/DataBaseName.db")
mysql_db = MysqlDB(db_name="databasename", username="root", password="root")


# Example of outputting a table using prettytable
# Set the 'show' flag to True and a nice sign is displayed
# If 'show' is False then a list will be returned
@mysql_db.execute_sql(show=True)
def get_employs():
    return "SELECT employs.id, employs.fio, posts.name_post, employs.zp FROM employs, posts WHERE employs.post_id = posts.id"


# Example of data output from parameters in sqlite
# Pay attention to the syntax
@sqlite_db.execute_sql()
def get_post_sqlite(id):
    return "SELECT * FROM posts WHERE id=?", (id,)


# Example of data output from parameters in mysql
# Pay attention to the syntax
@mysql_db.execute_sql()
def get_post_mysql(id):
    return "SELECT * FROM posts WHERE id=%s", (id,)


# An example of adding data to a table
@mysql_db.execute_sql()
def insert_post(name_post):
    return "INSERT INTO posts(`name_post`) VALUES (%s)", (name_post,)


if __name__ == "__main__":
    print("Example of outputting a table using prettytable: ")
    print(get_employs())
    print(10 * "-----", end='\n')

    print("Example of data output from parameters in sqlite: ")
    print(get_post_sqlite(1))
    print(10 * "-----", end='\n')

    print("Example of data output from parameters in mysql: ")
    print(get_post_mysql(1))
    print(10 * "-----", end='\n')

    print("Example of data output from parameters in mysql: ")
    print(insert_post("Test"))
    print(10 * "-----", end='\n')
