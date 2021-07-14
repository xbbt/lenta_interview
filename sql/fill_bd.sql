-- создание и заполнение таблиц для отладки задач по sql

create table warehouses (
    whs_id int PRIMARY KEY,
    frmt int,
    frmt_name varchar
);

create table transactions (
    trn_id int PRIMARY KEY ,
    acc_id int,
    whs_id int,
    trn_date timestamp,
    total float,
    foreign key (whs_id) references warehouses(whs_id)
);

create table products (
    trn_id int,
    art_id int,
    qnty float,
    value float,
    foreign key (trn_id) references transactions(trn_id)
);

alter table products add unique(trn_id, art_id);

insert into warehouses (whs_id, frmt, frmt_name)
values
       (1, 1, 'Гипермаркет'),
       (2, 1, 'Гипермаркет'),
       (3, 1, 'Гипермаркет'),
       (4, 2, 'У дома'),
       (5, 2, 'У дома'),
       (6, 3, 'Авто'),
       (7, 3, 'Авто'),
       (8, 4, 'Ларёк');

insert into transactions(trn_id, acc_id, whs_id, trn_date, total)
values
    (1, 1, 1, '2021-03-01'::timestamp, 100),
    (2, 1, 1, '2021-03-05'::timestamp, 200),
    (3, 1, 8, '2021-03-04'::timestamp, 5),
    (4, 2, 2, '2021-02-20'::timestamp, 300),
    (5, 2, 5, '2021-02-25'::timestamp, 200);


insert into transactions(trn_id, acc_id, whs_id, trn_date, total)
values
    (6, 3, 8, '2020-03-01'::timestamp, 20),
    (7, 4, 7, '2021-03-01'::timestamp, 100),
    (8, 5, 7, '2020-03-01'::timestamp, 359),
    (9, 6, 4, '2020-03-01'::timestamp, 300),
    (10, 7, 4, '2021-03-20'::timestamp, 344),
    (11, 8, 3, '2021-03-25'::timestamp, 343),
    (12, 9, 3, '2020-03-02'::timestamp, 343);

insert into transactions(trn_id, acc_id, whs_id, trn_date, total)
values
    (13, 10, 8, '2020-01-01'::timestamp, 333);

insert into products (trn_id, art_id, qnty, value)
values (1, 1, 8, 40),
       (1, 2, 10, 60),
       (2, 1, 40, 200),
       (3, 3, 10 ,5),
       (4, 4, 1, 300),
       (5, 5, 2, 200),
       (6, 6, 10 ,20),
       (7, 7, 1, 100),
       (8, 8, 100, 359),
       (9, 9, 1, 300),
       (10, 10, 1, 344),
       (11, 11, 20, 343);

insert into transactions(trn_id, acc_id, whs_id, trn_date, total)
values
    (18, 10, 1, '2021-03-01'::timestamp, 1000),
    (14, 10, 1, '2021-03-02'::timestamp, 1000),
    (15, 10, 1, '2021-03-03'::timestamp, 1000),
    (16, 10, 1, '2021-03-04'::timestamp, 1000),
    (17, 10, 1, '2021-03-05'::timestamp, 900);

insert into products(trn_id, art_id, qnty, value)
values
    (13, 100, 10, 1000),
    (14, 100, 10, 1000),
    (15, 100, 10, 1000),
    (16, 100, 10, 1000),
    (17, 100, 9, 1000);

delete from products
where trn_id = 13 and art_id = 100;

insert into products values (18, 100, 10, 1000);
insert into products values (13, 99, 111, 3);
