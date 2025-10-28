import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# 🔹 Telegram bot token
TOKEN = "6726415664:AAGgtOFgkOSVI437iuhTfwGPAfRniM1ETV8"

# 🔹 Guruh ID (buyurtmalar shu yerga keladi)
GROUP_ID = -1003143807723

# 🔹 Web App (Mini App) URL — Vercel’da joylashtirilgan link bo‘ladi
WEBAPP_URL = "https://sening-miniapp-urling.vercel.app"  # o‘zingnikiga almashtir

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text="🚖 Buyurtma berish",
                web_app=WebAppInfo(url=WEBAPP_URL)
            )
        ]]
    )
    await message.answer(
        "👋 Salom! Quyidagi tugma orqali buyurtma bering:",
        reply_markup=keyboard
    )


# 🟩 WebApp’dan qaytgan ma’lumotni qabul qilish
@dp.message(lambda msg: msg.web_app_data)
async def handle_webapp(message: types.Message):
    data = message.web_app_data.data

    # 📨 Guruhga yuboriladigan xabar
    text = f"📦 *Yangi buyurtma!*\n\n`{data}`"
    await bot.send_message(GROUP_ID, text, parse_mode="Markdown")

    await message.answer("✅ Buyurtmangiz yuborildi! Rahmat!")


# 🔹 Botni ishga tushirish
async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
