#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
- author: Lkeme
- contact: Useri@live.cn
- file: Printer
- time: 2019/9/18 12:11
- desc: 格式化输出打印模块
"""

import time
import inspect
from termcolor import *
from html import unescape


class Printer:
    # 格式化时间
    @staticmethod
    def current_time():
        return f"[{str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))}]"

    # 样式一 信息、函数名、行数、内容
    def printer(self, string, info, color):
        ctm = self.current_time()
        tmp = "[" + str(info) + "]"
        row = "[" + str(inspect.stack()[1][3]) + ":" + str(
            inspect.stack()[1][2]) + "]"
        msg = (
            "{:<22}{:<10}{:<28}{:<20}".format(str(ctm), str(tmp), str(row),
                                              str(string)))
        print(colored(msg, color), flush=True)

    # 样式二 多参数打印
    def printer(self, info, *args):
        format_time = self.current_time()
        content = f'{format_time} {info} {" ".join(f"{str(arg)}" for arg in args)}'
        print(content)

    # 样式三  多参数、多键值参数打印
    def printer(self, info, *args, **kwargs):
        format_time = self.current_time()
        content = f'{format_time} {info} {" ".join(f"{str(arg)}" for arg in args)}'
        print(content, **kwargs)

    # 样式四 多参数打印，html编码解码
    def printer(self, info, *args):
        format_time = self.current_time()
        content = f'{format_time} {info} {" ".join(f"{str(arg)}" for arg in args)}'
        print(unescape(content))


if __name__ == '__main__':
    pass
