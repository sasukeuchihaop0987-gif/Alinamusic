from pyrogram.types import InlineKeyboardButton

import config
from SHUKLAMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="✨ ✚ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ✚",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="📢 ═ ᴜᴘᴅᴀᴛᴇs ═", 
                url="https://t.me/ll_ABOUT_SASUKE_ll"
            ),
            InlineKeyboardButton(
                text="💬 ═ sᴜᴘᴘᴏʀᴛ ═", 
                url="https://t.me/+W3WrSwmHeaY5NjM9"
            ),
        ],
        [
            InlineKeyboardButton(
                text="🎄 ═ ʜᴇʟᴘ ᴀɴᴅ ᴄᴏᴍᴍᴀɴᴅ ═", 
                callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="👑 ═ ᴏᴡɴᴇʀ ═", 
                url="https://t.me/sasuke_qt"
            )
        ],
    ]
    return buttons
 
