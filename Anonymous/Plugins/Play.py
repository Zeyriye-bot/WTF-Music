import asyncio
from os import path

from pyrogram import filters
from pyrogram.types import (InlineKeyboardMarkup, InputMediaPhoto, Message,
                            Voice)
from youtube_search import YoutubeSearch

import Anonymous
from Anonymous import (BOT_USERNAME, DURATION_LIMIT, DURATION_LIMIT_MIN,
                   MUSIC_BOT_NAME, app, db_mem)
from Anonymous.Core.PyTgCalls.Converter import convert
from Anonymous.Core.PyTgCalls.Downloader import download
from Anonymous.Core.PyTgCalls.Tgdownloader import telegram_download
from Anonymous.Decorators.assistant import AssistantAdd
from Anonymous.Decorators.checker import checker
from Anonymous.Decorators.logger import logging
from Anonymous.Decorators.permission import PermissionCheck
from Anonymous.Database import get_video_limit, get_active_video_chats, is_active_video_chat
from Anonymous.Inline import (playlist_markup, search_markup, search_markup2, livestream_markup,
                          url_markup, url_markup2)
from Anonymous.Utilities.changers import seconds_to_min, time_to_seconds
from Anonymous.Utilities.chat import specialfont_to_normal
from Anonymous.Utilities.stream import start_stream, start_stream_audio
from Anonymous.Utilities.videostream import start_stream_video
from Anonymous.Utilities.theme import check_theme
from Anonymous.Utilities.thumbnails import gen_thumb
from Anonymous.Utilities.url import get_url
from Anonymous.Utilities.youtube import (get_yt_info_id, get_yt_info_query,
                                     get_yt_info_query_slider)

loop = asyncio.get_event_loop()


@app.on_message(
    filters.command(["play", f"play@{BOT_USERNAME}"]) & filters.group
)
@checker
@logging
@PermissionCheck
@AssistantAdd
async def play(_, message: Message):
    await message.delete()
    if message.chat.id not in db_mem:
        db_mem[message.chat.id] = {}
    if message.sender_chat:
        return await message.reply_text(
            "» ʏᴏᴜ'ʀᴇ ᴀɴ __ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ__ ɪɴ ᴛʜɪs ᴄʜᴀᴛ ɢʀᴏᴜᴘ!\nʀᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ ꜰʀᴏᴍ ᴀᴅᴍɪɴ ʀɪɢʜᴛs ʙᴀʙʏ."
        )
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    video = (
        (message.reply_to_message.video or message.reply_to_message.document)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    if audio:
        mystic = await message.reply_text(
            "» ᴘʀᴏᴄᴇssɪɴɢ ᴀᴜᴅɪᴏ... ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ʙᴀʙʏ!"
        )
        try:
            read = db_mem[message.chat.id]["live_check"]
            if read:
                return await mystic.edit("» ʟɪᴠᴇ sᴛʀᴇᴀᴍ sᴛʀᴇᴀᴍɪɴɢ ʙᴀʙʏ, sᴛᴏᴘ ɪᴛ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ")
            else:
                pass
        except:
            pass 
        if audio.file_size > 1073741824:
            return await mystic.edit_text(
                "» ᴀᴜᴅɪᴏ ꜰɪʟᴇ sɪᴢᴇ sʜᴏᴜʟᴅ ʙᴇ ʟᴇss ᴛʜᴀɴ 150 ᴍʙ"
            )
        duration_min = seconds_to_min(audio.duration)
        duration_sec = audio.duration
        if (audio.duration) > DURATION_LIMIT:
            return await mystic.edit_text(
                f"**» ᴅᴜʀᴀᴛɪᴏɴ ʟɪᴍɪᴛ ᴇxᴄᴇᴇᴅᴇᴅ ʙᴀʙʏ**\n\n**ᴀʟʟᴏᴡᴇᴅ ᴅᴜʀᴀᴛɪᴏɴ: **{DURATION_LIMIT_MIN} ᴍɪɴᴜᴛᴇ(s)\n**ʀᴇᴄᴇɪᴠᴇᴅ ᴅᴜʀᴀᴛɪᴏɴ:** {duration_min} ᴍɪɴᴜᴛᴇ(s)"
            )
        file_name = (
            audio.file_unique_id
            + "."
            + (
                (audio.file_name.split(".")[-1])
                if (not isinstance(audio, Voice))
                else "ogg"
            )
        )
        file_name = path.join(path.realpath("downloads"), file_name)
        file = await convert(
            (await message.reply_to_message.download(file_name))
            if (not path.isfile(file_name))
            else file_name,
        )
        return await start_stream_audio(
            message,
            file,
            "smex1",
            "ɢɪᴠᴇɴ ᴀᴜᴅɪᴏ ᴠɪᴀ ᴛᴇʟᴇɢʀᴀᴍ",
            duration_min,
            duration_sec,
            mystic,
        )
    elif video:
        limit = await get_video_limit(141414)
        if not limit:
            return await message.reply_text("**» ɴᴏ ʟɪᴍɪᴛ ᴅᴇꜰɪɴᴇᴅ ꜰᴏʀ ᴠɪᴅᴇᴏ ᴄʜᴀᴛs ʙᴀʙʏ**\n\nsᴇᴛ ᴀ ʟɪᴍɪᴛ ꜰᴏʀ ɴᴜᴍʙᴇʀ ᴏꜰ ᴍᴀxɪᴍᴜᴍ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ᴀʟʟᴏᴡᴇᴅ ᴏɴ ʙᴏᴛ ʙʏ /set_video_limit [ᴏɴʟʏ ꜰᴏʀ sᴜᴅᴏ ᴜsᴇʀs]")
        count = len(await get_active_video_chats())
        if int(count) == int(limit):
            if await is_active_video_chat(message.chat.id):
                pass
            else:
                return await message.reply_text("sᴏʀʀʏ! ʙᴏᴛ ᴏɴʟʏ ᴀʟʟᴏᴡs ʟɪᴍɪᴛᴇᴅ ɴᴜᴍʙᴇʀ ᴏꜰ ᴠɪᴅᴇᴏ ᴄᴀʟʟs ʙᴀʙʏ ᴅᴜᴇ ᴛᴏ ᴄᴘᴜ ᴏᴠᴇʀʟᴏᴀᴅ ɪssᴜᴇs. ᴍᴀɴʏ ᴏᴛʜᴇʀ ᴄʜᴀᴛs ᴀʀᴇ ᴜsɪɴɢ ᴠɪᴅᴇᴏ ᴄᴀʟʟ ʀɪɢʜᴛ ɴᴏᴡ. ᴛʀʏ sᴡɪᴛᴄʜɪɴɢ ᴛᴏ ᴀᴜᴅɪᴏ ᴏʀ ᴛʀʏ ᴀɢᴀɪɴ ʟᴀᴛᴇʀ ʙᴀʙʏ")
        mystic = await message.reply_text(
            "» ᴘʀᴏᴄᴇssɪɴɢ ᴠɪᴅᴇᴏ... ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ʙᴀʙʏ!"
        )
        try:
            read = db_mem[message.chat.id]["live_check"]
            if read:
                return await mystic.edit("» ʟɪᴠᴇ sᴛʀᴇᴀᴍ sᴛʀᴇᴀᴍɪɴɢ ʙᴀʙʏ, sᴛᴏᴘ ɪᴛ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ")
            else:
                pass
        except:
            pass 
        file =  await telegram_download(message, mystic)
        return await start_stream_video(
            message,
            file,
            "Given Video Via Telegram",
            mystic,
        )
    elif url:
        mystic = await message.reply_text("» ᴘʀᴏᴄᴇssɪɴɢ ᴜʀʟ, ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ʙᴀʙʏ...!")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        await mystic.delete()
        buttons = url_markup2(videoid, duration_min, message.from_user.id)
        return await message.reply_photo(
            photo=thumb,
            caption=f"📎ᴛɪᴛʟᴇ: **{title}\n\n⏳ᴅᴜʀᴀᴛɪᴏɴ:** {duration_min} ᴍɪɴᴜᴛᴇs\n\n__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴠɪᴅᴇᴏ](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        if len(message.command) < 2:
            buttons = playlist_markup(
                message.from_user.first_name, message.from_user.id, "abcd"
            )
            await message.reply_photo(
                photo="Utils/Playlist.jpg",
                caption=(
                    "**Usage:** /play [ᴍᴜsɪᴄ ɴᴀᴍᴇ ᴏʀ ʏᴏᴜᴛᴜʙᴇ ʟɪɴᴋ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀᴜᴅɪᴏ]\n\nɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴘʟᴀʏ ᴘʟᴀʏʟɪsᴛs! sᴇʟᴇᴄᴛ ᴛʜᴇ ᴏɴᴇ ꜰʀᴏᴍ ʙᴇʟᴏᴡ."
                ),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            return
        mystic = await message.reply_text("🔍")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        await mystic.delete()
        buttons = url_markup(
            videoid, duration_min, message.from_user.id, query, 0
        )
        return await message.reply_photo(
            photo=thumb,
            caption=f"📎ᴛɪᴛʟᴇ: **{title}\n\n⏳ᴅᴜʀᴀᴛɪᴏɴ:** {duration_min} ᴍɪɴᴜᴛᴇs\n\n__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴠɪᴅᴇᴏ](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
            reply_markup=InlineKeyboardMarkup(buttons),
        )

@app.on_callback_query(filters.regex(pattern=r"MusicStream"))
async def Music_Stream(_, CallbackQuery):
    if CallbackQuery.message.chat.id not in db_mem:
        db_mem[CallbackQuery.message.chat.id] = {}
    try:
        read1 = db_mem[CallbackQuery.message.chat.id]["live_check"]
        if read1:
            return await CallbackQuery.answer("» ʟɪᴠᴇ sᴛʀᴇᴀᴍ sᴛʀᴇᴀᴍɪɴɢ ʙᴀʙʏ, sᴛᴏᴘ ɪᴛ ᴛᴏ ᴘʟᴀʏ ᴍᴜsɪᴄ", show_alert=True)
        else:
            pass
    except:
        pass
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    chat_id = CallbackQuery.message.chat.id
    chat_title = CallbackQuery.message.chat.title
    videoid, duration, user_id = callback_request.split("|")
    if str(duration) == "None":
        buttons = livestream_markup("720", videoid, duration, user_id)
        return await CallbackQuery.edit_message_text("**» ʟɪᴠᴇ sᴛʀᴇᴀᴍɪɴɢ ᴅᴇᴛᴇᴄᴛᴇᴅ ʙᴀʙʏ**\n\nᴡᴀɴᴛ ᴛᴏ ᴘʟᴀʏ ʟɪᴠᴇ sᴛʀᴇᴀᴍ ? ᴛʜɪs ᴡɪʟʟ sᴛᴏᴘ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴏɴɢs(ɪꜰ ᴘʟᴀʏɪɴɢ) ᴀɴᴅ sᴛᴀʀᴛ ʟɪᴠᴇ sᴛʀᴇᴀᴍɪɴɢ ʙᴀʙʏ.", reply_markup=InlineKeyboardMarkup(buttons))
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "» ᴛʜɪs ɪs ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀʙʏ!.", show_alert=True
        )
    await CallbackQuery.message.delete()
    title, duration_min, duration_sec, thumbnail = get_yt_info_id(videoid)
    if duration_sec > DURATION_LIMIT:
        return await CallbackQuery.message.reply_text(
            f"**ᴅᴜʀᴀᴛɪᴏɴ ʟɪᴍɪᴛ ᴇxᴄᴇᴇᴅᴇᴅ**\n\n**ᴀʟʟᴏᴡᴇᴅ ᴅᴜʀᴀᴛɪᴏɴ: **{DURATION_LIMIT_MIN} ᴍɪɴᴜᴛᴇs\n**ʀᴇᴄᴇɪᴠᴇᴅ ᴅᴜʀᴀᴛɪᴏɴ:** {duration_min} ᴍɪɴᴜᴛᴇs"
        )
    await CallbackQuery.answer(f"Processing:- {title[:20]}", show_alert=True)
    mystic = await CallbackQuery.message.reply_text(
        f"**{MUSIC_BOT_NAME} ᴅᴏᴡɴʟᴏᴀᴅᴇʀ**\n\n**ᴛɪᴛʟᴇ:** {title[:50]}\n\n0% ▓▓▓▓▓▓▓▓▓▓▓▓ 100%"
    )
    downloaded_file = await loop.run_in_executor(
        None, download, videoid, mystic, title
    )
    raw_path = await convert(downloaded_file)
    theme = await check_theme(chat_id)
    chat_title = await specialfont_to_normal(chat_title)
    thumb = await gen_thumb(thumbnail, title, user_id, theme, chat_title)
    if chat_id not in db_mem:
        db_mem[chat_id] = {}
    await start_stream(
        CallbackQuery,
        raw_path,
        videoid,
        thumb,
        title,
        duration_min,
        duration_sec,
        mystic,
    )



@app.on_callback_query(filters.regex(pattern=r"Search"))
async def search_query_more(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "Search Your Own Music. You're not allowed to use this button.",
            show_alert=True,
        )
    await CallbackQuery.answer("Searching More Results")
    results = YoutubeSearch(query, max_results=5).to_dict()
    med = InputMediaPhoto(
        media="Utils/Result.JPEG",
        caption=(
            f"1️⃣<b>{results[0]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[0]['id']})__</u>\n\n2️⃣<b>{results[1]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[1]['id']})__</u>\n\n3️⃣<b>{results[2]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[2]['id']})__</u>\n\n4️⃣<b>{results[3]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[3]['id']})__</u>\n\n5️⃣<b>{results[4]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[4]['id']})__</u>"
        ),
    )
    buttons = search_markup(
        results[0]["id"],
        results[1]["id"],
        results[2]["id"],
        results[3]["id"],
        results[4]["id"],
        results[0]["duration"],
        results[1]["duration"],
        results[2]["duration"],
        results[3]["duration"],
        results[4]["duration"],
        user_id,
        query,
    )
    return await CallbackQuery.edit_message_media(
        media=med, reply_markup=InlineKeyboardMarkup(buttons)
    )


@app.on_callback_query(filters.regex(pattern=r"popat"))
async def popat(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    userid = CallbackQuery.from_user.id
    i, query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "» ᴛʜɪs ʙᴜᴛᴛᴏɴ ɪs ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀʙʏ!", show_alert=True
        )
    results = YoutubeSearch(query, max_results=10).to_dict()
    if int(i) == 1:
        buttons = search_markup2(
            results[5]["id"],
            results[6]["id"],
            results[7]["id"],
            results[8]["id"],
            results[9]["id"],
            results[5]["duration"],
            results[6]["duration"],
            results[7]["duration"],
            results[8]["duration"],
            results[9]["duration"],
            user_id,
            query,
        )
        await CallbackQuery.edit_message_text(
            f"6️⃣<b>{results[5]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[5]['id']})__</u>\n\n7️⃣<b>{results[6]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[6]['id']})__</u>\n\n8️⃣<b>{results[7]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[7]['id']})__</u>\n\n9️⃣<b>{results[8]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[8]['id']})__</u>\n\n🔟<b>{results[9]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[9]['id']})__</u>",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        disable_web_page_preview = True
        return
    if int(i) == 2:
        buttons = search_markup(
            results[0]["id"],
            results[1]["id"],
            results[2]["id"],
            results[3]["id"],
            results[4]["id"],
            results[0]["duration"],
            results[1]["duration"],
            results[2]["duration"],
            results[3]["duration"],
            results[4]["duration"],
            user_id,
            query,
        )
        await CallbackQuery.edit_message_text(
            f"1️⃣<b>{results[0]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[0]['id']})__</u>\n\n2️⃣<b>{results[1]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[1]['id']})__</u>\n\n3️⃣<b>{results[2]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[2]['id']})__</u>\n\n4️⃣<b>{results[3]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[3]['id']})__</u>\n\n5️⃣<b>{results[4]['title']}</b>\n  ┗  🔗 <u>__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ](https://t.me/{BOT_USERNAME}?start=info_{results[4]['id']})__</u>",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        disable_web_page_preview = True
        return


@app.on_callback_query(filters.regex(pattern=r"slider"))
async def slider_query_results(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    what, type, query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        return await CallbackQuery.answer(
            "» ᴛʜɪs ʙᴜᴛᴛᴏɴ ɪs ɴᴏᴛ ꜰᴏʀ ʏᴏᴜ ʙᴀʙʏ!.",
            show_alert=True,
        )
    what = str(what)
    type = int(type)
    if what == "F":
        if type == 9:
            query_type = 0
        else:
            query_type = int(type + 1)
        await CallbackQuery.answer("ɢᴇᴛᴛɪɴɢ ɴᴇxᴛ ʀᴇsᴜʟᴛ", show_alert=True)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query_slider(query, query_type)
        buttons = url_markup(
            videoid, duration_min, user_id, query, query_type
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"📎ᴛɪᴛʟᴇ: **{title}\n\n⏳ᴅᴜʀᴀᴛɪᴏɴ:** {duration_min} ᴍɪɴᴜᴛᴇs\n\n__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴠɪᴅᴇᴏ](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
    if what == "B":
        if type == 0:
            query_type = 9
        else:
            query_type = int(type - 1)
        await CallbackQuery.answer("ɢᴇᴛᴛɪɴɢ ᴘʀᴇᴠɪᴏᴜs ʀᴇsᴜʟᴛ", show_alert=True)
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query_slider(query, query_type)
        buttons = url_markup(
            videoid, duration_min, user_id, query, query_type
        )
        med = InputMediaPhoto(
            media=thumb,
            caption=f"📎ᴛɪᴛʟᴇ: **{title}\n\n⏳ᴅᴜʀᴀᴛɪᴏɴ:** {duration_min} Mins\n\n__[ɢᴇᴛ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴠɪᴅᴇᴏ](https://t.me/{BOT_USERNAME}?start=info_{videoid})__",
        )
        return await CallbackQuery.edit_message_media(
            media=med, reply_markup=InlineKeyboardMarkup(buttons)
        )
