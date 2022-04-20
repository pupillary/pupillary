-- SQL语句单行注释
-- 创建表格 
-- ;表示结束
-- varchar 字符串
CREATE TABLE stu(
	stu_no int(10) PRIMARY KEY auto_increment,
	name varchar(30) not null,
	gender int(10) not null,
	birthday date,
	addresss varchar(255)
);


-- 1. 增加数据
-- insert into table_name(列名1, 列名2, 列名3.....) values (值1, 值2, 值3,.....)
insert into men(name, age, address) values ("alex", 18, "八宝山");
insert into men(name, age, address) values("tory", "19", "八宝山");


-- 2. 删除数据
-- delete from table_name    全表删除
-- delete from table_name where条件  带条件删除
delete from men where id = 1;  
delete from men where name = 'tory';
delete from men;


-- 3. 修改数据
-- update table_name set 列名1=值1, 列名2 = 值2.... where条件
-- 把alex的住址修改到鸡冠山
update men set address='鸡冠山', age=99 where id = 5;


-- 4. 查询数据 
-- 查询的基本语句
-- select *|列名1, 列名2, 列名3..... from table_name
select * from men;
select name as `名字`, address as `住址` from men;

-- where条件
-- where 列 = 值
select * from men where name = 'alex';

-- 查询住在八宝山第一栋的, 年龄是25的人的信息
select * from men where address = '八宝山第一栋' and age = 25;
select * from men where address = '八宝山第一栋' or age = 25;
-- 非
-- 查询不住在八宝山第一栋的人的信息   != 不等于
select * from men where address != '八宝山第一栋';

-- 大于  >   小于  < , >= <=, =
select * from men where age >= 25;

-- between xxx and xxxx  
select * from men where age between 23 and 25;

-- 有意思的, 模糊搜索, like 
select * from men where name like '张%';
-- 查询住址有`宝山`
select * from men where address like '%宝山%';


-- 分组查询
-- group by  分组. 在执行的时候, 会根据by后面给出的列进行分组(相同数据分为一组)
-- 统计每个班级的语文平均成绩
-- 所有的数据都在一张表里. 
-- select 班级名称, avg(成绩) from 表 where 课 = '语文' group by 班级;
-- 查询各个 住所 的人的  平均年龄
select address, avg(age) from men group by address;

-- 聚合函数
-- avg(), 平均值
-- sum(), 求和
-- min(), 最小值
-- max(), 最大值
-- count(), 计数
-- 查询每个住址中最大年龄和最小年龄,以及平均年龄
select address, max(age), min(age), avg(age) from men group by address;
-- 查询每个住址中平均年龄大于20岁的住址以及平均年龄
-- having 在分组, 计算聚合函数之后. 在进行进一步的数据筛选

-- 计算机专业的数据库考试必考题
select address, avg(age) from men group by address having avg(age) > 20;








insert into men(name, age, address) values("tory1", "19", "八宝山第一栋");
insert into men(name, age, address) values("tory2", "20", "八宝山第二栋");
insert into men(name, age, address) values("tory3", "21", "八宝山第二栋");
insert into men(name, age, address) values("tory4", "22", "八宝山第二栋");
insert into men(name, age, address) values("tory5", "23", "八宝山第二栋");
insert into men(name, age, address) values("tory6", "24", "八宝山第一栋");
insert into men(name, age, address) values("tory7", "25", "八宝山第一栋");
insert into men(name, age, address) values("tory8", "25", "八宝山第一栋");
insert into men(name, age, address) values("tory9", "24", "八宝山第一栋");





