#!/usr/bin/env python3
"""
asyncio.gather()- is call with multiple coroutine,
return a future when all are resloved
when this is awaited, it returns a list
of all revolved coroutines

custom asdc sort
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    asyn function that works on
    multiple coroutines
    """
    # create a list of coroutine
    tasks = [wait_random(max_delay) for _ in range(n)]

    # run them concurrently and collect the delays
    delays = await asyncio.gather(*tasks)

    # sort the delay in Ascend order
    for i in range(1, len(delays)):
        cur = delays[i]
        j = i - 1
        prev = delays[j]

        while j >= 0 and cur < delays[j]:
            delays[j + 1] = delays[j]
            j -= 1
        delays[j + 1]

    return delays
