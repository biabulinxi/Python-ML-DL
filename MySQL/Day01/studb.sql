create database studb;
use studb;
create table stuInfo(id int,name char(10),age tinyint unsigned,height float(5,2),weight (6,3));
desc stuInfo;
show create table stuInfo;
insert into stuInfo values(1, 'Jack',10,121.34,182.234);
insert into stuInfo(id,name) values(2,'Rose'),(3,'liming');
select * from stuInfo;
select id,name from stuInfo;
											   

