#!/usr/bin/env python3
"""
asyn function in python
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """
    an async function that generate
    random delay
    return seconds delayed
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
