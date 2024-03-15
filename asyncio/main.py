import asyncio
import time
import aiohttp
import requests

# asyncio - асинхронное выполнение,подходит для IO-bound задач, работает ровно 1 поток

# плюсы:
# + скорость и экономия времени, вместо х + у + z -> max(x, y, z)
#
#
#
#
# 1) корутина работает как генератор
# 2) async - явный флаг,что функция является асинхронной (корутиной)
# 3)await - явный флаг, что в этом месте функция встает на паузу и дает работать другим, пока ждет свои данные
# 4) event loop - цикл событий, механизм, который отвечает за планирование и запуск корутин.
# Можно представить как список\очередь, из которого в вечном цикле достаются и запускаются корутины

# Частые ошибки:
# - не использование await внутри корутины
# - оздание корутины, но использование ее, как функции
# - использование внутри корутин синхронного(блокирующего) кода, в том числе IO

async def one():
    print('start one')
    await asyncio.sleep(1)
    print('stop one')


async def two():
    print('start two')
    await asyncio.sleep(2)
    print('stop two')


async def three():
    print('start third')
    await asyncio.sleep(3)
    print('stop third')


async def main():
    asyncio.create_task(one())
    asyncio.create_task(two())
    await asyncio.create_task(three())


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
