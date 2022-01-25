from cache.admins import admins
from driver.anonymous import call_py, bot
from pyrogram import Client, filters
from driver.queues import QUEUE, clear_queue
from driver.filters import command, other_filters
from driver.decorators import authorized_users_only
from driver.utils import skip_current_song, skip_item
from program.utils.inline import stream_markup, close_mark, back_mark
from config import BOT_USERNAME, GROUP_SUPPORT, IMG_3, UPDATES_CHANNEL
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)


@Client.on_message(command(["reload", f"reload@{BOT_USERNAME}"]) & other_filters)
@authorized_users_only
async def update_admin(client, message):
    global admins
    new_admins = []
    new_ads = await client.get_chat_members(message.chat.id, filter="administrators")
    for u in new_ads:
        new_admins.append(u.user.id)
    admins[message.chat.id] = new_admins
    await message.reply_text(
        "ðŸ˜Ž Anonymous Music Bot **Reloaded Correctly !**\n **Admin list** successfully **updated !**"
    )


@Client.on_message(command(["skip", f"skip@{BOT_USERNAME}", "vskip"]) & other_filters)
@authorized_users_only
async def skip(client, m: Message):
    await m.delete()
    user_id = m.from_user.id
    chat_id = m.chat.id
    if len(m.command) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await m.reply("Nothing is currently playing baby")
        elif op == 1:
            await m.reply("__Queue__ **is empty.**\n\n**Userbot leaving voice chat baby**")
        elif op == 2:
            await m.reply("**Clearing the Queue**\n\n**Userbot leaving voice chat baby**")
        else:
            buttons = stream_markup(user_id)
            requester = f"[{m.from_user.first_name}](tg://user?id={m.from_user.id})"
            await m.send_photo(
                chat_id,
                photo=f"{IMG_3}",
                reply_markup=InlineKeyboardMarkup(buttons),
                caption=f"**Skipped to the next track baby.**\n\n**Name:** [{op[0]}]({op[1]})\n**Chat:** `{chat_id}`\n**Requested by:** {requester}",
            )
    else:
        skip = m.text.split(None, 1)[1]
        OP = "**Removed song from queue:**"
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
                        OP = OP + "\n" + f"**#{x}** - {hm}"
            await m.reply(OP)


@Client.on_message(
    command(["stop", f"stop@{BOT_USERNAME}", "end", f"end@{BOT_USERNAME}", "vstop"])
    & other_filters
)
@authorized_users_only
async def stop(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await m.reply("The userbot has disconnected from the video chat baby.")
        except Exception as e:
            await m.reply(f"Â« **Error:**\n\n`{e}`")
    else:
        await m.reply("**Nothing is streaming baby**")


@Client.on_message(
    command(["pause", f"pause@{BOT_USERNAME}", "vpause"]) & other_filters
)
@authorized_users_only
async def pause(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await m.reply(
                "**Track paused baby.**\n\n**To resume the stream, use the**\nÂ» /resume command."
            )
        except Exception as e:
            await m.reply(f"Â« **Error:**\n\n`{e}`")
    else:
        await m.reply("**Nothing in streaming baby**")


@Client.on_message(
    command(["resume", f"resume@{BOT_USERNAME}", "vresume"]) & other_filters
)
@authorized_users_only
async def resume(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await m.reply(
                "**Track resumed baby.**\n\n**To pause the stream, use the**\nÂ» /pause command."
            )
        except Exception as e:
            await m.reply(f"Â« **error:**\n\n`{e}`")
    else:
        await m.reply("**Nothing in streaming baby**")


@Client.on_message(
    command(["mute", f"mute@{BOT_USERNAME}", "vmute"]) & other_filters
)
@authorized_users_only
async def mute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await m.reply(
                "**Userbot muted baby.**\n\n**To unmute the userbot, use the**\nÂ» /unmute command."
            )
        except Exception as e:
            await m.reply(f"Â« **error:**\n\n`{e}`")
    else:
        await m.reply("**nothing in streaming baby**")


@Client.on_message(
    command(["unmute", f"unmute@{BOT_USERNAME}", "vunmute"]) & other_filters
)
@authorized_users_only
async def unmute(client, m: Message):
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await m.reply(
                "**Userbot unmuted baby.**\n\n**To mute the userbot, use the**\nÂ» /mute command."
            )
        except Exception as e:
            await m.reply(f"Â« **error:**\n\n`{e}`")
    else:
        await m.reply("**nothing in streaming baby**")


@Client.on_callback_query(filters.regex("cbpause"))
async def cbpause(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("Only admin with manage video chat permission that can tap this button baby!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await query.answer("streaming paused")
            await query.edit_message_text(
                "The streaming has paused", reply_markup=back_mark
            )
        except Exception as e:
            await query.edit_message_text(f"Â« **Error:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("Nothing is currently streaming baby", show_alert=True)


@Client.on_callback_query(filters.regex("cbresume"))
async def cbresume(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("Only admin with manage video chat permission that can tap this button baby!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await query.answer("streaming resumed")
            await query.edit_message_text(
                "The streaming has resumed baby", reply_markup=back_mark
            )
        except Exception as e:
            await query.edit_message_text(f"Â« **Error:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("Nothing is currently streaming baby", show_alert=True)


@Client.on_callback_query(filters.regex("cbstop"))
async def cbstop(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("Only admin with manage video chat permission that can tap this button baby!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await query.edit_message_text("**This streaming has ended baby**", reply_markup=close_mark)
        except Exception as e:
            await query.edit_message_text(f"Â« **Error:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("Nothing is currently streaming baby", show_alert=True)


@Client.on_callback_query(filters.regex("cbmute"))
async def cbmute(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("Only admin with manage video chat permission that can tap this button baby!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.mute_stream(chat_id)
            await query.answer("streaming muted")
            await query.edit_message_text(
                "Userbot succesfully muted baby", reply_markup=back_mark
            )
        except Exception as e:
            await query.edit_message_text(f"Â« **Error:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("Nothing is currently streaming baby", show_alert=True)


@Client.on_callback_query(filters.regex("cbunmute"))
async def cbunmute(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("Only admin with manage video chat permission that can tap this button baby!", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.unmute_stream(chat_id)
            await query.answer("streaming unmuted")
            await query.edit_message_text(
                "Userbot succesfully unmuted baby", reply_markup=back_mark
            )
        except Exception as e:
            await query.edit_message_text(f"Â« **Error:**\n\n`{e}`", reply_markup=close_mark)
    else:
        await query.answer("Nothing is currently streaming baby", show_alert=True)


@Client.on_message(
    command(["volume", f"volume@{BOT_USERNAME}", "vol"]) & other_filters
)
@authorized_users_only
async def change_volume(client, m: Message):
    range = m.command[1]
    chat_id = m.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.change_volume_call(chat_id, volume=int(range))
            await m.reply(
                f"**Volume set to** `{range}`% baby"
            )
        except Exception as e:
            await m.reply(f"Â« **Error:**\n\n`{e}`")
    else:
        await m.reply("**Nothing in streaming baby**")
