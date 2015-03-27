
create table marketorder (oid varchar(10), uid varchar(10), timestamp varchar(20), strategy varchar(20));

create table marketorderitem (id varchar(10), oid varchar(10), symbol varchar(10), price real, num int);

create table account (uid varchar(10), passwd varchar(20));

create table accountitem (uid varchar(10), symbol varchar(10), avgcost real, num int);
