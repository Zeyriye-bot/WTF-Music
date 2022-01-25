import asyncio
from pytgcalls import idle
from driver.anonymous import call_py, bot

async def start_bot():
    await bot.start()
    print("[INFO]: BOT & UBOT CLIENT STARTED !!")
    await call_py.start()
    print("[INFO]: PYTGCALLS CLIENT STARTED !!")
    await idle()
    print("[INFO]: STOPPING BOT & ASSISTANT")
    await bot.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
