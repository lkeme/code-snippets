#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
- author: Lkeme
- contact: Useri@live.cn
- file: AsyncioLoop
- time: 2019/9/18 12:54
- desc: 兼容不同系统的协程逻辑
"""
import asyncio
import platform


# 自动判断类型生成loop
def switch_sys_loop():
    sys_type = platform.system()
    if sys_type == "Windows":
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)
    else:
        loop = asyncio.get_event_loop()

    return loop


# 逻辑
async def main_loop(thread):
    print(f"当前是第 {thread} 个协程")


# 运行
def run():
    threads = 10
    # 获取loop
    loop = switch_sys_loop()
    # 协程任务
    task_work = [
        main_loop(thread) for thread in range(threads)
    ]
    loop.run_until_complete(asyncio.wait(task_work))
    loop.close()


if __name__ == '__main__':
    run()
