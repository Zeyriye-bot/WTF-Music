from config import MUSIC_BOT_NAME, SUPPORT_CHANNEL, SUPPORT_GROUP
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)

from Anonymous import BOT_USERNAME

def setting_markup2():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Aᴜᴅɪᴏ Qᴜᴀʟɪᴛʏ", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Aᴜᴅɪᴏ Vᴏʟᴜᴍᴇ", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Aᴜᴛʜᴏʀɪᴢᴇᴅ Usᴇʀs", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Dᴀsʜʙᴏᴀʀᴅ", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Cʟᴏsᴇ", callback_data="close"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Sᴇᴛᴛɪɴɢs**", buttons



def start_pannel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
        ]
        return f"🎛  **ʜᴇʏ, ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **ʜᴇʏ, ᴛʜɪs ɪs {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ​", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **ʜᴇʏ, ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🔧 Sᴇᴛᴛɪɴɢs", callback_data="settingm"
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ​", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **ʜᴇʏ, ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons


def private_panel():
    if not SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Aᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
        ]
        return f"🎛  **ʜᴇʏ, ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if not SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Aᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **ʜᴇʏ, ᴛʜɪs ɪs {MUSIC_BOT_NAME}*", buttons
    if SUPPORT_CHANNEL and not SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Aᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ​", url=f"{SUPPORT_CHANNEL}"
                ),
            ],
        ]
        return f"🎛  **ʜᴇʏ, ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons = [
            [
                InlineKeyboardButton(
                    text="🗂 Hᴇʟᴘ", callback_data="shikhar"
                ),
            ],
            [
                InlineKeyboardButton(
                    "➕ Aᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ",
                    url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                )
            ],
            [
                InlineKeyboardButton(
                    text="📨Sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ​", url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text="📨Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ", url=f"{SUPPORT_GROUP}"
                ),
            ],
        ]
        return f"🎛  **ʜᴇʏ, ᴛʜɪs ɪs {MUSIC_BOT_NAME}**", buttons


def setting_markup():
    buttons = [
        [
            InlineKeyboardButton(text="🔈 Aᴜᴅɪᴏ Qᴜᴀʟɪᴛʏ", callback_data="AQ"),
            InlineKeyboardButton(text="🎚 Aᴜᴅɪᴏ Vᴏʟᴜᴍᴇ", callback_data="AV"),
        ],
        [
            InlineKeyboardButton(
                text="👥 Aᴜᴛʜᴏʀɪᴢᴇᴅ Usᴇʀs", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="💻 Dᴀsʜʙᴏᴀʀᴅ", callback_data="Dashboard"
            ),
        ],
        [
            InlineKeyboardButton(text="✖️ Cʟᴏsᴇ", callback_data="close"),
            InlineKeyboardButton(text="🔙 Gᴏ Bᴀᴄᴋ", callback_data="okaybhai"),
        ],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Sᴇᴛᴛɪɴɢs**", buttons


def volmarkup():
    buttons = [
        [
            InlineKeyboardButton(
                text="🔄 Rᴇsᴇᴛ Aᴜᴅɪᴏ Vᴏʟᴜᴍᴇ 🔄", callback_data="HV"
            )
        ],
        [
            InlineKeyboardButton(text="🔈 Lᴏᴡ Vᴏʟᴜᴍᴇ", callback_data="LV"),
            InlineKeyboardButton(text="🔉 Mᴇᴅɪᴜᴍ Vᴏʟᴜᴍᴇ", callback_data="MV"),
        ],
        [
            InlineKeyboardButton(text="🔊 Hɪɢʜ Vᴏʟᴜᴍᴇ", callback_data="HV"),
            InlineKeyboardButton(text="🔈 Aᴍᴘʟɪғɪᴇᴅ Vᴏʟᴜᴍᴇ", callback_data="VAM"),
        ],
        [
            InlineKeyboardButton(
                text="🔽 Cᴜsᴛᴏᴍ Vᴏʟᴜᴍᴇ 🔽", callback_data="Custommarkup"
            )
        ],
        [InlineKeyboardButton(text="🔙 Gᴏ Bᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Sᴇᴛᴛɪɴɢs**", buttons


def custommarkup():
    buttons = [
        [
            InlineKeyboardButton(text="+10", callback_data="PTEN"),
            InlineKeyboardButton(text="-10", callback_data="MTEN"),
        ],
        [
            InlineKeyboardButton(text="+25", callback_data="PTF"),
            InlineKeyboardButton(text="-25", callback_data="MTF"),
        ],
        [
            InlineKeyboardButton(text="+50", callback_data="PFZ"),
            InlineKeyboardButton(text="-50", callback_data="MFZ"),
        ],
        [InlineKeyboardButton(text="🔼 Cᴜsᴛᴏᴍ Vᴏʟᴜᴍᴇ 🔼", callback_data="AV")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Sᴇᴛᴛɪɴɢs**", buttons


def usermarkup():
    buttons = [
        [
            InlineKeyboardButton(text="👥 Eᴠᴇʀʏᴏɴᴇ", callback_data="EVE"),
            InlineKeyboardButton(text="🙍 Aᴅᴍɪɴs", callback_data="AMS"),
        ],
        [
            InlineKeyboardButton(
                text="📋 Aᴜᴛʜᴏʀɪᴢᴇᴅ Usᴇʀ Lɪsᴛ", callback_data="USERLIST"
            )
        ],
        [InlineKeyboardButton(text="🔙 Gᴏ Bᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Sᴇᴛᴛɪɴɢs**", buttons


def dashmarkup():
    buttons = [
        [
            InlineKeyboardButton(text="✔️ Uᴘᴛɪᴍᴇ", callback_data="UPT"),
            InlineKeyboardButton(text="💾 Rᴀᴍ", callback_data="RAT"),
        ],
        [
            InlineKeyboardButton(text="💻 ᴄᴘᴜ", callback_data="CPT"),
            InlineKeyboardButton(text="💽 Dɪsᴋ", callback_data="DIT"),
        ],
        [InlineKeyboardButton(text="🔙 Gᴏ Bᴀᴄᴋ", callback_data="settingm")],
    ]
    return f"🔧  **{MUSIC_BOT_NAME} Sᴇᴛᴛɪɴɢs**", buttons
