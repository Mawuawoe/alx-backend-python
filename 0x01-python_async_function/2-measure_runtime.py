#!/usr/bin/env python3
"""
measure the total time elapse
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    function to return time for each
    coroutine
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    time_per_coroutine = total_time / n
    return time_per_coroutine
