import tensorflow as tf
# 1、首先定义队列
Q = tf.FIFOQueue(3, tf.float32)
#
# # 放入一些数据
enq_many = Q.enqueue_many([[0.1, 0.2, 0.3], ])
#
# 2、定义一些处理数据的螺距，取数据的过程      取数据，+1， 入队列
#
out_q = Q.dequeue()

data = out_q + 1

en_q = Q.enqueue(data)

with tf.Session() as sess:
    # 初始化队列
    sess.run(enq_many)

    # 处理数据
    for i in range(100):
        sess.run(en_q)

    # 训练数据
    for i in range(Q.size().eval()):
        print(sess.run(Q.dequeue()))