import logging
import os
from dotenv import load_dotenv
load_dotenv()
from aiogram import Bot, Dispatcher, executor, types
from PSQL import DataBasa

token = os.getenv("bot")
logging.basicConfig(level= logging.INFO)
bt = Bot(token= token )
dp = Dispatcher(bt)

@dp.message_handler(commands= ['start','help'])
async def Bot_boshlash(message: types.Message):
    ismi = message.from_user.username
    familasi = message.from_user.username
    print(f"{ismi} start bot ")
    quer = f""" INSERT INTO users(ismi,familasi) VALUES ('{ismi}','{familasi}')"""
    DataBasa.postgrestt(quer,'insert')
    await message.reply(f"salom  @{ismi}   bolajon ??? ")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)