# 同步的概念
# 1. 多线程开发可能遇到的问题
# 假设两个线程t1和t2都要对num=0进行增1运算，t1和t2都各对num修改10次，num的最终的结果应该为20。
# 但是由于是多线程访问，有可能出现下面情况：
# 假设两个线程t1和t2都要对num=0进行增1运算
# t1和t2都各对num修改10次，num的最终的结果应该为20。
# 但是由于是多线程访问，有可能出现下面情况：
# 在num=0时，t1取得num=0。此时系统把t1调度为”sleeping”状态，把t2转换为”running”状态，t2也获得num=0。
# 然后t2对得到的值进行加1并赋给num，使得num=1。
# 然后系统又把t2调度为”sleeping”，把t1转为”running”。
# 线程t1又把它之前得到的0加1后赋值给num。
# 这样，明明t1和t2都完成了1次加1工作，但结果仍然是num=1。
# from threading import Thread
# import time
#
# g_num = 0
#
#
# def test1():
#     global g_num
#     for i in range(1000000):
#         g_num += 1
#
#     print("---test1---g_num=%d" % g_num)
#
#
# def test2():
#     global g_num
#     for i in range(1000000):
#         g_num += 1
#
#     print("---test2---g_num=%d" % g_num)
#
#
# p1 = Thread(target=test1)
# p1.start()
#
# # time.sleep(3) # 取消屏蔽之后 再次运行程序，结果会不一样，，，为啥呢？
#
# p2 = Thread(target=test2)
# p2.start()
#
# print("---g_num=%d---" % g_num)
# 执行输出
# ---g_num=501441---
# ---test1---g_num=1000000
# ---test2---g_num=1289605
# 执行输出
# ---g_num=498978---
# ---test2---g_num=1472091
# ---test1---g_num=1663684

# 取消屏蔽之后，再次运行结果如下
# ---test1---g_num=1000000
# ---g_num=1061443---
# ---test2---g_num=2000000

# 2. 什么是同步
# 同步就是协同步调，按预定的先后次序进行运行。如:你说完，我再说。
# "同"字从字面上容易理解为一起动作
# 其实不是，"同"字应是指协同、协助、互相配合。
# 如进程、线程同步，可理解为进程或线程A和B一块配合，A执行到一定程度时要依靠B的某个结果，于是停下来，示意B运行;
# B依言执行，再将结果给A;A再继续操作。