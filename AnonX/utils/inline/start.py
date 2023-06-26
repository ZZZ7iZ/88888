from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config



def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="【﻿ اضفني لمجموعتك 】",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="【﻿ الاوامر 】",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="المساعدة", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="【﻿ اضفني لمجموعتك 】",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="【﻿ الاوامر 】", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="【﻿ لتنصيب بوت 】", url=f"https://t.me/bp_bp"
            ),
            InlineKeyboardButton(
                text="【﻿ مطور البوت 】", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙎𝙋𝘼𝙍𝙆", url=f"https://t.me/ZZZ7iZ"
            )
        ],
      
     ]
    return buttons
