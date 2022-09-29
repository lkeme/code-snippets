#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
- author: Lkeme
- contact: Useri@live.cn
- file: MultThread
- time: 2019/9/18 13:45
- desc: 通用多任务分段多线程执行
"""
import threading
import math
import time


# 多线程
class MultiThread(threading.Thread):
    def __init__(self, tasks):
        threading.Thread.__init__(self)
        self.tasks = tasks

    def run(self):
        handle_request(self.ips)
        return None


# 任务逻辑
def handle_request(tasks):
    for task in tasks:
        print(f"thread {threading.current_thread().name} is running", task)


if __name__ == '__main__':
    # 线程数 线程列表
    threads = 20
    threads_list = []
    # 任务分段
    tasks = range(10000)
    step = math.floor(len(tasks) / threads)
    tasks_list = [tasks[i:i + step] for i in range(0, len(tasks), step)]
    # 启动线程
    for tasks in tasks_list:
        threads_list.append(MultiThread(tasks))
    for t in threads_list:
        t.setDaemon(True)
        t.start()

    while True:
        try:
            time.sleep(30)
        except Exception as e:
            print(e)
