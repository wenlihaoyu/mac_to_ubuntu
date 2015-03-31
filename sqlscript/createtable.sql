
create table stock_5min(symbol text ,Date text, Open real,High real ,Low real,Close real,Volume integer, Adj_close real);
create table stock_15min(symbol text ,Date text, Open real,High real ,Low real,Close real,Volume integer, Adj_close real);
create table stock_30min(symbol text ,Date text, Open real,High real ,Low real,Close real,Volume integer, Adj_close real);
create table stock_60min(symbol text ,Date text, Open real,High real ,Low real,Close real,Volume integer, Adj_close real);
create table stock_day(symbol text ,Date text, Open real,High real ,Low real,Close real,Volume integer, Adj_close real);
create table stock_week(symbol text ,Date text, Open real,High real ,Low real,Close real,Volume integer, Adj_close real);
create table stock_month(symbol text ,Date text, Open real,High real ,Low real,Close real,Volume integer, Adj_close real);
create table stock_year(symbol text ,Date text, Open real,High real ,Low real,Close real,Volume integer, Adj_close real);


create table marketorder (oid varchar primary key, uid varchar, timestamp varchar, strategy varchar);

create table marketorderitem (id varchar primary key, oid varchar, symbol varchar, price real, num int);

create table account (uid varchar primary key, passwd varchar);

create table accountitem (uid varchar, symbol varchar, avgcost real, num int);
