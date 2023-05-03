#!/usr/bin/env python3
"""
task 2
"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """comprehensions"""
    random_number = [num async for num in async_generator()]
    return random_number
