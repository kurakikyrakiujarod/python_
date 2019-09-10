### 一、库的操作

1、系统数据库

执行如下命令，查看系统库

```
show databases;
```

**information_schema**： 虚拟库，不占用磁盘空间，存储的是数据库启动后的一些参数，如用户表信息、列信息、权限信息、字符信息等

**performance_schema**： MySQL 5.5开始新增一个数据库：主要用于收集数据库服务器性能参数，记录处理查询请求时发生的各种事件、锁等现象

**mysql**： 授权库，主要存储系统用户的权限信息

**sys**:   通过这个库可以快速的了解系统的元数据信息。sys库里这些视图中的数据，都是从information_schema里面获得的，目标是把performance_schema的把复杂度降低，让DBA能更好的阅读这个库里的内容。让DBA更快的了解DB的运行情况

2、创建数据库

求救语法

```
help create database;
```

创建数据库语法

```
CREATE DATABASE 数据库名 charset utf8;
```

### 二、表的操作

1、存储引擎

**存储引擎** : 其实就是指定 **表** 如何**存储数据**，如何为存储的数据 **建立索引** 以及 **如何更新**，**查询数据**等技术实现的方法。因为在关系数据库中数据的存储是以表的形式存储的，所以存储引擎也可以称为表类型（即存储和操作此表的类型）

在Oracle 和SQL Server等数据库中只有一种存储引擎，所有数据存储管理机制都是一样的。而MySql数据库提供了多种存储引擎。用户可以根据不同的需求为数据表选择不同的存储引擎，用户也可以根据自己的需要编写自己的存储引擎。

![](https://i.loli.net/2018/11/18/5bf044c6da563.png)

其中最常见的两种存储引擎是**MyISAM 和 InnoDB**

查看所有支持的引擎

```
 show engines;
```

查看正在使用的存储引擎

```
show variables like '%storage_engine%';
```

**几大数据库引擎介绍**

INNODB存储引擎

（1）MySQL默认存储引擎(MySQL 5.5 版本后)

（2）innodb 支持事务，回滚以及系统崩溃修复能力和多版本迸发控制的事务的安全

（3）innodb 支持自增长列（auto_increment）,自增长列的值不能为空，(一个表只允许存在一个自增,并且要求自增列必须为索引)

（4）innodb 支持外键（foreign key） ,外键所在的表称为子表,而所依赖的表称为父表

（5）innodb存储引擎支持行级锁

（6）innodb存储引擎索引使用的是B+Tree

补充3点：

1.大容量的数据集时趋向于选择Innodb。因为它支持事务处理和故障的恢复。Innodb可以利用数据日志来进行数据的恢复。主键的查询在Innodb也是比较快的。

2.大批量的插入语句时（这里是INSERT语句）在MyIASM引擎中执行的比较的快，但是UPDATE语句在Innodb下执行的会比较的快，尤其是在并发量大的时候。

 3.两种引擎所使用的索引数据结构是什么？

MyIASM引擎，B+树的数据结构中存储的内容实际上是实际数据的地址值。也就是说它的索引和实际数据是分开的，只不过使用索引指向了实际数据。这种索引的模式被称为非聚集索引。

Innodb引擎的索引的数据结构也是B+树，只不过数据结构中存储的都是实际的数据，这种索引有被称为聚集索引。



### 三、Python操作MySQL

pymsql是Python中操作MySQL的模块

**下载安装**

```
pip3 install pymysql -i https://pypi.douban.com/simple
```



**防止sql注入**

```python
from pymysql import connect

username = input('username:')
password = input('password:')

# 创建连接
conn = connect(host='localhost',user='root',password='123123',database='666')
# 获取游标
cursor = conn.cursor()

sql = "select * from userinfo where username=%s and password=%s"
# print(sql)
# 执行sql
# 使用pymysql提供的execute方法,不要自己拼接sql语句，防止用户sql注入
cursor.execute(sql,[username,password])
print(cursor.fetchone())

# 关闭游标
cursor.close()
# 关闭连接
conn.close()
```

**使用操作**

```python
# -*- coding:utf-8 -*-
import pymysql
  
# 创建连接
conn = pymysql.connect(host='localhost', user='root', 
                       password='123123', database='666')
# 创建游标
cursor = conn.cursor()
  
# 执行SQL，并返回收影响行数
effect_row = cursor.execute("update userinfo set password = '111222'")
  
# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update userinfo set password = '121212' where id > %s", (1,))
  
# 执行SQL，并返回受影响行数
# effect_row = cursor.executemany("insert into userinfo(username,password) values(%s,%s)",
#                                 [("kara", '222333'), ("CLARA", '121212')])
  
  
# 增删改需要commit，不然无法保存新建或者修改的数据
conn.commit()
  
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
```

**获取新创建数据自增ID**

**获取查询数据**

```python
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123123', db='666')
cursor = conn.cursor()
cursor.execute("select * from userinfo")

# 获取第一行数据
row_1 = cursor.fetchone()
# print(row_1)

# 获取前n行数据
row_2 = cursor.fetchmany(3)
# print(row_2)

# 获取所有数据
row_3 = cursor.fetchall()
# print(row_3)

conn.commit()
cursor.close()
conn.close()
```

在fetch数据时按照顺序进行，可以使用cursor.scroll(num,mode)来移动游标位置

```
cursor.scroll(1, mode='relative')  # 相对当前位置移动
cursor.scroll(2, mode='absolute')  # 相对绝对位置移动
```

**fetch数据类型**

```python
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123123', db='666')

# 游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
r = cursor.execute("select * from userinfo;")

result = cursor.fetchone()
print(result)

conn.commit()
cursor.close()
conn.close()
```

**临时表**

左右连表： join

上下连表： union

```
union 自动去重
select 字段,字段 from 表
union
select 字段,字段 from 表;

UNION ALL 不去重
select 字段,字段 from 表
UNION ALL
select 字段,字段 from 表;
```

**视图**

视图是一个虚拟表（非真实存在），其本质是根据SQL语句获取动态的数据集，并为其命名，用户使用时只需使用名称即可获取结果集，并可以将其当作表来使用。

**临时表搜索**

```
SELECT
    *
FROM
    (
        SELECT
            id,
            name
        FROM
            tb1
        WHERE
            id > 2
    ) AS A
WHERE
    A.NAME like '%a%';
```



```
创建视图
create view 视图名称  as sql 查询语句;

使用视图
select * from 视图名称;

更新视图
alter view 视图名称 AS SQL语句;

删除视图
drop view 视图名称;
```

**触发器**

对某个表进行 增/删/改操作的前后如果希望触发某个特定的行为时，可以使用触发器，触发器用于定制用户对表的行进行增/删/改前后的行为。

**创建基本语法**

```
-- 插入前
CREATE TRIGGER 触发器名称 BEFORE INSERT ON 表 FOR EACH ROW
BEGIN
    ...
END

-- 插入后
CREATE TRIGGER 触发器名称 AFTER INSERT ON 表 FOR EACH ROW
BEGIN
    ...
END

-- 删除前
CREATE TRIGGER 触发器名称 BEFORE DELETE ON 表 FOR EACH ROW
BEGIN
    ...
END

-- 删除后
CREATE TRIGGER 触发器名称 AFTER DELETE ON 表 FOR EACH ROW
BEGIN
    ...
END

-- 更新前
CREATE TRIGGER 触发器名称 BEFORE UPDATE ON 表 FOR EACH ROW
BEGIN
    ...
END

-- 更新后
CREATE TRIGGER 触发器名称 AFTER UPDATE ON 表 FOR EACH ROW
BEGIN
    ...
END
```



```
-- NEW表示即将插入的数据行，OLD表示即将删除的数据行
-- 默认情况下，mysql语句是以分号来作为结束符的
-- 通过delimiter命令，可以修改结束符

delimiter //
CREATE TRIGGER tri_bef_ins_tb1 BEFORE INSERT ON tb1 FOR EACH ROW
BEGIN
    insert into class values(0,NEW.name);
END //
delimiter ;

delimiter //
CREATE TRIGGER tri_aft_del_tb1 AFTER DELETE ON tb1 FOR EACH ROW
BEGIN
    insert into class values(0,OLD.name);
END //
delimiter ;
```

**删除触发器**

```
DROP TRIGGER 触发器名称;
```

**使用触发器**

触发器无法由用户直接调用，而知由于对表的增/删/改操作被动引发的



### 函数

**内置函数**

```
CHAR_LENGTH(str)
-- 返回值为字符串str 的长度，长度的单位为字符。一个多字节字符算作一个单字符。
-- 对于一个包含五个二字节字符集, LENGTH()返回值为 10, 而CHAR_LENGTH()的返回值为5。

CONCAT(str1,str2,...)
-- 字符串拼接
-- 如有任何一个参数为NULL ，则返回值为 NULL。

CONCAT_WS(separator,str1,str2,...)
字符串拼接（自定义连接符）
CONCAT_WS()不会忽略任何空字符串。 (然而会忽略所有的 NULL）。

CONV(N,from_base,to_base)
进制转换
SELECT CONV('a',16,2); -- 表示将 a 由16进制转换为2进制字符串表示

FORMAT(X,D)
将数字X 的格式写为'#,###,###.##',以四舍五入的方式保留小数点后 D 位， 并将结果以字符串的形式返回。
若 D 为 0, 则返回结果不带有小数点，或不含小数部分。
SELECT FORMAT(12332.1,4); -- 结果为： '12,332.1000'

INSERT(str,pos,len,newstr)
在str的指定位置插入字符串
pos：要替换位置起始位置
len：替换的长度
newstr：新字符串
如果pos超过原字符串长度，则返回原字符串
如果len超过原字符串长度，则由新字符串完全替换

......

-- 执行函数 
select CURDATE();
```

**时间和日期函数**

<a href="https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html#function_date-format">官方文档</a>

```
-- 简单示例
SELECT DATE_FORMAT('1999-01-01', '%X %V');
```

**自定义函数**

```mysql
delimiter //
create function f1(
    i1 int,
    i2 int)
returns int
BEGIN
    declare num int;
    set num = i1 + i2;
    return(num);
END //
delimiter ;

--运行报错

-- ERROR 1418 (HY000): This function has none of DETERMINISTIC, NO SQL, or READS SQL ---- DATA in its declaration and binary logging is enabled (you might want to use the ----- less safe log_bin_trust_function_creators variable)
```

<a href="https://www.jb51.net/article/97037.htm">mysql 报错This function has none of DETERMINISTIC解决方案</a>

```mysql
show variables like 'log_bin_trust_function_creators';
-- +---------------------------------+-------+
-- | Variable_name                   | Value |
-- +---------------------------------+-------+
-- | log_bin_trust_function_creators | OFF   |
-- +---------------------------------+-------+

set global log_bin_trust_function_creators=1;
show variables like 'log_bin_trust_function_creators';
-- +---------------------------------+-------+
-- | Variable_name                   | Value |
-- +---------------------------------+-------+
-- | log_bin_trust_function_creators | ON    |
-- +---------------------------------+-------+
```

**执行函数**

```
SELECT f1(1,100);
```

**删除函数**

```
SELECT f1(1,100);
```

**存储过程**

**无参数存储过程**

```mysql
-- 定义存储过程
delimiter //
create procedure p1 ()
begin
    select * from class;  
    insert into class values(0,'我是存储过程');
end //
delimiter ;

-- 调用
call p1();
```

**pymysql调用存储过程**

```python
# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, 
                       user='root', passwd='123123', db='666',charset='utf8')

# 游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 调用存储过程
cursor.callproc('p1')

result = cursor.fetchall()
print(result)

conn.commit()
cursor.close()
conn.close()

```

**对于存储过程，可以接收参数，其参数有三类**

**参数in**

```mysql
-- in、out、inout
delimiter //
create procedure p2(
    in n1 int,
    in n2 int
    )
BEGIN
	select * from student where sid > n1;
END //
delimiter ;

-- mysql中调用
call p2(12,2)    

-- pymysql中调用 
-- cursor.callproc('p2',(12,2)) 
```

**参数out**

```mysql
delimiter //
create procedure p3(
    in n1 int,
    out n2 int
    )
BEGIN
	set n2 = 123123;
	select * from student where sid > n1;
END //
delimiter ;

set @v1 = 10;
call p3(12,@v1);
select @v1;

set @_p3_0 = 12;
set @_p3_1 = 2;
call p3(@_p3_0,@_p3_1);
select @_p3_0,@_p3_1;

-- mysql中调用
-- 结果集
-- cursor.callproc('p3',(12,2))
-- r1 = cursor.fetchall()
-- print(r1)

-- out值
-- cursor.execute('select @_p3_0,@_p3_1')
-- r2 = cursor.fetchall()
-- print(r2)
```

为什么有结果集又有out伪造的返回值？

一般用于标识存储过程的执行结果

**事务**

```mysql
delimiter \\
CREATE PROCEDURE p5 ( OUT p_return_code TINYINT ) BEGIN
	DECLARE
		EXIT HANDLER FOR SQLEXCEPTION BEGIN -- ERROR
			
			SET p_return_code = 1;
		ROLLBACK;
		
	END;
	START TRANSACTION;
	DELETE 
	FROM
		tb1;
	INSERT INTO tb2 ( NAME )
	VALUES
		( 'seven' );
	COMMIT; -- SUCCESS
	
	SET p_return_code = 2;
	
END \\ 
delimiter;
    
set @temp = 10;
CALL p5(@temp);
SELECT @temp;
```

**游标**

```mysql
-- 创建表A
create table A(
	id int not null auto_increment primary key,
	 num int(10)
	 );
	 
-- 创建表B	 
create table B(
	id int not null auto_increment primary key,
	number int(10)
	);
	
-- 插入三条数据	
insert into A values(0,99),(0,98),(0,97);

-- 定义
delimiter //
	create procedure p6()
	begin 
		declare row_id int; -- 自定义变量1  
		declare row_num int; -- 自定义变量2 
		declare done INT DEFAULT FALSE;
		declare temp int;
		
		declare my_cursor CURSOR FOR select id,num from A;
		declare CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;		
		
		open my_cursor;
			xxoo: LOOP
				fetch my_cursor into row_id,row_num;
				if done then 
					leave xxoo;
				END IF;
				set temp = row_id + row_num;
				insert into B(number) values(temp);
			end loop xxoo;
		close my_cursor;
						
end  //
delimter ;

-- 调用
CALL p6();

-- 删除存储过程
DROP PROCEDURE p6;
```

**动态执行防止sql注入**



### 索引

索引，是数据库中专门用于帮助用户快速查询数据的一种数据结构。类似于字典中的目录，查找字典内容时可以根据目录查找到数据的存放位置，然后直接获取即可。

MySQL中常见索引有：

**普通索引**：加速查找

```mysql
create table 表(
    nid int not null auto_increment primary key,
    name varchar(32) not null,
    email varchar(64) not null,
    index 索引名(字段)
); -- 创建表 + 索引

create index 索引名 on 表(字段) -- 创建索引

drop index 索引名 on 表; -- 删除索引

show index from 表; -- 查看索引

```

**唯一索引**：加速查找 + 唯一约束(不能重复，可含null)

```mysql
create table 表(
    nid int not null auto_increment primary key,
    name varchar(32) not null,
    email varchar(64) not null,
    extra text,
    unique 索引名(字段)
); -- 创建表 + 唯一索引

create unique index 索引名 on 表名(列名); -- 添加
drop index 索引名 on 表名;  -- 删除
ALTER TABLE `table_name` ADD UNIQUE ( `column` ); -- 添加
ALTER TABLE `table_name` DROP INDEX `column`;    -- 删除
```

**主键索引**：加速查找 + 不能为空 + 不能重复

**联合索引**（多列）：联合索引是将n个列组合成一个索引

```mysql
create index 索引名 on 表(列,列);
```

- 联合主键索引

- 联合唯一索引

- 联合普通索引


**准备300w条数据：**

```mysql
 -- 准备表
 create table userinfo(
 	id int not null auto_increment primary key,
 	name varchar(20),
 	email varchar(50),
 	gender char(6)
 	);
 	
-- 创建存储过程，实现批量插入300万条记录
delimiter $$ -- 声明存储过程的结束符号为$$
create procedure auto_insert1()
BEGIN
    -- 设置变量1，默认值为1
    declare i int default 1;
    while(i<=3000000)do
       -- concat，字符串拼接。当i为1时，那么concat('alex',i)表示为alex1
        insert into userinfo values(0,concat('alex',i),'male',concat('egon',i,'@oldboy'));
        set i=i+1;
    end while;
END$$ -- $$结束
delimiter ; -- 重新声明分号为结束符号

-- 查看存储过程
show create procedure auto_insert1\G 

-- 调用存储过程
call auto_insert1();

-- !!! 这种方式插入300万条数据慢
```

**利用python脚本，使用协程插入300万条数据**

```python
# coding: utf-8
import pymysql
import gevent
import time


class MyPyMysql:
    def __init__(self, host, port, username, password, db, charset='utf8'):
        self.host = host  # mysql主机地址
        self.port = port  # mysql端口
        self.username = username  # mysql远程连接用户名
        self.password = password  # mysql远程连接密码
        self.db = db  # mysql使用的数据库名
        self.charset = charset  # mysql使用的字符编码,默认为utf8
        self.pymysql_connect()  # __init__初始化之后，执行的函数

    def pymysql_connect(self):
        # pymysql连接mysql数据库
        # 需要的参数host,port,user,password,db,charset
        self.conn = pymysql.connect(host=self.host,
                                    port=self.port,
                                    user=self.username,
                                    password=self.password,
                                    db=self.db,
                                    charset=self.charset
                                    )
        # 连接mysql后执行的函数
        self.asynchronous()

    def run(self, nmin, nmax):
        # 创建游标
        self.cur = self.conn.cursor()

        # 定义sql语句,插入数据id,name,gender,email
        sql = "insert into userinfo(name,gender,email) values (%s,%s,%s)"

        # 定义总插入行数为一个空列表
        data_list = []
        for i in range(nmin, nmax):
            # 添加所有任务到总的任务列表
            result = ('alex' + str(i), 'male', 'egon' + str(i) + '@oldboy')
            data_list.append(result)

        # 执行多行插入，executemany(sql语句,数据(需一个元组类型))
        content = self.cur.executemany(sql, data_list)
        if content:
            print('成功插入第{}条数据'.format(nmax - 1))

        # 提交数据,必须提交，不然数据不会保存
        self.conn.commit()

    def asynchronous(self):
        # g_l 任务列表
        # 定义了异步的函数: 这里用到了一个gevent.spawn方法
        max_line = 10000  # 定义每次最大插入行数(max_line=10000,即一次插入10000行)
        g_l = [gevent.spawn(self.run, i, i + max_line)
               for i in range(1, 3000001, max_line)]

        # gevent.joinall 等待所以操作都执行完毕
        gevent.joinall(g_l)
        self.cur.close()  # 关闭游标
        self.conn.close()  # 关闭pymysql连接


if __name__ == '__main__':
    start_time = time.time()  # 计算程序开始时间
    st = MyPyMysql('localhost', 3306, 'root', '123123', 'db1')  # 实例化类，传入必要参数
    print('程序耗时{:.2f}'.format(time.time() - start_time))  # 计算程序总耗时

```

**测试**

```mysql
-- 无索引查找
select * from userinfo where name='alex1990000';
-- +---------+-------------+--------------------+--------+
-- | id      | name        | email              | gender |
-- +---------+-------------+--------------------+--------+
-- | 1990000 | alex1990000 | egon1990000@oldboy | male   |
-- +---------+-------------+--------------------+--------+
-- 1 row in set (1.10 sec)

-- 通过主键索引查找
select * from userinfo where id=1990000;
-- +---------+-------------+--------------------+--------+
-- | id      | name        | email              | gender |
-- +---------+-------------+--------------------+--------+
-- | 1990000 | alex1990000 | egon1990000@oldboy | male   |
-- +---------+-------------+--------------------+--------+
-- 1 row in set (0.00 sec)

-- 创建索引
create index ix_name on userinfo(name);

-- 根据索引查找
select * from userinfo where name='alex1990000';
-- +---------+-------------+--------------------+--------+
-- | id      | name        | email              | gender |
-- +---------+-------------+--------------------+--------+
-- | 1990000 | alex1990000 | egon1990000@oldboy | male   |
-- +---------+-------------+--------------------+--------+
-- 1 row in set (0.01 sec)
```

无索引：从前到后依次查找 ，索引：创建额外文件(某种格式存储)，加速查找

索引种类（某种格式存储）：hash索引（单值快、范围查找慢）、 btree索引（二叉树，应用广）

建立索引：a. 额外的文件保存特殊的数据结构 b. 查询快，插入更新删除慢 c. 需要命中索引生效

覆盖索引：在索引文件中直接获取数据

```mysql
select id from userinfo where name = 1990000;
```

索引合并：把多个单列索引合并使用

```mysql
select * from userinfo where name = 'alex1990000' and id = 1990000;
```

联合索引效率 高于索引合并，但组合索引需要遵循最左前缀匹配 

**最左前缀匹配**

```mysql

create index ix_name_email on userinfo(name,email); -- 创建组合索引，name和email组合

select * from userinfo where name = 'alex';
select * from userinfo where name = 'alex' and email='alex@oldBody';
select * from userinfo where  email='alex@oldBody';

-- name和email组合索引之后，查询：
-- （1）name        ---使用索引
-- （2）name和email ---使用索引
-- （3）email       ---不使用索引
```

**正确使用索引**

数据库表中添加索引后确实会让查询速度起飞，但前提必须是正确的使用索引来查询，如果以错误的方式使用，则即使建立索引也会不奏效。

```mysql
-- like '%xx'
select * from userinfo where name like '%17899%';

-- 使用函数
select * from userinfo where reverse(name) = '1xela';

-- or 当or条件中有未建立索引的列才失效
select * from userinfo where id = 1 or email = 'egon1@oldboy';

-- 类型不一致
insert into userinfo values(0,'9','99',male);
select * from userinfo where name = 9;

-- != 如果是主键，则还是会走索引

-- > 如果是主键或索引是整数类型，则还是会走索引

-- order by 当根据索引排序时候，选择的映射如果不是索引，则不走索引 如果对主键排序，则还是走索引
```

**其他注意事项**

避免使用select *
count(1)或count(列) 代替 count(*)
创建表时尽量时 char 代替 varchar
表的字段顺序固定长度的字段优先
组合索引代替多个单列索引（经常使用多个条件查询时）
尽量使用短索引
使用连接（JOIN）来代替子查询(Sub-Queries)
连表时注意条件类型需一致
索引散列值（重复少）不适合建索引，例：性别不适合

**执行计划**

explain + 查询SQL ，用于显示SQL执行信息参数，根据参考信息可以进行SQL优化

```mysql
explain select * from userinfo;
explain select * from (select id,name from userinfo where id <20) as A;
```

参数说明

| select_type  | 查询类型       |
| ------------ | -------------- |
| SIMPLE       | 简单查询       |
| PRIMARY      | 最外层查询     |
| SUBQUERY     | 映射为子查询   |
| DERIVED      | 子查询         |
| UNION        | 联合           |
| UNION RESULT | 使用联合的结果 |

| table          |
| -------------- |
| 正在访问的表名 |

type： 查询时的访问方式

性能：**all < index < range < index_merge < ref_or_null < ref < eq_ref < system/const**

ALL ：全表扫描，对于数据表从头到尾找一遍

```mysql
explain select * from userinfo;
```

如果有limit限制，则找到之后就不在继续向下扫描

```mysql
explain select * from userinfo limit 1;
```

INDEX ： 全索引扫描，对索引从头到尾找一遍

```mysql
explain select nid from userinfo;
```

RANGE： 对索引列进行范围查找

```mysql
explain select *  from userinfo where name < 'alex';
```

INDEX_MERGE： 合并索引，使用多个单列索引搜索

```mysql
explain select *  from userinfo where name = 'alex' or id in (11,22,33);
```

 REF： 根据索引查找一个或多个值

```mysql
explain select *  from userinfo where name = 'alex112';
```

EQ_REF： 连接时使用primary key 或 unique类型

```mysql
explain select userinfo2.id,userinfo.name from userinfo left join userinfo2 on userinfo.id = userinfo2.id;
```

CONST ：常量 

表最多有一个匹配行,因为仅有一行,在这行的列值可被优化器剩余部分认为是常数，const表很快,因为它们只读取一次

```mysql
explain select id from tb1 where id = 2 ;
```

SYSTEM：系统 表仅有一行(=系统表)。这是const联接类型的一个特例

possible_keys：可能使用的索引

key：真实使用的

key_len：mysql中使用索引字节长度

rows： mysql估计为了找到所需的行而要读取的行数 ，只是预估值



**慢日志记录**

开启慢查询日志，可以让MySQL记录下查询超过指定时间的语句，通过定位分析性能的瓶颈，才能更好的优化数据库系统的性能。

查询是否开了慢查询

```mysql
show variables like 'slow_query%';
```

参数解释：

slow_query_log         慢查询开启状态，OFF 未开启 ON 为开启

slow_query_log_file  慢查询日志存放的位置

```mysql
show variables like '%queries%';
```

log_queries_not_using_indexes 为使用索引的搜索是否记录

查看慢查询超时时间

```mysql
show variables like 'long%';
```

long_query_time 查询超过多少秒才记录，默认10秒 

**开启慢日志方法1**

```mysql
set global slow_query_log=1; -- 1表示开启，0表示关闭
```

```mysql
set global slow_query_log=on;
```

**开启慢日志方法2**

mysql-8.0.13没有找到配置文件，在安装目录下新建my.ini配置文件，启动mysql会自动读取该目录下的配置文件，因此该配置是永久生效的。

配置文件内容如下：

```mysql
[mysqld]
slow_query_log = on
slow_query_log_file=D:\Program files\mysql-8.0.13-winx64_\data\localhost_slow.log
long_query_time = 1
```

修改配置文件之后，需要重启mysql服务

指定配置文件启动服务，关闭后重启，不会再应用该配置文件

```mysql
mysqld --defaults-file="D:\Program files\mysql-8.0.13-winx64_\my2.ini"  
```

**分页性能相关方案**



```mysql
-- 第1页：
select * from userinfo limit 0,10;
-- 第2页：
select * from userinfo limit 10,10;
-- 第3页：
select * from userinfo limit 20,10;
-- 第4页：
select * from userinfo limit 30,10;
......
-- 第2000010页
select * from userinfo limit 2000000,10;

-- 越往后查询，需要的时间约长，是因为越往后查，全文扫描查询，会去数据表中扫描查询。
```

**解决方案**

一、不允许查看这么靠后的数据，比如百度就是这样的

![](https://i.loli.net/2018/11/20/5bf42b7de1b6c.jpg)

二、在查询下一页时把上一页的行id作为参数传递给客户端程序，然后sql就改成了

```mysql
select * from userinfo where id>3000000 limit 10;
```

这条语句执行也是在毫秒级完成的，id>300w其实就是让mysql直接跳到这里了，不用依次在扫描全面所有的行

如果你的table的主键id是自增的，并且中间没有删除和断点，那么还有一种方式，比如100页的10条数据

```mysql
select * from userinfo where id>100*10 limit 10;
```

**页面只有上一页，下一页**

语法

```mysql
select * from userinfo where id>max_id limit 10; -- 下一页

select * from userinfo where id<min_id order by id desc limit 10; -- 上一页
```

举例

```mysql
select * from userinfo where id > 20010 limit 10; -- 下一页
select * from userinfo where id<20011 order by id desc limit 10; -- 上一页
```

**中间有页码的情况**

语法

```mysql
select * from (select * from userinfo where id > pre_max_id limit (cur_max_id-pre_max_id)) as A order by id desc limit 10;
```

举例

```mysql
select * from userinfo where id > 20010 limit 10; -- 比如现在是2001页
select * from userinfo where id > 20030 limit 10; -- 现在需要跳转到2003页

-- 就是下面的sql
select * from (select * from userinfo where id > 20010 limit 30) as A order by id desc limit 10;

-- 如果觉得id排序，页面展示有问题时，可以对上面的sql，增加一个排序
select * from (
select * from (select * from userinfo where id > 20010 limit 30) as A order by id desc limit 10) as foo ORDER BY id asc;
```

三.延迟索引

那我们尽量的只查有索引的id，通过索引查出来的id，速度非常的快，然后我们再根据查出来的id，进行回行一次性的取具体的数据。这就是延迟索引。



### SQLAchemy

SQLAlchemy是Python编程语言下的一款ORM框架，该框架建立在数据库API之上，使用关系对象映射进行数据库操作，简言之便是：将对象转换成SQL，然后使用数据API执行SQL并获取执行结果。

**安装**

```
pip3 install SQLAlchemy
```

![](https://images2015.cnblogs.com/blog/425762/201607/425762-20160723192854919-886727948.png)



SQLAlchemy本身无法操作数据库，其必须依赖pymsql等第三方插件，Dialect用于和数据API进行交流，根据配置文件的不同调用不同的数据库API，从而实现对数据库的操作

**pymysql**

```
 mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
```

**一、内部处理**

```mysql
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123123@127.0.0.1:3306/db1", max_overflow=5)

# 执行SQL 插入数据
cur = engine.execute("INSERT INTO t1 (name) VALUES ('sqlalchemy')")
cur = engine.execute('INSERT INTO t1(name) VALUES(%s)', [('tom2',), ('john2', )])

# 执行SQL 查询数据
cur = engine.execute('select * from t1')
# 获取第一行数据
print(cur.fetchone())
# 获取第n行数据
print(cur.fetchmany(3))
# 获取所有数据
print(cur.fetchall())
```

**二、ORM功能使用**

```python
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index, CHAR, VARCHAR
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

Base = declarative_base()


class UserType(Base):
    __tablename__ = 'usertype'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(32), nullable=True, index=True)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(32), nullable=True, index=True)
    email = Column(VARCHAR(16), unique=True)
    user_type_id = Column(Integer, ForeignKey("usertype.id"))

    user_type = relationship("UserType", backref='xxoo')

    # __table_args__ = (
    #     UniqueConstraint('id', 'name', name='uix_id_name'),
    #     Index('ix_n_ex','name', 'email',),
    # )


def create_db():
    engine = create_engine("mysql+pymysql://root:123123@127.0.0.1:3306/s4day62db?								charset=utf8", max_overflow=5)
    Base.metadata.create_all(engine)


def drop_db():
    engine = create_engine("mysql+pymysql://root:123123@127.0.0.1:3306/s4day62db?								charset=utf8", max_overflow=5)
    Base.metadata.drop_all(engine)


engine = create_engine("mysql+pymysql://root:123123@127.0.0.1:3306/s4day62db?charset=utf8", max_overflow=5)
Session = sessionmaker(bind=engine)
session = Session()

# 类    ---> 表
# 对象  ---> 行
# 增加
obj1 = UserType(title='普通用户')
session.add(obj1)

objs = [
        UserType(title='超级用户'),
        UserType(title='白金用户'),
        UserType(title='黑金用户'),
        ]
session.add_all(objs)


session.commit()
session.close()
```

```python
# 查
print(session.query(UserType))
# SELECT usertype.id AS usertype_id, usertype.title AS usertype_title
# FROM usertype

user_type_list = session.query(UserType).all()
print(user_type_list)
# [<__main__.UserType object at 0x00000228D2FA8240>, <__main__.UserType object at 0x00000228D2FA8550>, 
# <__main__.UserType object at 0x00000228D2FA8630>, <__main__.UserType object at 0x00000228D2FA84A8>]

for row in user_type_list:
    print(row.id, row.title)
    
# 26 普通用户
# 28 白金用户
# 27 超级用户
# 29 黑金用户

# select id,title from usertype where id > 26;
user_type_list = session.query(UserType.id, UserType.title).filter(UserType.id > 26)
for row in user_type_list:
    print(row.id, row.title)

# 笛卡尔积
# select * from user,usertype;
ret = session.query(Users, UserType)

print(ret)
# SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email, 
# users.user_type_id AS users_user_type_id, usertype.id AS usertype_id, usertype.title AS usertype_title 
# FROM users, usertype
```

```python
# 连表
ret = session.query(Users, UserType).filter(Users.user_type_id == UserType.id)
# 相当于sql语句 select * from (users,usertype) where users.user_type_id = usertype.id;
for row in ret:
    print(row[0].id, row[0].name, row[0].email, row[1].id, row[1].title)
    
result = session.query(Users).join(UserType)
print(result)
# SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email, 
# users.user_type_id AS users_user_type_id 
# FROM users INNER JOIN usertype ON usertype.id = users.user_type_id

result2 = session.query(Users).join(UserType, isouter=True)
print(result2)
# SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email,
# users.user_type_id AS users_user_type_id
# FROM users LEFT OUTER JOIN usertype ON usertype.id = users.user_type_id
```

```python
print(session.query(Users).as_scalar())
# (SELECT users.id, users.name, users.email, users.user_type_id 
# FROM users)

result = session.query(UserType.id, session.query(Users).filter(Users.user_type_id == UserType.id).as_scalar())
print(result)
# SELECT usertype.id AS usertype_id, (SELECT users.id, users.name, users.email, users.user_type_id 
# FROM users 
# WHERE users.user_type_id = usertype.id) AS anon_1 
# FROM usertype

```

```python
# 子查询
q1 = session.query(UserType).filter(UserType.id > 27).subquery()
result = session.query(q1).all()
print(result)
```

**其他**

```python
#　条件
ret = session.query(Users).filter_by(name='alex').all()
ret = session.query(Users).filter(Users.id > 1, Users.name == 'eric').all()
ret = session.query(Users).filter(Users.id.between(1, 3), Users.name == 'eric').all()
ret = session.query(Users).filter(Users.id.in_([1, 3, 4])).all()
ret = session.query(Users).filter(~Users.id.in_([1, 3, 4])).all()
ret = session.query(Users).filter(Users.id.in_(session.query(Users.id).filter_by(name='eric'))).all()

from sqlalchemy import and_, or_

ret = session.query(Users).filter(and_(Users.id > 3, Users.name == 'eric')).all()
ret = session.query(Users).filter(or_(Users.id < 2, Users.name == 'eric')).all()
ret = session.query(Users).filter(
    or_(
        Users.id < 2,
        and_(Users.name == 'eric', Users.id > 3),
        Users.extra != ""
    )).all()
```

```python
# 通配符
ret = session.query(Users).filter(Users.name.like('e%')).all()
# ~ 非，not
ret = session.query(Users).filter(~Users.name.like('e%')).all()
```

```python
# 分页
ret = session.query(Users)[1:2]
```

```python
# 排序
ret = session.query(Users).order_by(Users.name.desc()).all()
ret = session.query(Users).order_by(Users.name.desc(), Users.id.asc()).all()
```

```python
# 分组
from sqlalchemy.sql import func

ret = session.query(
    func.max(Users.id),
    func.sum(Users.id),
    func.min(Users.id)).group_by(Users.name).all()

ret = session.query(
    func.max(Users.id),
    func.sum(Users.id),
    func.min(Users.id)).group_by(Users.name).having(func.min(Users.id) > 2).all()
```

```python
# 问题1. 获取用户信息以及与其关联的用户类型名称(FK,Relationship正向操作)
user_list = session.query(Users, UserType).join(UserType, isouter=True)
print(user_list)
# SELECT users.id AS users_id, users.name AS users_name, users.email AS users_email, 
# users.user_type_id AS users_user_type_id, usertype.id AS usertype_id, 
# usertype.title AS usertype_title 
# FROM users LEFT OUTER JOIN usertype ON usertype.id = users.user_type_id
for row in user_list:
    print(row[0].id, row[0].name, row[0].email, row[0].user_type_id, row[1].title)
    
user_list = session.query(Users.name, UserType.title).join(UserType,isouter=True).all()
for row in user_list:
    print(row[0], row[1], row.name, row.title)

user_list = session.query(Users)
for row in user_list:
    print(row.name, row.id, row.user_type.title)
```

```python
# 问题2. 获取用户类型
type_list = session.query(UserType)
for row in type_list:
    print(row.id, row.title, session.query(Users).filter(Users.user_type_id == row.id).all())

type_list = session.query(UserType)
for row in type_list:
    print(row.id, row.title, row.xxoo)
```

