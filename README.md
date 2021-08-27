# db_manage
---
_A module to make it easier to use databases (sqlite and etc.)_
**`P.S. This module is recommended for educational purposes only.`**

## Features
---
- Decorator to simplify interaction with the database
- You only need to write SQL code and that's it

## Examples
```python
from db_manager import SqliteDB

db = SqliteDB('DataBaseName.db')


@db.select_all
def get_posts():
    return "SELECT * FROM posts"


@db.select_one
def get_post(id):
    return "SELECT * FROM posts WHERE id=?", (id,)


@db.update_or_delete_or_insert
def insert_post(name_post):
    return "INSERT INTO posts(`name_post`) VALUES (?)", (name_post,)


if __name__ == "__main__":
    print("Get all records in DB: ", get_posts())
    print("Get one records in DB: ", get_post(1))
    print("Insert one records in DB: ", insert_post("Test"))
```
### Result
```sh
Get all records in DB:  [(1, 'Разнорабочий'), (2, 'Секретарь'), (3, 'Директор')]
Get one records in DB:  (1, 'Разнорабочий')
Insert one records in DB:  True
```

## Supports DBMS
- SQLite

## Feedback
For all questions write to my [telegram](https://t.me/axemanofic)