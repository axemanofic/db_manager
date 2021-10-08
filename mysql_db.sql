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