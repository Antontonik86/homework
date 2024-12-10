from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


import asyncio

api = ""
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
async def inform(message):
    await message.answer('Привет этот бот создан по формуле Миффлина-Сан Жеора – это одна из самых последних формул расчета калорий для '
                         'оптимального похудения или сохранения нормального веса. Она была выведена в 2005 году и '
                         'все чаще стала заменять классическую формулу Харриса-Бенедикта.')

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



@dp.message_handler(text = 'Расчитать')
async def set_age(message):
    await message.answer('Введите свой возраст: ')
    await UserState.age.set()

@dp.message_handler(state= UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост: ')
    await UserState.growth.set()


@dp.message_handler(state= UserState.growth)
async def sey_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state= UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()

    age = float(data['age'])
    growth = float(data['growth'])
    weight = float(data['weight'])

    man = 10 * weight + 6.25 * growth - 5 * age + 5
    woman = 10 * weight + 6.25 * growth - 5 * age - 161

    await message.answer(f"Норма калорий для мужчин: {man}")
    await message.answer(f"Норма калорий для женщин: {woman}")

    await state.finish()


@dp.message_handler(commands=["start"])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
