from Anonymous import BOT_USERNAME, LOG_GROUP_ID, app
from Anonymous.Database import blacklisted_chats, is_gbanned_user, is_on_off


def checker(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "Yᴏᴜ ᴀʀᴇ ᴀɴ __Aɴᴏɴʏᴍᴏᴜs Aᴅᴍɪɴ__ʙᴀʙʏ !\nRᴇᴠᴇʀᴛ ʙᴀᴄᴋ ᴛᴏ ᴜsᴇʀ ᴀᴄᴄᴏᴜɴᴛ Fᴏʀ ᴀᴅᴍɪɴ ʀɪɢʜᴛs"
            )
        blacklisted_chats_list = await blacklisted_chats()
        if message.chat.id in blacklisted_chats_list:
            await message.reply_text(
                f"**ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ᴄʜᴀᴛ​**\n\nYᴏᴜʀ ᴄʜᴀᴛ ʜᴀs ʙᴇᴇɴ ʙʟᴀᴄᴋʟɪsᴛᴇᴅ ʙʏ sᴜᴅᴏ ᴜsᴇʀs ʙᴀʙʏ. Asᴋ ᴀɴʏ __sᴜᴅᴏ ᴜsᴇʀ​__ ᴛᴏ ᴡʜɪᴛᴇʟɪsᴛ.\nCʜᴇᴄᴋ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ [ꜰʀᴏᴍ ʜᴇʀᴇ](https://t.me/{BOT_USERNAME}?start=sudolist)"
            )
            return await app.leave_chat(message.chat.id)
        if await is_on_off(1):
            if int(message.chat.id) != int(LOG_GROUP_ID):
                return await message.reply_text(
                    f"Bᴏᴛ ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ. Sᴏʀʀʏ ғᴏʀ ᴛʜᴇ ɪɴᴄᴏɴᴠᴇɴɪᴇɴᴄᴇ ʙᴀʙʏ !"
                )
        if await is_gbanned_user(message.from_user.id):
            return await message.reply_text(
                f"**ɢʙᴀɴɴᴇᴅ ᴜsᴇʀ​**\n\nYᴏᴜ'ʀᴇ ɢʙᴀɴɴᴇᴅ ғᴏʀ ᴜsɪɴɢ ᴛʜɪs ʙᴏᴛ ʙᴀʙʏ. Asᴋ ᴀɴʏ __SUDO USER__ ᴛᴏ ᴜɴɢʙᴀɴ.\nCʜᴇᴄᴋ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ [ꜰʀᴏᴍ ʜᴇʀᴇ](https://t.me/{BOT_USERNAME}?start=sudolist)"
            )
        return await mystic(_, message)

    return wrapper


def checkerCB(mystic):
    async def wrapper(_, CallbackQuery):
        blacklisted_chats_list = await blacklisted_chats()
        if CallbackQuery.message.chat.id in blacklisted_chats_list:
            return await CallbackQuery.answer(
                "Blacklisted Chat", show_alert=True
            )
        if await is_on_off(1):
            if int(CallbackQuery.message.chat.id) != int(LOG_GROUP_ID):
                return await CallbackQuery.answer(
                    "Bᴏᴛ ɪs ᴜɴᴅᴇʀ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ. Sᴏʀʀʏ ғᴏʀ ᴛʜᴇ ɪɴᴄᴏɴᴠᴇɴɪᴇɴᴄᴇ ʙᴀʙʏ !",
                    show_alert=True,
                )
        if await is_gbanned_user(CallbackQuery.from_user.id):
            return await CallbackQuery.answer(
                "Yᴏᴜ'ʀᴇ ɢʙᴀɴɴᴇᴅ ʙᴀʙʏ", show_alert=True
            )
        return await mystic(_, CallbackQuery)

    return wrapper
