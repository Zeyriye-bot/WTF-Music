import os
import glob
import json
import logging
import asyncio
import youtube_dl
from pytgcalls import StreamType
from pytube import YouTube
from youtube_search import YoutubeSearch
from pytgcalls import PyTgCalls, idle
from pytgcalls.types import Update
from pyrogram.raw.base import Update
from pytgcalls.types import AudioPiped, AudioVideoPiped
from pytgcalls.types import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo
)
from pytgcalls.types.stream import StreamAudioEnded, StreamVideoEnded
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from helpers.queues import QUEUE, add_to_queue, get_queue, clear_queue, pop_an_item
from helpers.admin_check import *

bot = Client(
    "Music Stream Bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

client = Client(os.environ["SESSION_NAME"], int(os.environ["API_ID"]), os.environ["API_HASH"])

app = PyTgCalls(client)

OWNER_ID = int(os.environ["OWNER_ID"])

LIVE_CHATS = []

START_TEXT = """━━━━━━━━━━━━━━━━━━━━━━
[🖤](https://telegra.ph/file/086b35ba765a023e18498.jpg) ʀɪʙᴀᴊ, <b>{}</b> 

ᴡᴀxᴀᴀɴ ᴀᴀᴅ ᴜɢᴜ ᴅʜᴇᴇʀᴇᴇʏᴀᴀ ᴠᴄ ᴘʟᴀʏᴇʏ ʙᴏᴛ ᴇᴇ ᴋᴏᴏxᴀʜᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴋᴀ...
ᴅʜᴀᴍᴍᴀᴀɴ ᴀᴍᴀʀʀᴀᴅᴀʏᴅᴀ ᴡᴀᴀ ʟᴀ ɪsᴛɪᴄᴍᴀᴀʟɪ ᴋᴀʀᴀᴀ : /

┏━━━━━━━━━━━━━━━━━┓
┣★ ᴅᴇᴠᴇʟᴏᴘᴇʀ​ : [𝗥𝗜𝗕𝗔𝗝 𝗢𝗦𝗠𝗔𝗡𝗜](tg://user?id=1008271006)
┗━━━━━━━━━━━━━━━━━┛

💙 ʜᴀᴅɪɪ ᴀᴀᴅ ᴡᴀx sᴜ'ᴀᴀʟᴏ ᴀʜ ǫᴀʙᴛɪᴅ •ᴄᴀᴀᴡɪɴᴀᴀᴅ• [ᴏᴡɴᴇʀ](tg://user?id=1008271006) ʜᴏɢᴀᴀᴍɪʏᴇ...
━━━━━━━━━━━━━━━━━━━━━━
"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                        "✪ ᴀᴅᴅ ᴍᴇ ᴛᴏ ᴜᴏʀ ɢʀᴏᴜᴘ ✪", url="https://t.me/Seyriye_os_bot?startgroup=true")
        ],
        [
            InlineKeyboardButton("🇸🇴 sᴜᴘᴘᴏʀᴛ 🇸🇴", url="https://t.me/teamosmani"),
            InlineKeyboardButton("💙 ᴜᴘᴅᴀᴛᴇ 💙", url="https://t.me/osmanigroupbot"),
        ]
    ]
)

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⏸️", callback_data="pause"),
            InlineKeyboardButton("▶️", callback_data="resume"),
            InlineKeyboardButton("⏭️", callback_data="skip"),
            InlineKeyboardButton("⏹️", callback_data="end"),
        ],
        [
            InlineKeyboardButton("• ᴄʟᴏsᴇ​ •", callback_data="close")
        ]
    ]
)

async def skip_current_song(chat_id):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await app.leave_group_call(chat_id)
            clear_queue(chat_id)
            return 1
        else:
            title = chat_queue[1][0]
            duration = chat_queue[1][1]
            link = chat_queue[1][2]
            playlink = chat_queue[1][3]
            type = chat_queue[1][4]
            Q = chat_queue[1][5]
            thumb = chat_queue[1][6]
            if type == "Audio":
                await app.change_stream(
                    chat_id,
                    AudioPiped(
                        playlink,
                    ),
                )
            elif type == "Video":
                if Q == "high":
                    hm = HighQualityVideo()
                elif Q == "mid":
                    hm = MediumQualityVideo()
                elif Q == "low":
                    hm = LowQualityVideo()
                else:
                    hm = MediumQualityVideo()
                await app.change_stream(
                    chat_id, AudioVideoPiped(playlink, HighQualityAudio(), hm)
                )
            pop_an_item(chat_id)
            await bot.send_photo(chat_id, photo = thumb,
                                 caption = f"🕕 <b>ᴅᴜʀᴀᴛɪᴏɴ:</b> {duration}",
                                 reply_markup = BUTTONS)
            return [title, link, type, duration, thumb]
    else:
        return 0


async def skip_item(chat_id, lol):
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        try:
            x = int(lol)
            title = chat_queue[x][0]
            chat_queue.pop(x)
            return title
        except Exception as e:
            print(e)
            return 0
    else:
        return 0


@app.on_stream_end()
async def on_end_handler(_, update: Update):
    if isinstance(update, StreamAudioEnded):
        chat_id = update.chat_id
        await skip_current_song(chat_id)


@app.on_closed_voice_chat()
async def close_handler(client: PyTgCalls, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)
        

async def yt_video(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "best[height<=?720][width<=?1280]",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()
    

async def yt_audio(link):
    proc = await asyncio.create_subprocess_exec(
        "yt-dlp",
        "-g",
        "-f",
        "bestaudio",
        f"{link}",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    if stdout:
        return 1, stdout.decode().split("\n")[0]
    else:
        return 0, stderr.decode()


@bot.on_callback_query()
async def callbacks(_, cq: CallbackQuery):
    user_id = cq.from_user.id
    try:
        user = await cq.message.chat.get_member(user_id)
        admin_strings = ("creator", "administrator")
        if user.status not in admin_strings:
            is_admin = False
        else:
            is_admin = True
    except ValueError:
        is_admin = True        
    if not is_admin:
        return await cq.answer("» ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ʙᴀʙʏ.")   
    chat_id = cq.message.chat.id
    data = cq.data
    if data == "close":
        return await cq.message.delete()
    if not chat_id in QUEUE:
        return await cq.answer("» ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴛ ɪɴ ᴠᴄ ʙᴀʙʏ.")

    if data == "pause":
        try:
            await app.pause_stream(chat_id)
            await cq.answer("» ᴛʀᴀᴄᴋ ᴘᴀᴜsᴇᴅ ʙᴀʙʏ.")
        except:
            await cq.answer("» ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴛ ɪɴ ᴠᴄ ʙᴀʙʏ.")
      
    elif data == "resume":
        try:
            await app.resume_stream(chat_id)
            await cq.answer("» ᴛʀᴀᴄᴋ ʀᴇsᴜᴍᴇᴅ ʙᴀʙʏ.")
        except:
            await cq.answer("» ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴛ ɪɴ ᴠᴄ ʙᴀʙʏ.")   

    elif data == "end":
        await app.leave_group_call(chat_id)
        clear_queue(chat_id)
        await cq.answer("» sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ ʙᴀʙʏ.")  

    elif data == "skip":
        op = await skip_current_song(chat_id)
        if op == 0:
            await cq.answer("» ǫᴜᴇᴜᴇ ᴇᴍᴘᴛʏ ʙᴀʙʏ..")
        elif op == 1:
            await cq.answer("» ǫᴜᴇᴜᴇ ᴇᴍᴘᴛʏ, ᴄʟᴏsᴇᴅ sᴛʀᴇᴀᴍɪɴɢ.")
        else:
            await cq.answer("» ᴛʀᴀᴄᴋ sᴋɪᴘᴘᴇᴅ ʙᴀʙʏ.")
            

@bot.on_message(filters.command("start") & filters.private)
async def start_private(_, message):
    msg = START_TEXT.format(message.from_user.mention)
    await message.reply_text(text = msg,
                             reply_markup = START_BUTTONS)
    

@bot.on_message(filters.command(["ping", "alive"]) & filters.group)
async def start_group(_, message):
    await message.reply_text("🖤 ɪ ᴀᴍ ᴀʟʀᴇᴀᴅʏ ᴀᴡᴀᴋᴇ •ʀɪʙᴀᴊ•​ !")


@bot.on_message(filters.command(["join", "assistant", " userbotjoin"]) & filters.group)
@is_admin
async def start_group(_, message):
    await message.reply_text("ᴜsᴇʀʙᴏᴛ ɢᴏᴛ ꜰʟᴏᴏᴅᴡᴀɪᴛ •ʀɪʙᴀᴊ•, ɪ sᴇɴᴛ ʜɪᴍ ᴛᴏ sʟᴇᴇᴘ ꜰᴏʀ ꜰᴇᴡ ᴍɪɴᴜᴛᴇs, ᴀᴅᴅ @lovelyosmani ᴍᴀɴᴜᴀʟʟʏ sᴏ ᴛʜᴀɴ ɪ ᴄᴀɴ ᴘʟᴀʏ​ !")
    
@bot.on_message(filters.command(["play", "vplay"]) & filters.group)
async def video_play(_, message):
    await message.delete()
    user_id = message.from_user.id
    state = message.command[0].lower()
    try:
        query = message.text.split(None, 1)[1]
    except:
        return await message.reply_text(f"<b>Usage:</b> <code>/{state} [query]</code>")
    chat_id = message.chat.id
    if chat_id in LIVE_CHATS:
        return await message.reply_text("❗️Please send <code>/end</code> to end current live streaming before play songs or videos.")
    
    m = await message.reply_text("» ᴘʀᴏᴄᴇssɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ •ʀɪʙᴀᴊ•...")
    if state == "play":
        damn = AudioPiped
        ded = yt_audio
        doom = "Audio"
    elif state == "vplay":
        damn = AudioVideoPiped
        ded = yt_video
        doom = "Video"
    if "low" in query:
        Q = "low"
    elif "mid" in query:
        Q = "mid"
    elif "high" in query:
        Q = "high"
    else:
        Q = "0"
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        thumb = results[0]["thumbnails"][0]
        duration = results[0]["duration"]
        yt = YouTube(link)
        cap = f"» <b>ɴᴀᴍᴇ:</b> [{yt.title}]({link}) | `{doom}` \n\n🕕 <b>ᴅᴜʀᴀᴛɪᴏɴ:</b> {duration}"
        try:
            ydl_opts = {"format": "bestvideo[height<=720]+bestaudio/best[height<=720]"}
            ydl = youtube_dl.YoutubeDL(ydl_opts)
            info_dict = ydl.extract_info(link, download=False)
            p = json.dumps(info_dict)
            a = json.loads(p)
            playlink = a['formats'][1]['manifest_url']
        except:
            ice, playlink = await ded(link)
            if ice == "0":
                return await m.edit("❗️YTDL ERROR !!!")               
    except Exception as e:
        return await m.edit(str(e))
    
    try:
        if chat_id in QUEUE:
            position = add_to_queue(chat_id, yt.title, duration, link, playlink, doom, Q, thumb)
            caps = f"» [{yt.title}]({link}) <b>ǫᴜᴇᴜᴇᴅ ᴀᴛ {position}</b> ʙᴀʙʏ \n\n🕕 <b>ᴅᴜʀᴀᴛɪᴏɴ:</b> {duration}"
            await message.reply_photo(thumb, caption=caps)
            await m.delete()
        else:            
            await app.join_group_call(
                chat_id,
                damn(playlink),
                stream_type=StreamType().pulse_stream
            )
            add_to_queue(chat_id, yt.title, duration, link, playlink, doom, Q, thumb)
            await message.reply_photo(thumb, caption=cap, reply_markup=BUTTONS)
            await m.delete()
    except Exception as e:
        return await m.edit(str(e))
    
    
@bot.on_message(filters.command(["stream", "vstream"]) & filters.group)
@is_admin
async def stream_func(_, message):
    await message.delete()
    state = message.command[0].lower()
    try:
        link = message.text.split(None, 1)[1]
    except:
        return await message.reply_text(f"<b>Usage:</b> <code>/{state} [link]</code>")
    chat_id = message.chat.id
    
    if state == "stream":
        damn = AudioPiped
        emj = "🎵"
    elif state == "vstream":
        damn = AudioVideoPiped
        emj =📽️"
    m = await message.reply_text("» ᴘʀᴏᴄᴇssɪɴɢ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ •ʀɪʙᴀᴊ•...")
    try:
        if chat_id in QUEUE:
            return await m.edit("❗️Please send <code>/end</code> to end voice chat before live streaming.")
        elif chat_id in LIVE_CHATS:
            await app.change_stream(
                chat_id,
                damn(link)
            )
            await m.edit(f"{emj} Started streaming: [Link]({link})", disable_web_page_preview=True)
        else:    
            await app.join_group_call(
                chat_id,
                damn(link),
                stream_type=StreamType().pulse_stream)
            await m.edit(f"{emj} Started streaming: [Link]({link})", disable_web_page_preview=True)
            LIVE_CHATS.append(chat_id)
    except Exception as e:
        return await m.edit(str(e))


@bot.on_message(filters.command("skip") & filters.group)
@is_admin
async def skip(_, message):
    await message.delete()
    chat_id = message.chat.id
    if len(message.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await message.reply_text("» ǫᴜᴇᴜᴇ ᴇᴍᴘᴛʏ ʙᴀʙʏ..")
        elif op == 1:
            await message.reply_text("» ǫᴜᴇᴜᴇ ᴇᴍᴘᴛʏ, ᴄʟᴏsᴇᴅ sᴛʀᴇᴀᴍɪɴɢ.")
    else:
        skip = message.text.split(None, 1)[1]
        out = "🗑 <b>Removed the following song(s) from the queue:</b> \n"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x == 0:
                    pass
                else:
                    hm = await skip_item(chat_id, x)
                    if hm == 0:
                        pass
                    else:
                        out = out + "\n" + f"<b>» {x}</b> - {hm}"
            await message.reply_text(out)
            
            
@bot.on_message(filters.command(["playlist", "queue"]) & filters.group)
@is_admin
async def playlist(_, message):
    chat_id = message.chat.id
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await message.delete()
            await message.reply_text(
                f"▶️ <b>Now playing:</b> [{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][4]}`",
                disable_web_page_preview=True,
            )
        else:
            out = f"<b>📃 Player queue:</b> \n\n▶️ <b>Now playing:</b> [{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][4]}` \n"
            l = len(chat_queue)
            for x in range(1, l):
                title = chat_queue[x][0]
                link = chat_queue[x][2]
                type = chat_queue[x][4]
                out = out + "\n" + f"<b>» {x}</b> - [{title}]({link}) | `{type}` \n"
            await message.reply_text(out, disable_web_page_preview=True)
    else:
        await message.reply_text("» ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴛ ɪɴ ᴠᴄ •ʀɪʙᴀᴊ•.")
    

@bot.on_message(filters.command("end") & filters.group)
@is_admin
async def end(_, message):
    await message.delete()
    chat_id = message.chat.id
    if chat_id in LIVE_CHATS:
        await app.leave_group_call(chat_id)
        LIVE_CHATS.remove(chat_id)
        return await message.reply_text("» sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ •ʀɪʙᴀᴊ•.")
        
    if chat_id in QUEUE:
        await app.leave_group_call(chat_id)
        clear_queue(chat_id)
        await message.reply_text("» sᴛʀᴇᴀᴍ ᴇɴᴅᴇᴅ •ʀɪʙᴀᴊ•.")
    else:
        await message.reply_text("» ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴛ ɪɴ ᴠᴄ •ʀɪʙᴀᴊ•.")
        

@bot.on_message(filters.command("pause") & filters.group)
@is_admin
async def pause(_, message):
    await message.delete()
    chat_id = message.chat.id
    if chat_id in QUEUE:
        try:
            await app.pause_stream(chat_id)
            await message.reply_text("» ᴛʀᴀᴄᴋ ᴘᴀᴜsᴇᴅ •ʀɪʙᴀᴊ•.")
        except:
            await message.reply_text("» ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴛ ɪɴ ᴠᴄ •ʀɪʙᴀᴊ•.")
    else:
        await message.reply_text("» ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴛ ɪɴ ᴠᴄ •ʀɪʙᴀᴊ•.")
        
        
@bot.on_message(filters.command("resume") & filters.group)
@is_admin
async def resume(_, message):
    await message.delete()
    chat_id = message.chat.id
    if chat_id in QUEUE:
        try:
            await app.resume_stream(chat_id)
            await message.reply_text("» ᴛʀᴀᴄᴋ ʀᴇsᴜᴍᴇᴅ •ʀɪʙᴀᴊ•.")
        except:
            await message.reply_text("» ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴛ ɪɴ ᴠᴄ •ʀɪʙᴀᴊ•.")
    else:
        await message.reply_text("» ᴜsᴇʀʙᴏᴛ ɪs ɴᴏᴛ ɪɴ ᴠᴄ •ʀɪʙᴀᴊ•.")
        
        
@bot.on_message(filters.command("restart"))
async def restart(_, message):
    user_id = message.from_user.id
    if user_id != OWNER_ID:
        return
    await message.reply_text("» <i>ʀᴇsᴛᴀʀᴛɪɴɢ •ʀɪʙᴀᴊ•...</i>")
    os.system(f"kill -9 {os.getpid()} && python3 app.py")
            

app.start()
bot.run()
idle()
