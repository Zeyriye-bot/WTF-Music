from typing import Dict, List, Union

from Anonymous import BOT_ID, app

def PermissionCheck(mystic):

    async def wrapper(_, message):

        a = await app.get_chat_member(message.chat.id, BOT_ID)

        if a.status != "administrator":

            return await message.reply_text(

                "I ɴᴇᴇᴅ ᴛᴏ ʙᴇ ᴀᴅᴍɪɴ ᴡɪᴛʜ sᴏᴍᴇ ᴘᴇʀᴍɪssɪᴏɴs:\n"

                + "\n- **can_manage_voice_chats:** Tᴏ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs ʙᴀʙʏ."

                + "\n- **can_delete_messages:** Tᴏ ᴅᴇʟᴇᴛᴇ ʙᴏᴛ's sᴇᴀʀᴄʜ ᴡᴀsᴛᴀɢᴇ ʙᴀʙʏ."

                + "\n- **can_invite_users**: Fᴏʀ ɪɴᴠɪᴛɪɴɢ ᴀssɪsᴛᴀɴᴛ ᴛᴏ ᴛʜᴇ ᴄʜᴀᴛ ʙᴀʙʏ."

            )

        if not a.can_manage_voice_chats:

            await message.reply_text(

                "I ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴅ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ ʙᴀʙʏ."

                + "\n**ᴘᴇʀᴍɪssɪᴏɴ:** __ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛs__"

            )

            return

        if not a.can_delete_messages:

            await message.reply_text(

                "I ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴅ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ ʙᴀʙʏ."

                + "\n**ᴘᴇʀᴍɪssɪᴏɴ:** __ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs__"

            )

            return

        if not a.can_invite_users:

            await message.reply_text(

                "I ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴛʜᴇ ʀᴇǫᴜɪʀᴇᴅ ᴘᴇʀᴍɪssɪᴏɴs ᴛᴏ ᴘᴇʀғᴏʀᴍ ᴛʜɪs ᴀᴄᴛɪᴏɴ ʙᴀʙʏ."

                + "\n**ᴘᴇʀᴍɪssɪᴏɴ:** __ɪɴᴠɪᴛᴇ ᴜsᴇʀs ᴠɪᴀ ʟɪɴᴋ__"

            )

            return

        return await mystic(_, message)

    return wrapper

