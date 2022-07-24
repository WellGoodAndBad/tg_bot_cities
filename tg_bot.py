import asyncio

from aiogram import Bot, Dispatcher, executor, types

import mongo
import parser
import settings

bot = Bot(token=settings.TG_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="city")
async def cmd_city(message: types.Message):
    if (args := message.get_args()):
        txt_msg = await mongo.get_city_data(city=args.lower())
        if txt_msg is None:
            await message.reply("город не найден")
        else:
            await message.reply(f"ГОРОД - {txt_msg.get('city')}\n"
                                f"население - {txt_msg.get('population')}\n"
                                f"ссылка - {txt_msg.get('url')}")


@dp.message_handler(commands="start_parser")
async def cmd_parser(message: types.Message):
    task_set = asyncio.all_tasks(loop=None)
    if len([i for i in task_set if "parser" in i._coro.cr_code.co_filename]) == 0:
        asyncio.create_task(parser.parse_data())
        await message.reply("сбор данных начался")
    else:
        await message.reply("сбор данных УЖЕ начался")


@dp.message_handler()
async def cmd_cities(message: types.Message):
    if (city := message.text.lower()):
        cities = await mongo.get_all_cities(city=city)
        if cities is None:
            await message.reply("город не найден")
        else:
            cities = [i["city"] for i in cities]
            answer = '\n'.join(cities)
            await message.reply(answer)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
