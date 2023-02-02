import asyncio
import sys


class Sleeper:

    def __init__(self, time: int):
        self.time = time

    async def sleeping(self, return_test_value=None):
        await asyncio.sleep(self.time)
        return return_test_value


async def async_example():
    sleeper1 = Sleeper(5)
    sleeper2 = Sleeper(10)
    gather_result = await asyncio.gather(
        sleeper1.sleeping(1),
        sleeper2.sleeping(0),
    )
    return gather_result


result = asyncio.run(async_example())
sys.exit(0)
