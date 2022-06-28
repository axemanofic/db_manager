create table employs
(
    id      INTEGER
        primary key autoincrement,
    fio     TEXT    not null,
    post_id INTEGER not null
        references posts,
    zp      INTEGER(15) default 0 not null
);

INSERT INTO employs (id, fio, post_id, zp) VALUES (1, 'Maks', 2, 5000);
INSERT INTO employs (id, fio, post_id, zp) VALUES (2, 'Кондратенко С.В.', 3, 1000000);
INSERT INTO employs (id, fio, post_id, zp) VALUES (3, 'Сотников Р.Я.', 2, 50000);
INSERT INTO employs (id, fio, post_id, zp) VALUES (4, 'Иванов И.И.', 1, 10000);
INSERT INTO employs (id, fio, post_id, zp) VALUES (5, 'Сидоров С.С.', 1, 10000);
INSERT INTO employs (id, fio, post_id, zp) VALUES (6, 'Петров П.П.', 1, 10000);


create table posts
(
    id        INTEGER
        primary key autoincrement,
    name_post VARCHAR(50) not null
);

INSERT INTO posts (id, name_post) VALUES (1, 'Разнорабочий');
INSERT INTO posts (id, name_post) VALUES (2, 'Секретарь');
INSERT INTO posts (id, name_post) VALUES (3, 'Директор');
INSERT INTO posts (id, name_post) VALUES (4, 'Test');