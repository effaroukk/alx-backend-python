#!/usr/bin/env python3
'''Task 0's module.'''
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds between 0 and max_delay.'''
    wait_time = random.uniform(0, max_delay)  # Ensure float in full range [0, max_delay]
    await asyncio.sleep(wait_time)
    return wait_time

# Example of calling the coroutine (not required for function definition):
# asyncio.run(wait_random())

