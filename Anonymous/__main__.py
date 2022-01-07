import asyncio
import importlib
import os
import re

from config import LOG_GROUP_ID
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from rich.console import Console
from rich.table import Table
from youtubesearchpython import VideosSearch

from Anonymous import (ASSID, ASSMENTION, ASSNAME, ASSUSERNAME, BOT_ID, BOT_NAME,
                   BOT_USERNAME, SUDOERS, app, db, userbot)
from Anonymous.Core.Logger.Log import (startup_delete_last, startup_edit_last,
                                   startup_send_new)
from Anonymous.Core.PyTgCalls.Anonymous import run
from Anonymous.Database import get_active_chats, get_sudoers, remove_active_chat
from Anonymous.Inline import private_panel
from Anonymous.Plugins import ALL_MODULES
from Anonymous.Utilities.inline import paginate_modules

loop = asyncio.get_event_loop()
console = Console()
HELPABLE = {}


async def initiate_bot():
    with console.status(
        "[magenta]» ʙᴏᴏᴛɪɴɢ ᴜᴘ ᴛʜᴇ ᴀɴᴏɴʏᴍᴏᴜs ᴍᴜsɪᴄ ʙᴏᴛ...",
    ) as status:
        console.print("» [red]ᴄʟᴇᴀʀɪɴɢ ᴍᴏɴɢᴏᴅʙ ᴄᴀᴄʜᴇ​...")
        try:
            chats = await get_active_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_chat(chat_id)
        except Exception as e:
            console.print("» [red] ᴇʀʀᴏʀ ᴡʜɪʟᴇ ᴄʟᴇᴀɴɪɴɢ ᴍᴏɴɢᴏᴅʙ​.")
        console.print("» [green]ᴍᴏɴɢᴏᴅʙ ᴄʟᴇᴀʀᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ​!\n\n")
        ____ = await startup_send_new("ɪᴍᴘᴏʀᴛɪɴɢ ᴀʟʟ ᴘʟᴜɢɪɴs​...")
        status.update(
            status="[bold blue]» sᴄᴀɴɴɪɴɢ ꜰᴏʀ ᴘʟᴜɢɪɴs", spinner="earth"
        )
        await asyncio.sleep(1.7)
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]» ɪᴍᴘᴏʀᴛɪɴɢ ᴘʟᴜɢɪɴs​...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        await asyncio.sleep(1.2)
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "Anonymous.Plugins." + all_module
            )
            if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
            console.print(
                f">> [bold cyan]sᴜᴄᴄᴇssꜰᴜʟʟʏ ɪᴍᴘᴏʀᴛᴇᴅ​: [green]{all_module}.py"
            )
            await asyncio.sleep(0.2)
        console.print("")
        _____ = await startup_edit_last(____, "ꜰɪɴᴀʟɪsɪɴɢ...")
        status.update(
            status="[bold blue]ɪᴍᴘᴏʀᴛᴀᴛɪᴏɴ ᴄᴏᴍᴘʟᴇᴛᴇᴅ​!",
        )
        await asyncio.sleep(2.4)
        await startup_delete_last(_____)
    console.print(
        "[bold green]ᴄᴏɴɢʀᴀᴛs!! ᴀɴᴏɴʏᴍᴏᴜs ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ​!\n"
    )
    try:
        await app.send_message(
            LOG_GROUP_ID,
            "<b>ᴄᴏɴɢʀᴀᴛs!! ᴀɴᴏɴʏᴍᴏᴜs ᴍᴜsɪᴄ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ​!</b>",
        )
    except Exception as e:
        print(
            "ʙᴏᴛ ʜᴀs ꜰᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇᴅ ᴀs ᴀᴅᴍɪɴ!"
        )
        console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
        return
    a = await app.get_chat_member(LOG_GROUP_ID, BOT_ID)
    if a.status != "administrator":
        print("ᴘʀᴏᴍᴏᴛᴇ ʙᴏᴛ ᴀs ᴀᴅᴍɪɴ ɪɴ ʟᴏɢɢᴇʀ ᴄʜᴀɴɴᴇʟ")
        console.print(f"\n[red]Stopping Bot")
        return
    try:
        await userbot.send_message(
            LOG_GROUP_ID,
            "<b>ᴄᴏɴɢʀᴀᴛs!! ᴀssɪsᴛᴀɴᴛ ʜᴀs sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ​!</b>",
        )
    except Exception as e:
        print(
            "ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ʜᴀs ꜰᴀɪʟᴇᴅ ᴛᴏ ᴀᴄᴄᴇss ᴛʜᴇ ʟᴏɢ ᴄʜᴀɴɴᴇʟ. ᴍᴀᴋᴇ sᴜʀᴇ ᴛʜᴀᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴀᴅᴅᴇᴅ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏ ʏᴏᴜʀ ʟᴏɢ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴘʀᴏᴍᴏᴛᴇᴅ ᴀs ᴀᴅᴍɪɴ​!"
        )
        console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")
        return
    try:
        await userbot.join_chat("fallen_angel_music")
    except:
        pass
    console.print(f"\n┌[red] ʙᴏᴛ sᴛᴀʀᴛᴇᴅ ᴀs​ {BOT_NAME}!")
    console.print(f"├[green] ID :- {BOT_ID}!")
    console.print(f"├[red] ᴀssɪsᴛᴀɴᴛ sᴛᴀʀᴛᴇᴅ ᴀs​ {ASSNAME}!")
    console.print(f"└[green] ID :- {ASSID}!")
    await run()
    console.print(f"\n[red]sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")


home_text_pm = "await message.reply_sticker("CAADBAADWxcAAqbxcR4yeTJRtPe4UAI")"


@app.on_message(filters.command("help") & filters.private)
async def help_command(_, message):
    text, keyboard = await help_parser(message.from_user.mention)
    await app.send_message(message.chat.id, text, reply_markup=keyboard)


@app.on_message(filters.command("start") & filters.private)
async def start_command(_, message):
    if len(message.text.split()) > 1:
        name = (message.text.split(None, 1)[1]).lower()
        if name[0] == "s":
            sudoers = await get_sudoers()
            text = "**__sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ ᴏꜰ ʙᴏᴛ:-__**\n\n"
            j = 0
            for count, user_id in enumerate(sudoers, 1):
                try:
                    user = await app.get_users(user_id)
                    user = (
                        user.first_name if not user.mention else user.mention
                    )
                except Exception:
                    continue
                text += f"➤ {user}\n"
                j += 1
            if j == 0:
                await message.reply_text("ɴᴏ sᴜᴅᴏ ᴜsᴇʀs​")
            else:
                await message.reply_text(text)
        if name == "help":
            text, keyboard = await help_parser(message.from_user.mention)
            await message.delete()
            return await app.send_text(
                message.chat.id,
                text,
                reply_markup=keyboard,
            )
        if name[0] == "i":
            m = await message.reply_text("🔎 ꜰᴇᴛᴄʜɪɴɢ ɪɴꜰᴏ!")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
🔍__**ᴠɪᴅᴇᴏ ᴛʀᴀᴄᴋ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ**__

❇️**Title:** {title}

⏳**ᴅᴜʀᴀᴛɪᴏɴ:** {duration} Mins
👀**ᴠɪᴇᴡs:** `{views}`
⏰**ᴘᴜʙʟɪsʜᴇᴅ ᴛɪᴍᴇ:** {published}
🎥**ᴄʜᴀɴɴᴇʟ ɴᴀᴍᴇ:** {channel}
📎**ᴄʜᴀɴɴᴇʟ ʟɪɴᴋ:** [Visit From Here]({channellink})
🔗**ᴠɪᴅᴇᴏ ʟɪɴᴋ:** [Link]({link})

🖤 __sᴇᴀʀᴄʜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ​ {BOT_NAME}__"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="🎥 ᴡᴀᴛᴄʜ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="🔄 ᴄʟᴏsᴇ", callback_data="close"
                        ),
                    ],
                ]
            )
            await m.delete()
            return await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
    out = private_panel()
    return await message.reply_text(
        home_text_pm,
        reply_markup=InlineKeyboardMarkup(out[1]),
    )


async def help_parser(name, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(paginate_modules(0, HELPABLE, "help"))
    return (
        """ʜᴇʏ{},

ɪ ᴀᴍ {BOT_NAME}, ɪ ᴄᴀɴ ᴘʟᴀʏ sᴏɴɢs ɪɴ ᴛᴇʟᴇɢʀᴀᴍ ʙʏ ᴜsɪɴɢ ᴛᴇʟᴇɢʀᴀᴍ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ꜰᴇᴀᴛᴜʀᴇ.

ᴛᴏ ᴋɴᴏᴡ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs : /ʜᴇʟᴘ
ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /​
""".format(
            first_name=name
        ),
        keyboard,
    )


@app.on_callback_query(filters.regex("shikhar"))
async def shikhar(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


@app.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
    home_match = re.match(r"help_home\((.+?)\)", query.data)
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)
    top_text = f"""ʜᴇʏ {query.from_user.first_name},

ᴛᴏ ᴋɴᴏᴡ ᴀʟʟ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs : /ʜᴇʟᴘ
ᴀʟʟ ᴏꜰ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /​
 """
    if mod_match:
        module = mod_match.group(1)
        text = (
            "{} **{}**:\n".format(
                "ʜᴇʀᴇ's ᴛʜᴇ ʜᴇʟᴘ ꜰᴏʀ​", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="↪️ ʙᴀᴄᴋ​", callback_data="help_back"
                    ),
                    InlineKeyboardButton(
                        text="🔄 ᴄʟᴏsᴇ", callback_data="close"
                    ),
                ],
            ]
        )

        await query.message.edit(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    elif home_match:
        out = private_panel()
        await app.send_message(
            query.from_user.id,
            text=home_text_pm,
            reply_markup=InlineKeyboardMarkup(out[1]),
        )
        await query.message.delete()
    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text,
            reply_markup=keyboard,
            disable_web_page_preview=True,
        )

    return await client.answer_callback_query(query.id)


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
