-- acct.sql
-- 创建表，插入数据
create table acct(
  acct_no varchar(32) primary key,
  acct_name varchar(64) not null,
  reg_date date,
  acct_type int,
  balance decimal(18,2)
);

insert into acct values(
  '622345000001','Jerry',now(),1,1100
);

insert into acct values(
  '622345000002','Tom',now(),1,2000
);

insert into acct values(
  '622345000003','Rose',now(),1,3000
),('622345000004','Jack',now(),1,4000);