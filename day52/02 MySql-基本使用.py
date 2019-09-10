# 1、RDBMS

# Relational Database Management System
# 当前主要使用两种类型的数据库：关系型数据库、非关系型数据库。本部分主要讨论关系型数据库，对于非关系型数据库会在后面学习
#
# 所谓的关系型数据库RDBMS，是建立在关系模型基础上的数据库，借助于集合代数等数学概念和方法来处理数据库中的数据
#
#
# 2、SQL

# Structured Query Language
# SQL是结构化查询语言，是一种用来操作RDBMS的数据库语言，当前关系型数据库都支持使用SQL语言进行操作
# 也就是说可以通过 SQL 操作 oracle,sql server,mysql,sqlite 等等所有的关系型的数据库

# SQL语句主要分为：
# DQL：数据查询语言，用于对数据进行查询，如select
# DML：数据操作语言，对数据进行增加、修改、删除，如insert、udpate、delete
# TPL：事务处理语言，对事务进行处理，包括begin transaction、commit、rollback
# DCL：数据控制语言，进行授权与权限回收，如grant、revoke
# DDL：数据定义语言，进行数据库、表的管理等，如create、drop
# CCL：指针控制语言，通过控制指针完成表的操作，如declare cursor

# 对于web程序员来讲，重点是数据的增删改查，必须熟练编写DQL、DML，能够编写DDL完成数据库、表的操作
# 其它语言如TPL、DCL、CCL了解即可

# SQL 是一门特殊的语言,专门用来操作关系数据库 不区分大小写

# 3、MySQL 简介

# MySQL是一个关系型数据库管理系统

# mysql-8.0.11-winx64.zip在Windows中的安装配置
# https://jingyan.baidu.com/article/0964eca25903618285f53602.html
# 安装mysql8.0.11及修改root密码、连接navicat for mysql的思路详解
# https://www.jb51.net/article/142025.htm

# 4、数据完整性

# 一个数据库就是一个完整的业务单元，可以包含多张表，数据被存储在表中
# 在表中为了更加准确的存储数据，保证数据的正确有效，可以在创建表的时候，为表添加一些强制性的验证，包括数据字段的类型、约束

# 数据类型
# 使用数据类型的原则是：够用就行，尽量使用取值范围小的，而不用大的，这样可以更多的节省存储空间

# 常用数据类型如下：
# 整数：int，bit
# 小数：decimal
# 字符串：varchar,char
# 日期时间: date, time, datetime
# 枚举类型(enum)

# 特别说明的类型如下：
# decimal表示浮点数，如decimal(5,2)表示共存5位数，小数占2位
# char表示固定长度的字符串，如char(3)，如果填充'ab'时会补一个空格为'ab '
# varchar表示可变长度的字符串，如varchar(3)，填充'ab'时就会存储'ab'
# 字符串text表示存储大文本，当字符大于4000时推荐使用
# 对于图片、音频、视频等文件，不存储在数据库中，而是上传到某个服务器上，然后在表中存储这个文件的保存路径
# 更全的数据类型可以参考http://blog.csdn.net/anxpp/article/details/51284106

# 约束
# 主键primary key：物理上存储的顺序
# 非空not null：此字段不允许填写空值
# 惟一unique：此字段的值不允许重复
# 默认default：当不填写此值时会使用默认值，如果填写时以填写为准
# 外键foreign key：对关系字段进行约束，当为关系字段填写值时，会到关联的表中查询此值是否存在
# 如果存在则填写成功，如果不存在则填写失败并抛出异常

# 数值类型(常用)

# 类型	            字节大小	    有符号范围(Signed)	            无符号范围(Unsigned)
# TINYINT	        1	        -128 ~ 127	                    0 ~ 255
# SMALLINT	        2	        -32768 ~ 32767	                0 ~ 65535
# MEDIUMINT	        3	        -8388608 ~ 8388607	            0 ~ 16777215
# INT/INTEGER	    4	        -2147483648 ~2147483647	        0 ~ 4294967295
# BIGINT	        8	        -9223372036854775808            0 ~ 18446744073709551615
#                               ~ 9223372036854775807

# 字符串
# 类型	    字节大小	        示例
# CHAR	    0-255	        类型:char(3) 输入 'ab', 实际存储为'ab ', 输入'abcd' 实际存储为 'abc'
# VARCHAR	0-255	        类型:varchar(3) 输 'ab',实际存储为'ab', 输入'abcd',实际存储为'abc'
# TEXT	    0-65535	        大文本

# 日期时间类型
# 类型	        字节大小	        示例
# DATE	        4	            '2020-01-01'
# TIME	        3	            '12:29:59'
# DATETIME	    8	            '2020-01-01 12:29:59'
# YEAR	        1	            '2017'
# TIMESTAMP	    4	            '1970-01-01 00:00:01' UTC ~ '2038-01-01 00:00:01' UTC