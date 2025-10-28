import asyncio
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "TOKENINGNI_BU_YERGA_QO'Y"
WEBAPP_URL = "https://YOUR-VERCEL-APP.vercel.app"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(text="🚖 Buyurtma berish", web_app=WebAppInfo(url=WEBAPP_URL))
        ]]
    )
    await message.answer("👋 Salom! Quyidagi tugma orqali buyurtma bering:", reply_markup=keyboard)

# WebApp dan kelgan ma'lumotni qabul qilish
@dp.message()
async def handle_all_messages(message: types.Message):
    if message.web_app_data:
        try:
            data = json.loads(message.web_app_data.data)
            text = (
                f"🚘 <b>Yangi buyurtma!</b>\n\n"
                f"📍 Qayerdan: <b>{data.get('from')}</b>\n"
                f"🎯 Qayerga: <b>{data.get('to')}</b>\n"
                f"🚗 Mashina: <b>{data.get('car')}</b>\n"
                f"👥 Odamlar soni: <b>{data.get('people')}</b>\n"
                f"👤 Foydalanuvchi: @{message.from_user.username or 'Noma’lum'}"
            )
            await message.answer(text, parse_mode="HTML")
        except Exception as e:
            await message.answer(f"❌ Xatolik: {e}")

async def main():
    print("✅ Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
