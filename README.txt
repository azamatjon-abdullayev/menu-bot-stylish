MiniApp-Bot — Telegram Mini App (WebApp) loyiha

Ichida:

- bot.py       : Aiogram bot. TOKEN va WEBAPP_URL ni to'ldiring.
- index.html   : Mini App sahifasi (Vercel ga upload qilish uchun)

Qanday ishlatish:
1) index.html ni Vercel/Netlify ga joylashtiring va HTTPS URL oling.
2) bot.py ichidagi WEBAPP_URL ga o'sha HTTPS URL ni qo'ying.
3) bot.py ichidagi TOKEN ga bot tokenni qo'ying.
4) bot.py ni ishga tushiring: python bot.py

Guruhga yuborish:
- Loyihada GROUP_ID sifatida -1003143807723 belgilangan.
- Botning guruhga xabar yuborishi uchun botni guruhga admin qilib qo'ying yoki guruhga qo'shing.

Eslatma: Aiogram 3.x talab qilinadi.
pip install aiogram flask
