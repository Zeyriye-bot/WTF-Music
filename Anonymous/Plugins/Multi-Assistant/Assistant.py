from inspect import getfullargspec

from pyrogram import filters, Client

from pyrogram.raw.functions.messages import DeleteHistory

from pyrogram.types import (CallbackQuery, InlineKeyboardButton,

                            InlineKeyboardMarkup, InlineQueryResultArticle,

                            InlineQueryResultPhoto, InputTextMessageContent,

                            Message)

from Anonymous import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5,

                   ASSISTANT_PREFIX, BOT_ID, BOT_USERNAME, LOG_GROUP_ID,

                   MUSIC_BOT_NAME, SUDOERS, app)

from Anonymous.Database import (approve_pmpermit, disapprove_pmpermit, is_on_off,

                            is_pmpermit_approved)

flood = {}

@Client.on_message(filters.private & filters.incoming & ~filters.service & ~filters.edited & ~filters.me & ~filters.bot & ~filters.via_bot & ~filters.user(SUDOERS))

async def awaiting_message(client, message):

    if await is_on_off(5):

        try:

            await client.forward_messages(

                chat_id = LOG_GROUP_ID,

                from_chat_id = message.from_user.id,

                message_ids = message.message_id

            )

        except Exception as err:

            pass

    user_id = message.from_user.id

    if await is_pmpermit_approved(user_id):

        return

    async for m in client.iter_history(user_id, limit=6):

        if m.reply_markup:

            await m.delete()

    if str(user_id) in flood:

        flood[str(user_id)] += 1

    else:

        flood[str(user_id)] = 1

    if flood[str(user_id)] > 5:

        await message.reply_text("sᴘᴀᴍ ᴅᴇᴛᴇᴄᴛᴇᴅ. ᴜsᴇʀ ʙʟᴏᴄᴋᴇᴅ")

        await client.send_message(

            LOG_GROUP_ID,

            f"**sᴘᴀᴍ ᴅᴇᴛᴇᴄᴛᴇᴅ ʙʟᴏᴄᴋ ᴏɴ ᴀssɪsᴛᴀɴᴛ**\n\n- **ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀ:** {message.from_user.mention}\n- **ᴜsᴇʀ ɪᴅ:** {message.from_user.id}",

        )

        return await client.block_user(user_id)

    await message.reply_text(

        f"ʜᴇʏ, ᴛʜɪs ᴛʜɪs {MUSIC_BOT_NAME}'s ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ʙᴀʙʏ.\n\nᴅᴏɴ'ᴛ sᴘᴀᴍ ʜᴇʀᴇ ʙᴀʙʏ ᴇʟsᴇ ʏᴏᴜ ᴡɪʟʟ ɢᴇᴛ ꜰᴜ*ᴋᴇᴅ ʙʏ [Anonymous](https://t.me/anonymous_was_bot).\nꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏ: @{BOT_USERNAME}"

    )

@Client.on_message(filters.command("approve", prefixes=ASSISTANT_PREFIX) & filters.user(SUDOERS) & ~filters.via_bot)

async def pm_approve(client, message):

    if not message.reply_to_message:

        return await eor(

            message, text="ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴛᴏ ᴀᴘᴘʀᴏᴠᴇ ʙᴀʙʏ."

        )

    user_id = message.reply_to_message.from_user.id

    if await is_pmpermit_approved(user_id):

        return await eor(message, text="ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ ʙᴀʙʏ")

    await approve_pmpermit(user_id)

    await eor(message, text="ᴜsᴇʀ ɪs ᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ ʙᴀʙʏ")

@Client.on_message(filters.command("disapprove", prefixes=ASSISTANT_PREFIX) & filters.user(SUDOERS) & ~filters.via_bot)

async def pm_disapprove(client, message):

    if not message.reply_to_message:

        return await eor(

            message, text="ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴛᴏ ᴅɪsᴀᴘᴘʀᴏᴠᴇ ʙᴀʙʏ."

        )

    user_id = message.reply_to_message.from_user.id

    if not await is_pmpermit_approved(user_id):

        await eor(message, text="ᴜsᴇʀ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ ʙᴀʙʏ")

        async for m in client.iter_history(user_id, limit=6):

            if m.reply_markup:

                try:

                    await m.delete()

                except Exception:

                    pass

        return

    await disapprove_pmpermit(user_id)

    await eor(message, text="ᴜsᴇʀ ɪs ᴅɪsᴀᴘᴘʀᴏᴠᴇᴅ ᴛᴏ ᴘᴍ ʙᴀʙʏ")

@Client.on_message(filters.command("block", prefixes=ASSISTANT_PREFIX) & filters.user(SUDOERS) & ~filters.via_bot)

async def block_user_func(client, message):

    if not message.reply_to_message:

        return await eor(message, text="ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴛᴏ ʙʟᴏᴄᴋ ʙᴀʙʏ.")

    user_id = message.reply_to_message.from_user.id

    await eor(message, text="sᴜᴄᴄᴇssꜰᴜʟʟʏ ʙʟᴏᴄᴋᴇᴅ ᴄʜᴜᴛɪʏᴀ")

    await client.block_user(user_id)

@Client.on_message(filters.command("unblock", prefixes=ASSISTANT_PREFIX) & filters.user(SUDOERS) & ~filters.via_bot)

async def unblock_user_func(client, message):

    if not message.reply_to_message:

        return await eor(

            message, text="ʀᴇᴘʟʏ ᴛᴏ ᴜsᴇʀ's ᴍᴇssᴀɢᴇ ᴛᴏ ᴜɴʙʟᴏᴄᴋʙᴀʙʏ."

        )

    user_id = message.reply_to_message.from_user.id

    await client.unblock_user(user_id)

    await eor(message, text="sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴜɴʙʟᴏᴄᴋᴇᴅ ʙᴀʙʏ")

@Client.on_message(filters.command("pfp", prefixes=ASSISTANT_PREFIX) & filters.user(SUDOERS) & ~filters.via_bot)

async def set_pfp(client, message):

    if not message.reply_to_message or not message.reply_to_message.photo:

        return await eor(message, text="ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘɪᴄ ʙᴀʙʏ.")

    photo = await message.reply_to_message.download()

    try:

        await client.set_profile_photo(photo=photo)

        await eor(message, text="sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴘꜰᴘ ʙᴀʙʏ.")

    except Exception as e:

        await eor(message, text=e)

@Client.on_message(filters.command("bio", prefixes=ASSISTANT_PREFIX) & filters.user(SUDOERS) & ~filters.via_bot)

async def set_bio(client, message):

    if len(message.command) == 1:

        return await eor(message, text="ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ʙɪᴏ ʙᴀʙʏ.")

    elif len(message.command) > 1:

        bio = message.text.split(None, 1)[1]

        try:

            await client.update_profile(bio=bio)

            await eor(message, text="sᴜᴄᴄᴇssꜰᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ʙɪᴏ.")

        except Exception as e:

            await eor(message, text=e)

    else:

        return await eor(message, text="ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴛᴏ sᴇᴛ ɪᴛ ᴀs ʙɪᴏ ʙᴀʙʏ.")

async def eor(msg: Message, **kwargs):

    func = (

        (msg.edit_text if msg.from_user.is_self else msg.reply)

        if msg.from_user

        else msg.reply

    )

    spec = getfullargspec(func.__wrapped__).args

    return await func(**{k: v for k, v in kwargs.items() if k in spec})
