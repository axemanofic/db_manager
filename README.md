# db_manage

_A module to make it easier to use databases (sqlite and etc.)_

**`P.S. This module is recommended for educational purposes only.`**

## Features

- Decorator to simplify interaction with the database
- You only need to write SQL code and that's it

## DataBase
```mysql
create table employs
(
    id      int auto_increment
        primary key,
    fio     text          not null,
    post_id int default 0 not null,
    zp      int default 0 not null,
    constraint employs_posts_id_fk
        foreign key (post_id) references posts (id)
);

INSERT INTO databasename.employs (id, fio, post_id, zp) VALUES (1, 'Maks', 2, 5000);
INSERT INTO databasename.employs (id, fio, post_id, zp) VALUES (2, 'Кондратенко С.В.', 3, 1000000);
INSERT INTO databasename.employs (id, fio, post_id, zp) VALUES (3, 'Сотников Р.Я.', 2, 50000);
INSERT INTO databasename.employs (id, fio, post_id, zp) VALUES (4, 'Иванов И.И.', 1, 10000);
INSERT INTO databasename.employs (id, fio, post_id, zp) VALUES (5, 'Сидоров С.С.', 1, 10000);
INSERT INTO databasename.employs (id, fio, post_id, zp) VALUES (6, 'Петров П.П.', 1, 10000);


create table posts
(
    id        int auto_increment
        primary key,
    name_post varchar(50) not null
);

INSERT INTO databasename.posts (id, name_post) VALUES (0, 'Нет должности');
INSERT INTO databasename.posts (id, name_post) VALUES (1, 'Разнорабочий');
INSERT INTO databasename.posts (id, name_post) VALUES (2, 'Секретарь');
INSERT INTO databasename.posts (id, name_post) VALUES (3, 'Директор');
INSERT INTO databasename.posts (id, name_post) VALUES (4, 'Test');
INSERT INTO databasename.posts (id, name_post) VALUES (7, 'Нет должности');
```

## Examples

```python
from pyDBmanager.db_classes import SqliteDB, MysqlDB

sqlite_db = SqliteDB(db_name="DataBaseName.db")
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
    print(get_employs(), end=2 * '\n')

    print("Example of data output from parameters in sqlite: ")
    print(get_post_sqlite(1), end=2 * '\n')

    print("Example of data output from parameters in mysql: ")
    print(get_post_mysql(1), end=2 * '\n')

    print("Example of data output from parameters in mysql: ")
    print(insert_post("Test"), end=2 * '\n')

```
### Result
```shell
Example of outputting a table using prettytable: 
+----+------------------+--------------+---------+
| id |       fio        |  name_post   |    zp   |
+----+------------------+--------------+---------+
| 1  |       Maks       |  Секретарь   |   5000  |
| 2  | Кондратенко С.В. |   Директор   | 1000000 |
| 3  |  Сотников Р.Я.   |  Секретарь   |  50000  |
| 4  |   Иванов И.И.    | Разнорабочий |  10000  |
| 5  |   Сидоров С.С.   | Разнорабочий |  10000  |
| 6  |   Петров П.П.    | Разнорабочий |  10000  |
+----+------------------+--------------+---------+
--------------------------------------------------
Example of data output from parameters in sqlite: 
[(1, 'Разнорабочий')]
--------------------------------------------------
Example of data output from parameters in mysql: 
[(1, 'Разнорабочий')]
--------------------------------------------------
Example of data output from parameters in mysql: 
True
--------------------------------------------------
```

## Supports DBMS
- SQLite
- MySQL

## Feedback
For all questions write to my [telegram](https://t.me/axemanofic)