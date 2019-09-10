# 抢票
import json
import time
import random
from multiprocessing import Process, Lock


def check_ticket(i):
    with open('ticket') as f:
        ticket_count = json.load(f)
    print('person{}查询当前余票{}'.format(i, ticket_count['count']))


def buy_ticket(i, lo):
    check_ticket(i)
    lo.acquire()
    with open('ticket') as f:
        ticket_count = json.load(f)
    time.sleep(random.random())
    if ticket_count['count'] > 0:
        print('person{}购票成功'.format(i))
        ticket_count['count'] -= 1
    else:
        print('余票不足，person{}购票失败'.format(i))
    time.sleep(random.random())
    with open('ticket', mode='w') as f:
        json.dump(ticket_count, f)
    lo.release()


if __name__ == '__main__':
    lo = Lock()
    for i in range(1, 6):
        Process(target=buy_ticket, args=(i, lo)).start()
