from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data

    if data == "about":

        # 🔴 BOT NAME
        bot_name = "ആതിര"

        # 🔴 BOT USERNAME
        # @ വേണ്ട
        # ഉദാഹരണം: @AshwathyFileBot ആണെങ്കിൽ ഇവിടെ AshwathyFileBot മാത്രം
        bot_username = "AthiraxBot"

        bot_link = f"https://t.me/{bot_username}"

        await query.message.edit_text(
            text=f"<b>🤖 My Name :</b> "
                 f"<a href='{bot_link}'>{bot_name}</a>\n"
                 f"<b>📝 Join :</b> "
                 f"<a href='https://t.me/kambichat143'>Python 3</a>\n"
                 f"<b>📚 വീഡിയോ :</b> "
                 f"<a href='https://t.me/Kambichat_1'>Pyrogram {__version__}</a>\n"
                 f"<b>🚀 Video :</b> "
                 f"<a href='https://t.me/MaIlu_xxx'>Heroku</a>\n"
                 f"<b>📢 Channel :</b> "
                 f"<a href='https://t.me/MaIlu_xxx'>Madflix Botz</a>\n"
                 f"<b>🧑‍💻 Developer :</b> "
                 f"<a href='tg://user?id={OWNER_ID}'>ബിലാൽ ജോൺ Developer</a>",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🔒 Close",
                            callback_data="close"
                        )
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()

        try:
            await query.message.reply_to_message.delete()
        except:
            pass


# Jishu Developer
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
