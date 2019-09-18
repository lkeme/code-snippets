#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
- author: Lkeme
- contact: Useri@live.cn
- file: ThreadPool
- time: 2019/9/18 13:22
- desc: 基础线程池
"""
from threading import Thread
import threading
import time
import random
from queue import Queue


class ThreadPoolManger:
    """线程池管理器"""

    def __init__(self, thread_num):
        # 初始化参数
        self.work_queue = Queue()
        self.thread_num = thread_num
        self.__init_threading_pool(self.thread_num)

    def __init_threading_pool(self, thread_num):
        # 初始化线程池，创建指定数量的线程池
        for i in range(thread_num):
            thread = ThreadManger(self.work_queue)
            thread.start()

    def add_job(self, func, *args):
        # 将任务放入队列，等待线程池阻塞读取，参数是被执行的函数和函数的参数
        self.work_queue.put((func, args))


class ThreadManger(Thread):
    """定义线程类，继承threading.Thread"""

    def __init__(self, work_queue):
        Thread.__init__(self)
        self.work_queue = work_queue
        self.daemon = True

    def run(self):
        # 启动线程
        while True:
            target, args = self.work_queue.get()
            target(*args)
            self.work_queue.task_done()


# 处理中心
def handle_request(param):
    delay = random.randint(1, 10)
    time.sleep(delay)
    print(f"thread {threading.current_thread().name} is running", param)


if __name__ == '__main__':
    # 创建一个有4个线程的线程池
    thread_pool = ThreadPoolManger(4)

    # 循环
    while True:
        thread_pool.add_job(handle_request, "args")
        time.sleep(1)
