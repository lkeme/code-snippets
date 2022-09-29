#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
- author: Lkeme
- contact: Useri@live.cn
- file: Request
- time: 2019/9/18 13:05
- desc: 协程请求与正常请求
"""
import aiohttp
import asyncio
import requests
import traceback


# aiohttp请求中心
async def _requests(method, url, proxy=None, retry=10, timeout=15, **kwargs):
    if method in ["get", "post"]:
        for _ in range(retry + 1):
            try:
                async with aiohttp.ClientSession() as session:
                    async with getattr(session, method)(
                            url, proxy=proxy, verify_ssl=False,
                            timeout=timeout,
                            **kwargs) as r:
                        # text()函数相当于requests中的r.text，r.read()相当于requests中的r.content
                        data = await r.read()
                        await r.release()
                        return data
            except Exception as e:
                print(_, e)
    return None


# requests请求中心 偷的大佬的
def _requests(method, url, decode_level=2, proxy=None, retry=10,
              timeout=15, **kwargs):
    if method in ["get", "post"]:
        for _ in range(retry + 1):
            try:
                response = getattr(requests, method)(url, timeout=timeout,
                                                     proxies=proxy, **kwargs)
                return response.json() if decode_level == 2 else response.content if decode_level == 1 else response
            except Exception as e:
                print(_, e)

    return None


if __name__ == '__main__':
    pass
