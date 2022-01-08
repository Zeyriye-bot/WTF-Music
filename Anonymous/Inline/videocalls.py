from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

def choose_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎵 ᴘʟᴀʏ ᴀᴜᴅɪᴏ",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 ᴘʟᴀʏ ᴠɪᴅᴇᴏ​",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            )
        ],
        [
            InlineKeyboardButton(
                text="😶 ᴄʟᴏsᴇ sᴇᴀʀᴄʜ​",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

def livestream_markup(quality, videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="📽  sᴛᴀʀᴛ ʟɪᴠᴇ​",
                callback_data=f"LiveStream {quality}|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="😶 ᴄʟᴏsᴇ sᴇᴀʀᴄʜ​",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

def stream_quality_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="😘“½ 360P",
                callback_data=f"VideoStream 360|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="😫“½ 720P",
                callback_data=f"VideoStream 720|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="😁“½ 480P",
                callback_data=f"VideoStream 480|{videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="😶 ᴄʟᴏsᴇ sᴇᴀʀᴄʜ​",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons