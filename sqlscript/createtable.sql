
create table marketorder (oid varchar primary key, uid varchar, timestamp varchar, strategy varchar);

create table marketorderitem (id varchar primary key, oid varchar, symbol varchar, price real, num int);

create table account (uid varchar primary key, passwd varchar);

create table accountitem (uid varchar, symbol varchar, avgcost real, num int);
