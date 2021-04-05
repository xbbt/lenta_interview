-- Для каждого клиента выведете магазин, в котором он совершил
--первую покупку, и ее дату;

-- для каждого клиента находим первую транзакцию
with first_transactions as (
    select
        acc_id,
        min(trn_date) as first_trn_date
    from
        transactions t
    group by
        acc_id
)
-- для первых транзакций клиентов находим
-- id магазина
select
    t.acc_id,
    t.whs_id,
    t.trn_date
from
    transactions t
inner join
    first_transactions ft
on
    t.acc_id = ft.acc_id
    and t.trn_date = ft.first_trn_date;

-- Выведете клиентов, которые не посещали форматы «У Дома» и
-- «Гипермаркет» более 8 недель и формат «Авто» более 4 недель;

-- можно считать, что если клиент никогда не пользовался
-- некоторым форматом, то он его не посещал "давно" (более 8 недель)

-- для каждого пользователя находим, когда в последний
-- раз он покупал что-то в каждом формате
with last_trn_age as (
    select
        t.acc_id,
        w.frmt_name,
        age(now(), max(t.trn_date))
            as last_trn_age
    from
        transactions t
    left join
        warehouses w
    on
        t.whs_id = w.whs_id
    group by
        t.acc_id,
        w.frmt_name
),
-- находим пользователей, которые в каком-либо
-- интересующем нас формате бывали "недвано"
visited as (
    select
        distinct acc_id
    from
        last_trn_age
    where
        (frmt_name = 'У дома' or frmt_name = 'Гипермаркет')
            and last_trn_age < interval '8 weeks'
        or (frmt_name = 'Авто' and last_trn_age < interval '4 weeks')
)
-- исключаем из всех пользователей тех, кто появлялся
-- в магазинах разных форматов недавно
select
    distinct  t.acc_id
from
    transactions t
left join
    visited v
on
    t.acc_id = v.acc_id
where
    v.acc_id is null;


-- покупку каждого товара маркируем 1, если было
-- куплено от 10 единиц этого товара или
-- 0, если было куплено менее 10 единиц
with ten_or_less as (
    select
        t.acc_id,
        t.trn_id,
        case
            when p.qnty >= 10 then 1
            else 0
        end as decima
    from
        transactions t
    left join
        products p
    on
        t.trn_id = p.trn_id
),
-- находим транзакции, в которых каждый товар,
-- был куплен в количеств от 10 штук (оптовая покупка)
every_tens as (
    select
        acc_id,
        trn_id,
        count(*) = sum(decima) as every_ten
    from
        ten_or_less
    group by
        acc_id,
        trn_id
)
-- выбираем пользователей, у которых от 80% транзакций
-- были "оптовыми"
select
    acc_id
from
    every_tens
group by
    acc_id
having
    sum(every_ten::int)::float / count(*) >= 0.8;

