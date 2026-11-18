import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, MenuButtonWebApp

BOT_TOKEN = "ВСТАВЬ_СЮДА_ТОКЕН_ОТ_BOTFATHER"
WEBAPP_URL = "https://ТВОЙ_НИК.github.io/НАЗВАНИЕ_РЕПОЗИТОРИЯ/"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    # Устанавливаем постоянную кнопку меню слева от поля ввода
    await bot.set_chat_menu_button(
        chat_id=message.chat.id,
        menu_button=MenuButtonWebApp(
            text="🏝 Играть",
            web_app=WebAppInfo(url=WEBAPP_URL),
        ),
    )

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🏝 Открыть Остров Солнца",
                    web_app=WebAppInfo(url=WEBAPP_URL),
                )
            ]
        ]
    )

    await message.answer(
        "Добро пожаловать на <b>Остров Солнца</b>! ☀️\n\n"
        "Объединяй ресурсы, выполняй заказы жителей и преврати пустынный берег в процветающий порт.\n\n"
        "Нажми кнопку ниже, чтобы начать:",
        parse_mode="HTML",
        reply_markup=kb,
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())