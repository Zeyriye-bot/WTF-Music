from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

stats1 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Sʏsᴛᴇᴍ Sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Sᴛᴏʀᴀɢᴇ Sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bᴏᴛ Sᴛᴀᴛs", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="MᴏɴɢᴏDB Sᴛᴀᴛs", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assɪsᴛᴀɴᴛ Sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats2 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Gᴇɴᴇʀᴀʟ Sᴛᴀᴛs", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="Sᴛᴏʀᴀɢᴇ Sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bᴏᴛ Sᴛᴀᴛs", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="MᴏɴɢᴏDB Sᴛᴀᴛs", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assɪsᴛᴀɴᴛ Sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats3 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Sʏsᴛᴇᴍ Sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Gᴇɴᴇʀᴀʟ Sᴛᴀᴛs", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bᴏᴛ Sᴛᴀᴛs", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="MᴏɴɢᴏDB Sᴛᴀᴛs", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assɪsᴛᴀɴᴛ Sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats4 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Sʏsᴛᴇᴍ Sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Sᴛᴏʀᴀɢᴇ Sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Gᴇɴᴇʀᴀʟ Sᴛᴀᴛs", callback_data=f"gen_stats"
            ),
            InlineKeyboardButton(
                text="MᴏɴɢᴏDB Sᴛᴀᴛs", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assɪsᴛᴀɴᴛ Sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats5 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Sʏsᴛᴇᴍ Sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Sᴛᴏʀᴀɢᴇ Sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bᴏᴛ Sᴛᴀᴛs", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="Gᴇɴᴇʀᴀʟ Sᴛᴀᴛs", callback_data=f"gen_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Assɪsᴛᴀɴᴛ Sᴛᴀᴛs", callback_data=f"assis_stats"
            )
        ],
    ]
)

stats6 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Sʏsᴛᴇᴍ Sᴛᴀᴛs", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="Sᴛᴏʀᴀɢᴇ Sᴛᴀᴛs", callback_data=f"sto_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Bᴏᴛ Sᴛᴀᴛs", callback_data=f"bot_stats"
            ),
            InlineKeyboardButton(
                text="MᴏɴɢᴏDB Sᴛᴀᴛs", callback_data=f"mongo_stats"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Gᴇɴᴇʀᴀʟ Sᴛᴀᴛs", callback_data=f"gen_stats"
            )
        ],
    ]
)


stats7 = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="Gᴇᴛᴛɪɴɢ Assɪsᴛᴀɴᴛ Sᴛᴀᴛs ʙᴀʙʏ...",
                callback_data=f"wait_stats",
            )
        ]
    ]
)
