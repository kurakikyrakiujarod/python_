-- 数据的准备
	-- 创建一个数据库
	create database python_test charset=utf8;

	-- 使用一个数据库
	use python_test;

	-- 显示使用的当前数据是哪个?
	select database();

	-- 创建一个数据表
	-- students表
	create table students(
	    id int unsigned primary key auto_increment not null,
	    name varchar(20) default '',
	    age tinyint unsigned default 0,
	    height decimal(5,2),
	    gender enum('男','女','中性','保密') default '保密',
	    cls_id int unsigned default 0,
	    is_delete bit default 0
	);


	-- classes表
	create table classes (
	    id int unsigned auto_increment primary key not null,
	    name varchar(30) not null
	);


-- 准备数据
	-- 向students表中插入数据
	insert into students values
	(0,'小明',18,180.00,2,1,0),
	(0,'小月月',18,180.00,2,2,1),
	(0,'彭于晏',29,185.00,1,1,0),
	(0,'刘德华',59,175.00,1,2,1),
	(0,'黄蓉',38,160.00,2,1,0),
	(0,'凤姐',28,150.00,4,2,1),
	(0,'王祖贤',18,172.00,2,1,1),
	(0,'周杰伦',36,NULL,1,1,0),
	(0,'程坤',27,181.00,1,2,0),
	(0,'刘亦菲',25,166.00,2,2,0),
	(0,'金星',33,162.00,3,3,1),
	(0,'静香',12,180.00,2,4,0),
	(0,'郭靖',12,170.00,1,4,0),
	(0,'周杰',34,176.00,2,5,0);
	
	-- 向classes表中插入数据
	insert into classes values (0, "python_01期"), (0, "python_02期");


-- 查询
	-- 查询所有字段
	-- select * from 表名;
	select * from students;
	select * from classes;

	-- 查询指定字段
	-- select 列1,列2,... from 表名;
	select name, age from students;

	-- 使用 as 给字段起别名
	-- select 字段 as 名字.... from 表名;
	select name as 姓名, age as 年龄 from students;

	-- select 表名.字段 .... from 表名;
	select students.name, students.age from students;

	-- 可以通过 as 给表起别名
	-- select 别名.字段 .... from 表名 as 别名;
	select students.name, students.age from students;
	select s.name, s.age from students as s;
	-- 失败的select students.name, students.age from students as s;

	-- 消除重复行
	-- distinct 字段
	select distinct gender from students;

-- 条件查询
	-- 使用where子句对表中的数据筛选，结果为true的行会出现在结果集中
	-- where后面支持多种运算符，进行条件的处理
	-- 比较运算符
	-- 逻辑运算符
	-- 模糊查询
	-- 范围查询
	-- 空判断

-- 比较运算符
	-- 等于: =
	-- 大于: >
	-- 大于等于: >=
	-- 小于: <
	-- 小于等于: <=S
	-- 不等于: != 或 <>

	-- select .... from 表名 where .....
	-- 查询大于18岁的信息
	select * from students where age>18;
	select id,name,gender from students where age>18;

	-- 查询小于18岁的信息
	select * from students where age<18;

	-- =
	-- 查询年龄为18岁的所有学生的名字
	select * from students where age=18;

	-- != 或者 <>
	-- 查询没被删除的学生
	select * from students where is_delete=0;

	-- 查询姓名不是“黄蓉”的学生
	select * from students where name != '黄蓉';

	-- 逻辑运算符
	-- and
	-- or
	-- not

	-- and
	-- 18到28之间的所以学生信息
	select * from students where age>18 and age<28;
	-- 失败select * from students where age>18 and <28;

	-- 18岁以上的女性
	select * from students where age>18 and gender="女";
	select * from students where age>18 and gender=2;

	-- or
	-- 18以上或者身高查过180(包含)以上
	select * from students where age>18 or height>=180;

	-- not
	-- 不在18岁以上的女性 这个范围内的信息
	-- select * from students where not age>18 and gender=2;
	select * from students where not (age>18 and gender=2);

	-- 年龄不是小于或者等于18 并且是女性
	select * from students where (not age<=18) and gender=2;

	-- 模糊查询
	-- like 
	-- %表示任意多个任意字符
	-- _表示一个任意字符
	-- 查询姓名中 以 "小" 开始的名字
	select name from students where name like "小%";

	-- 查询姓名中 有 "小" 所有的名字
	select name from students where name like "%小%";

	-- 查询有2个字的名字
	select name from students where name like "__";

	-- 查询有3个字的名字
	select name from students where name like "___";

	-- 查询至少有2个字的名字
	select name from students where name like "__%";

	-- rlike 正则
	-- 查询以周开始的姓名
	select name from students where name rlike "^周.*";

	-- 查询以周开始、伦结尾的姓名
	select name from students where name rlike "^周.*伦$";

	-- 范围查询
	-- in表示在一个非连续的范围内
	-- 查询年龄为18、34、34的姓名
	select name,age from students where age=18 or age=34 or age=12;
	select name,age from students where age in (12, 18, 34);

	-- not in
	-- 年龄不是 12、18、34岁之间的信息
	select name,age from students where age not in (12, 18, 34);

	-- between ... and ...表示在一个连续的范围内
	-- 查询年龄在18到34之间的的信息
	select name, age from students where age between 18 and 34;

	-- not between ... and ...表示不在一个连续的范围内
	-- 查询 年龄不在在18到34之间的的信息
	select * from students where age not between 18 and 34;
	select * from students where not age between 18 and 34;
	-- 失败的select * from students where age not (between 18 and 34);

	-- 空判断
	-- 注意：null与''是不同的
	-- 判空is null
	-- 查询身高为空的信息
	select * from students where height is null;

	-- 判非空is not null
	select * from students where height is not null;

	-- 优先级
	-- 优先级由高到低的顺序为：小括号，not，比较运算符，逻辑运算符
	-- and比or先运算，如果同时出现并希望先算or，需要结合()使用

-- 排序
	-- order by 字段
	-- asc从小到大排列，即升序
	-- desc从大到小排序，即降序
	-- 默认按照列值从小到大排列（asc）

	-- 查询年龄在18到34岁之间的男性，按照年龄从小到到排序
	select * from students where (age between 18 and 34) and gender=1 order by age;
	select * from students where (age between 18 and 34) and gender=1 order by age asc;

	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序
	select * from students where (age between 18 and 34) and gender=2 order by height desc;

	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序, 如果身高相同的情况下按照年龄从小到大排序,
	-- 如果年龄也相同那么按照id从大到小排序
	select * from students where (age between 18 and 34) and gender=2 order by height desc,age asc,id desc;

	-- 按照年龄从小到大、身高从高到矮的排序
	select * from students order by age asc, height desc;

-- 聚合函数
	-- 总数
	-- count
	-- count(*)表示计算总行数，括号中写星与列名，结果是相同的	
	-- 查询男性有多少人，女性有多少人
	select count(*) from students where gender=1;
	select count(*) as 男性人数 from students where gender=1;
	select count(*) as 女性人数 from students where gender=2;

	-- 最大值
	-- max
	-- max(列)表示求此列的最大值
	-- 查询最大的年龄
	select age from students;
	select max(age) from students;

	-- 最小值
	-- min
	-- min(列)表示求此列的最小值
	
	-- 求和
	-- sum
	-- sum(列)表示求此列的和
	-- 计算所有人的年龄总和
	select sum(age) from students;

	-- 平均值
	-- avg
	-- avg(列)表示求此列的平均值
	-- 计算平均年龄
	select avg(age) from students;

	-- 计算平均年龄 sum(age)/count(*)
	select sum(age)/count(*) from students;

	-- 四舍五入 round(123.23 , 1) 保留1位小数
	-- 计算所有人的平均年龄，保留2位小数
	select round(sum(age)/count(*), 2) from students;

	-- 计算男性的平均身高 保留2位小数
	select round(avg(height), 2) from students where gender=1;
	-- 错误 select name, round(avg(height), 2) from students where gender=1;

-- 分组
	-- group by
	-- group by的含义:将查询结果按照1个或多个字段进行分组，字段值相同的为一组
	-- group by可用于单个字段分组，也可用于多个字段分组
	-- 按照性别分组,查询所有的性别
	-- select name from students group by gender;
	-- select * from students group by gender;
	select gender from students group by gender;
	-- 根据gender字段来分组，gender字段的全部值有4个'男','女','中性','保密'，所以分为了4组 
	-- 当group by单独使用时，只显示出每组的第一条记录, 所以group by单独使用时的实际意义不大

	-- group by + group_concat()
	-- group_concat(字段名)可以作为一个输出字段来使用
	-- 表示分组之后，根据分组结果，使用group_concat()来放置每一组的某字段的值的集合
	-- 查询同种性别中的姓名
	select gender,group_concat(name) from students where gender=1 group by gender;
	select gender,group_concat(name, age, id) from students where gender=1 group by gender;
	select gender,group_concat(name, "_", age, " ", id) from students where gender=1 group by gender;

	-- group by + 集合函数
	-- 通过group_concat()的启发，我们既然可以统计出每个分组的某字段的值的集合
	-- 那么我们也可以通过集合函数来对这个值的集合做一些操作
	select gender,avg(age) from students group by gender;

	-- 分别统计性别为男/女的人的个数
	select gender,count(*) from students group by gender;

	-- 计算男性的人数
	select gender,count(*) from students where gender=1 group by gender;

	-- group by + having
	-- having 条件表达式：用来分组查询后指定一些条件来输出查询结果
	-- having作用和where一样，但having只能用于group by
	-- 查询平均年龄超过30岁的组，显示性别，以及姓名，平均年龄
	select gender, group_concat(name),avg(age) from students group by gender having avg(age)>30;

	-- 查询每种性别中的人数多于2个的信息
	select gender, group_concat(name) from students group by gender having count(*)>2;

	-- group by + with rollup
	-- with rollup的作用是：在最后新增一行，来记录当前列里所有记录的总和
	select gender,count(*) from students group by gender with rollup;
	select gender,group_concat(age) from students group by gender with rollup;

-- 分页
	-- limit start, count
	-- 从start开始，获取count条数据

	-- 限制查询出来的数据个数
	select * from students where gender=1 limit 2;

	-- 查询前5个数据
	select * from students limit 0, 5;

	-- 查询id 6-10（包含）的书序
	select * from students limit 5, 5;

	-- 每页显示2个，第1个页面
	select * from students limit 0,2;

	-- 每页显示2个，第2个页面
	select * from students limit 2,2;

	-- 每页显示2个，第3个页面
	select * from students limit 4,2;

	-- 每页显示2个，第4个页面
	select * from students limit 6,2; -- -----> limit (第N页-1)*每个的个数, 每页的个数;

	-- 每页显示2个，显示第6页的信息, 按照年龄从小到大排序
	-- 失败select * from students limit 2*(6-1),2;
	-- 失败select * from students limit 10,2 order by age asc;
	select * from students order by age asc limit 10,2;

	select * from students where gender=2 order by height desc limit 0,4;

-- 连接查询
	-- 当查询结果的列来源于多张表时，需要将多张表连接成一个大的数据集，再选择合适的列返回

	-- 内连接查询：查询的结果为两个表匹配到的数据
	-- inner join ... on
	-- select ... from 表A inner join 表B;
	select * from students inner join classes;

	-- 查询有能够对应班级的学生以及班级信息
	select * from students inner join classes on students.cls_id=classes.id;

	-- 按照要求显示姓名、班级
	select students.*, classes.name from students inner join classes on students.cls_id=classes.id;

	-- 给数据表起名字
	select s.name, c.name from students as s inner join classes as c on s.cls_id=c.id;

	-- 查询有能够对应班级的学生以及班级信息，显示学生的所有信息，只显示班级名称
	select s.*, c.name from students as s inner join classes as c on s.cls_id=c.id;

	-- 在以上的查询中，将班级名字显示在第1列
	select c.name, s.* from students as s inner join classes as c on s.cls_id=c.id;

	-- 查询有能够对应班级的学生以及班级, 班级显示名字，学生显示所有信息，按照班级名字进行排序
	-- select c.xxx s.xxx from student as s inner join clssses as c on .... order by ....
	select c.name, s.* from students as s inner join classes as c on s.cls_id=c.id order by c.name;

	-- 当同一个班级的时候，按照学生的id进行从小到大排序
	select c.name, s.* from students as s inner join classes as c on s.cls_id=c.id order by c.name,s.id;

	-- left join
	-- 查询每位学生对应的班级信息
	select * from students as s left join classes as c on s.cls_id=c.id;

	-- 查询没有对应班级信息的学生
	-- select ... from xxx as s left join xxx as c on..... where .....
	-- select ... from xxx as s left join xxx as c on..... having .....
	select * from students as s left join classes as c on s.cls_id=c.id having c.id is null;
	-- select * from students as s left join classes as c on s.cls_id=c.id where c.id is null;

	-- right join   on
	-- 将数据表名字互换位置，用left join完成


-- 子查询
	-- 在一个 select 语句中,嵌入了另外一个 select 语句, 那么被嵌入的 select 语句称之为子查询语句
	-- 主查询
	-- 主要查询的对象，第一条 select 语句
	-- 主查询和子查询的关系
	-- 子查询是嵌入到主查询中
	-- 子查询是辅助主查询的,要么充当条件,要么充当数据源
	-- 子查询是可以独立存在的语句,是一条完整的 select 语句

	-- 子查询分类
	-- 标量子查询: 子查询返回的结果是一个数据(一行一列)
	-- 列子查询: 返回的结果是一列(一列多行)
	-- 行子查询: 返回的结果是一行(一行多列)

	-- 标量子查询
	-- 1.查询班级学生平均年龄
	-- 2.查询大于平均年龄的学生
	select * from students where age > (select avg(age) from students);
	
	-- 列级子查询
	-- 查询所有学生所在班的班级名字
	-- 1.找出学生表中所有的班级 id
	-- 2.找出班级表中对应的名字
	select name from classes where id in (select cls_id from students);

	-- 查询学生的班级号能够对应的学生信息
	select * from students where cls_id in (select id from classes);

-- 	行级子查询
	-- 需求: 查找班级年龄最大,身高最高的学生
	-- 行元素: 将多个字段合成一个行元素,在行级子查询中会使用到行元素
	select * from students where (height,age) = (select max(height),max(age) from students);


-- 总结

	-- 查询的完整格式
	-- SELECT select_expr [,select_expr,...] [      
	--       FROM tb_name
	--       [WHERE 条件判断]
	--       [GROUP BY {col_name | postion} [ASC | DESC], ...] 
	--       [HAVING WHERE 条件判断]
	--       [ORDER BY {col_name|expr|postion} [ASC | DESC], ...]
	--       [ LIMIT {[offset,]rowcount | row_count OFFSET offset}]
	-- ]

	-- 完整的select语句
	-- select distinct *
	-- from 表名
	-- where ....
	-- group by ... having ...
	-- order by ...
	-- limit start,count

	-- 执行顺序为：
	-- from 表名
	-- where ....
	-- group by ...
	-- select distinct *
	-- having ...
	-- order by ...
	-- limit start,count
	-- 实际使用中，只是语句中某些部分的组合，而不是全部