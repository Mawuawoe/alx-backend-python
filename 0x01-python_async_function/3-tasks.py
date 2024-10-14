#!/usr/bin/env python3
"""
create and return a task object
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """
    function create a task
    return a task object
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
