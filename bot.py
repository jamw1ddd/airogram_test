'''import asyncio
import logging
import sys
from os import getenv

from aiogram import F, Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
import os
from utils import get_info,calculate,calculate2
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton


TOKEN = "7642623985:AAGwb5M7FzNOXGlWCeYl6SX17APkFxWOxYk"
#print(TOKEN)
# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Tabriknomalar')]],resize_keyboard=True)
    
    await message.answer(f"Assalomu aleykum.\nQuyidagi kerakli bo'limni tanlang!",reply_markup=keyboard)


@dp.message(F.text=='Tabriknomalar')
async def command_start_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Bayramlar'),KeyboardButton(text='Tugilgan kun')],
                  [KeyboardButton(text="To'y"),KeyboardButton(text='Yubiley')]],
        resize_keyboard=True)
    await message.answer(f"Nima bilan tabriklamoqchisiz?",reply_markup=keyboard)


@dp.message(F.text=='Bayramlar')
async def command_start_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Yangi yil'),KeyboardButton(text='Xotira va Qadirlash kuni')],
                  [KeyboardButton(text="Mustaqillik kuni"),KeyboardButton(text='Ustoz va Murabiylar kuni')],
                  [KeyboardButton(text='Konsitutsiya kuni'),KeyboardButton(text='Ramazon hayiti')],
                  [KeyboardButton(text="Qurbon hayiti"),KeyboardButton(text='Xalqaro xotin-qizlar kuni')],
                  [KeyboardButton(text="Navro'z bayrami"),KeyboardButton(text='Vatan himoyachilari kuni')]],
        resize_keyboard=True)
    await message.answer(f"Qaysi bayram?",reply_markup=keyboard)

@dp.message(F.text=='Tugilgan kun')
async def command_start_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Ayol'),KeyboardButton(text='Erkak')],
                  [KeyboardButton(text="Qizaloq"),KeyboardButton(text='Bolakay')]],
        resize_keyboard=True)
    await message.answer(f"Kim uchun?",reply_markup=keyboard)

@dp.message(F.text=="To'y")
async def command_start_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Ayol'),KeyboardButton(text='Erkak')]],
        resize_keyboard=True)
    await message.answer(f"Kim uchun?",reply_markup=keyboard)

@dp.message(F.text=='Yubiley')
async def command_start_handler(message: Message) -> None:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text='Ayol'),KeyboardButton(text='Erkak')]],
        resize_keyboard=True)
    await message.answer(f"Kim uchun?",reply_markup=keyboard)

@dp.message(F.text=='hello')
async def echo_handler(message: Message) -> None:
    await message.answer("hi")

@dp.message(F.text=='Qondaye')
async def echo_handler(message: Message) -> None:
    await message.answer("Otday")

@dp.message(F.text=='Kimsan')
async def echo_handler(message: Message) -> None:
    await message.answer("Olim mani ismim")

@dp.message(F.text=='Qatasan')
async def echo_handler(message: Message) -> None:
    await message.answer("Orqendigi shkopda")

@dp.message(F.text=='Nimaga keldin')
async def echo_handler(message: Message) -> None:
    await message.answer("Kola ob keldm")

@dp.message(F.text=='Chiq')
async def echo_handler(message: Message) -> None:
    await message.answer("Toxten oldin eshitin")

@dp.message(F.text=='Nima qvosan')
async def echo_handler(message: Message) -> None:
    await message.answer("Onalariga ukalarideman")

@dp.message(F.text=='asd')
async def echo_handler(message: Message) -> None:
    await message.answer("sdfsfds")

async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())'''
import asyncio
import logging
from os import getenv

from handlers.register import register_router
from handlers.shop import shop_router

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

TOKEN = "7642623985:AAGwb5M7FzNOXGlWCeYl6SX17APkFxWOxYk"

async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(
        register_router,
        shop_router,
    )

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())