from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio
import logging
from crud_functions import *



print()     # Отступ

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


inline_kb = InlineKeyboardMarkup()
inline_button_calculate = InlineKeyboardButton(text='Рассчитать норму калорий',
                                               callback_data='calories')
inline_button_formulas = InlineKeyboardButton(text='Формулы расчёта',
                                              callback_data='formulas')
inline_kb.add(inline_button_calculate, inline_button_formulas)


kb = ReplyKeyboardMarkup(resize_keyboard=True)


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Рассчитать'),
            KeyboardButton(text='Информация')

        ],
        [
            KeyboardButton(text='Купить')
        ]
    ], resize_keyboard=True
)

buy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Product1", callback_data="product_buying"),
            InlineKeyboardButton(text="Product2", callback_data="product_buying"),
            InlineKeyboardButton(text="Product3", callback_data="product_buying"),
            InlineKeyboardButton(text="Product4", callback_data="product_buying")
        ]
    ]
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inline_kb)



@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('Формула Миффлина-Сан Жеора:\n'
                              'Для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5\n'
                              'Для женщин: 10 * вес + 6.25 * рост - 5 * возраст - 161')



@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст: ')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес: ')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)

    data = await state.get_data()
    age = float(data['age'])
    growth = float(data['growth'])
    weight = float(data['weight'])

    man = 10 * weight + 6.25 * growth - 5 * age + 5
    woman = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Норма калорий для мужчин: {man}")
    await message.answer(f"Норма калорий для женщин: {woman}")

    await state.finish()

@dp.message_handler(text='Информация')
async def info(message):
    with open('files/4.jpg', 'rb') as img:
        await message.answer_photo(img,' МЫ предлогаем лучшие товары', reply_markup=start_kb)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    # with open("files/BOMBBAR.jpg", "rb") as BOMBBAR:
    #     await message.answer_photo(BOMBBAR, f"Название: Product1 | Описание: BOMBBAR | Цена: {1*100}")
    # with open("files/Nattys.jpg", "rb") as Nattys:
    #     await message.answer_photo(Nattys, f"Название: Product2 | Описание: Nattys | Цена: {2*100}")
    # with open("files/R.A.W.LIFE.jpg", "rb") as LIFE:
    #     await message.answer_photo(LIFE, f"Название: Product3 | Описание: R_A_W_LIFE | Цена: {3*100}")
    # with open("files/Kultlab.jpg", "rb") as Kultlab:
    #     await message.answer_photo(Kultlab, f"Название: Product4 | Описание: Kultlab | Цена: {4*100}")
    base = get_all_products()
    for number in base:
        await message.answer(f'Название:Продукт {number[1]} / Описание: описание {number[2]} / Цена: {number[3]}')
        with open(f'{number[0]}.jpg', 'rb') as file:
            await message.answer_photo(file)
    await message.answer("Выберите продукт для покупки:", reply_markup=buy_menu)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукцию!')



@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью и продающий товары.',
                         reply_markup=start_kb)


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)