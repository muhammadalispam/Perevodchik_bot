import logging
from aiogram import Bot, Dispatcher, executor, types
from inline_btn import *
from database import *
from utills import translate_text


BOT_TOKEN = "6786900809:AAFVUiwhy6gXCCgFStotfg7rI1U7ZRvkngI"
ADMINS = [127158713]

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot)


async def command_menu(dp: Dispatcher):
    await create_tables()
    await dp.bot.set_my_commands(
        [
            types.BotCommand('start', 'Ishga tushirish'),
            types.BotCommand('help', 'Yordam'),
            types.BotCommand('statisticks', 'Statistika'),
        ]
    )


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await add_user(
        user_id=message.from_user.id,
        username=message.from_user.username
    )
    await message.answer(f"Assalomu aleykum ❗️{message.from_user.first_name}❗️ \n"
                         f"Men Tarjimon botman \n"
                         f"Menga xoxlagan soz yozsangiz men xoxlagan tilingizga tarjimaM qilib beraman ️️️️️❗️❗️ ")


@dp.message_handler(commands=["Statisticks"])
async def get_user_stat_hendler(message: types.Message):
    if message.from_user.id in ADMINS:
        count = await get_all_user()
        await message.answer(f"Pervodchik_bot botining a'zolari soni: 👉{count}👈 ni tashkil etadi")
    else:
        await message.answer(f"Pervodchik_bot botining a'zolari soni faqat bot adminiga korinadi‼️‼️")


@dp.message_handler()
async def get_user_text_handler(message: types.Message):
    btn = await translate_language_inline()
    await message.answer(text=message.text, reply_markup=btn)


@dp.callback_query_handler(text_contains="lang")
async def selected_lang_callback(call: types.callback_query):
    lang = call.data.split(':')[-1]
    text = call.message.text

    result_text = await translate_text(text=text, lang=lang)

    btn = await translate_language_inline()
    await call.message.edit_text(text=result_text, reply_markup=btn)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=command_menu)
