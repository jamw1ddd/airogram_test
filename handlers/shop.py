from aiogram import Bot, Dispatcher, html, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram import Router
from aiogram.fsm.context import FSMContext
from session import get_categories, get_customer, get_events, register_customer
from states.shop import Shop
from utils import get_word

shop_router = Router()


@shop_router.message(F.text.in_(['Tabriknomalar', 'Открытки']))
async def company_handler(message: Message, state: FSMContext) -> None:
    customer, _ = await get_customer(message.from_user.id)
    categories = await get_categories()
    await state.update_data({category['name']: category['next_state'] for category in categories})
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=category['name'])] for category in categories],
        resize_keyboard=True)
    await state.set_state(Shop.category)
    await message.answer(await get_word('choose-event', customer['lang']), reply_markup=keyboard)


@shop_router.message(Shop.category)
async def category_handler(message: Message, state: FSMContext) -> None:
    events = await get_events(message.text)
    data = await state.get_data()
    next_state = data[message.text]
    if next_state == 'event':
        await state.set_state(Shop.event)
        keys = [[KeyboardButton(text=event['name'])] for event in events]
    elif next_state == 'for_who':
        await state.set_state(Shop.for_who)
        keys = [[KeyboardButton(text="Erkak"), KeyboardButton(text="Ayol")]]

    keys.append([KeyboardButton(text="Orqaga")])
    keyboard = ReplyKeyboardMarkup(
            keyboard=keys,
            resize_keyboard=True)
    await message.answer(await get_word('choose-event'), reply_markup=keyboard)


@shop_router.message(Shop.event)
async def company_handler(message: Message, state: FSMContext) -> None:
    if message.text == 'Orqaga':
        customer,_ = await get_customer(message.from_user.id)
        categories = await get_categories()
        await state.set_state(Shop.category)
        keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=category['name'])] for category in categories],
        resize_keyboard=True)
        await message.answer(await get_word('choose-event',customer['lang']),reply_markup=keyboard)
    
    await state.set_state(Shop.for_who)
    await message.answer(await get_word('choose-event'),reply_markup=keyboard)


@shop_router.message(Shop.for_who)
async def company_handler(message: Message, state:FSMContext) -> None:
    if message.text == 'Orqaga':
        customer,_ = await get_customer(message.from_user.id)
        categories = await get_categories()
        await state.set_state(Shop.category)
        keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=category['name'])] for category in categories],
        resize_keyboard=True)
        await message.answer(await get_word('choose-event',customer['lang']),reply_markup=keyboard)
    
    await message.answer(await get_word('choose-event'),reply_markup=keyboard)

