import asyncio
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
 

        # ==============================
        # PREMIUM EMOJI IDs
        # ==============================
        PREMIUM_EMOJIS = {
            "sasuke": 6219943402952204798,
            "one": 5935970344413172236,
            "two": 5260567255145539253,
            "three": 6314331120372552664,
            "four": 4938201020091073754,
        }

        async def custom_emoji(emoji_id, fallback):
            try:
                stickers = await app.get_custom_emoji_stickers([emoji_id])

                if stickers and stickers[0].emoji:
                    return (
                        f'<emoji id="{emoji_id}">'
                        f'{stickers[0].emoji}'
                        f'</emoji>'
                    )

            except Exception as ex:
                print(
                    f"Custom emoji {emoji_id} unavailable: {ex}"
                )

            return fallback

        # Get Premium Custom Emojis
        emoji_1 = await custom_emoji(
            PREMIUM_EMOJIS["one"], "🦋"
        )

        emoji_2 = await custom_emoji(
            PREMIUM_EMOJIS["two"], "🦋"
        )

        emoji_3 = await custom_emoji(
            PREMIUM_EMOJIS["three"], "🦋"
        )

        emoji_4 = await custom_emoji(
            PREMIUM_EMOJIS["four"], "🦋"
        )

        sasuke_emoji = await custom_emoji(
            PREMIUM_EMOJIS["sasuke"], "👤"
        )

        # ==============================
        # WELCOME MESSAGE
        # ==============================
        welcome_text = f"""
<blockquote>
{emoji_1} ʜєʏ {message.from_user.mention} {emoji_1}

{emoji_2} ᴡєʟᴄσϻє ᴛσ {app.mention} ♫ ✨
ᴘʀєϻɪᴜϻ | ᴀᴅ-ғʀєє | ᴜʟᴛʀᴧ ꜱϻσσᴛʜ

{emoji_3} ʜɪɢʜ-ǫᴜᴧʟɪᴛʏ ᴍᴜꜱɪᴄ ᴘʟᴧʏєʀ ʙσᴛ
ғσʀ ᴛєʟєɢʀᴧϻ ɢʀσᴜᴘꜱ & ᴄʜᴧηηєʟꜱ

{emoji_4} ɪηꜱᴛᴧηᴛ ꜱᴛʀєᴧϻɪηɢ
{emoji_4} ꜱϻσσᴛʜ ᴘʟᴧʏʙᴧᴄᴋ
{emoji_4} ᴄʀʏꜱᴛᴧʟ ꜱσᴜηᴅ | ησ ʟᴧɢ

{emoji_1} ᴛᴧᴘ ʜєʟᴘ ғσʀ ᴄσϻϻᴧηᴅꜱ

•── ⋅ ⋅ ────── ⋅᯽⋅ ────── ⋅ ⋅ ──•

<a href="https://t.me/sasuke_qt">
{sasuke_emoji} ᴘσᴡєʀєᴅ ʙʏ : 𝛅 ᥲ s 𝛖 𝛋 ᴇ ࿐
</a>
</blockquote>
"""

        # ==============================
        # HELP BUTTON
        # ==============================
        welcome_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🦋 ʜєʟᴘ",
                        url=f"https://t.me/{app.username}?start=help",
                    )
                ]
            ]
        )

        # ==============================
        # SEND WELCOME
        # ==============================
        await message.reply_photo(
            START_IMG_URL,
            caption=welcome_text,
            parse_mode="html",
            reply_markup=welcome_keyboard,
            message_effect_id=random.choice(EFFECT_IDS),
        )

        # ==============================
        # LOGGING
        # ==============================
        if await is_on_off(2):
            await app.send_message(
                chat_id=config.LOGGER_ID,
                text=(
                    f"❖ {message.from_user.mention} "
                    f"ᴊᴜꜱᴛ ꜱᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n"
                    f"<b>๏ ᴜꜱᴇʀ ɪᴅ :</b> "
                    f"<code>{message.from_user.id}</code>\n"
                    f"<b>๏ ᴜꜱᴇʀɴᴀᴍᴇ :</b> "
                    f"@{message.from_user.username}"
                ),
            )
