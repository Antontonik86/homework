from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import asyncio

api = " "  
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Информация'),
            KeyboardButton(text='Рассчитать')
        ]
    ], resize_keyboard=True
)

@dp.message_handler(text='Информация')
async def inform(message: types.Message):
    await message.answer('Привет! Этот бот создан по формуле Миффлина-Сан Жеора – это одна из самых последних формул расчета калорий для '
                         'оптимального похудения или сохранения нормального веса. Она была выведена в 2005 году и '
                         'все чаще заменяет классическую формулу Харриса-Бенедикта.')

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text='Рассчитать')
async def set_age(message: types.Message):
    await message.answer('Введите свой возраст: ')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if message.text.isdigit():  
        await state.update_data(age=message.text)
        await message.answer('Введите свой рост в см: ')
        await UserState.growth.set()
    else:
        await message.answer('Пожалуйста, введите корректный возраст в числах.')

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if message.text.isdigit():  
        await state.update_data(growth=message.text)
        await message.answer('Введите свой вес в кг:')
        await UserState.weight.set()
    else:
        await message.answer('Пожалуйста, введите корректный рост в числах.')

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    if message.text.replace('.', '', 1).isdigit():  
        await state.update_data(weight=message.text)
        data = await state.get_data()

        age = float(data['age'])
        growth = float(data['growth'])
        weight = float(data['weight'])

        man = 10 * weight + 6.25 * growth - 5 * age + 5
        woman = 10 * weight + 6.25 * growth - 5 * age - 161

        await message.answer(f"Норма калорий для мужчин: {man:.2f} ккал")
        await message.answer(f"Норма калорий для женщин: {woman:.2f} ккал")

        await state.finish()
    else:
        await message.answer('Пожалуйста, введите корректный вес в числах.')

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
