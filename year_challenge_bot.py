from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from year_challenge import YearChallenge
import database_year_challenge


#  токен который выдал BotFather
BOT_TOKEN = 'xxx'

#  инициализируем экземпляр класса Bot и Dispatcher
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def process_start_bot(message: Message):
    await message.answer("Тебя приветствует бот годового челленджа! Я помогу тебе накопить сумму\n"
                         "Чтобы узнать возможности бота отправь /help")


@dp.message(Command(commands='help'))
async def process_help_bot(message: Message):
    await message.answer("Для старта челленджа отправьте /begin\n"
                         "Для генерации случайной суммы для перевода отправь /generate\n"
                         "После перевода суммы на годовой челледж отправь /transfer")

@dp.message(Command(commands='begin'))
async def process_stat_command(message: Message):
    #  инициализируем объект годового челленджа для юзера
    user_challenge = YearChallenge()
    #  создаем запись по юзеру в бд
    database_year_challenge.create_user(message.user.id, user_challenge)


if __name__ == '__main__':
    dp.run_polling(bot)
