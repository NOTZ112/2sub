from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🤖 My Name :</b> <a href='https://t.me/kambichat143'>File Sharing Bot</a> \n<b>📝 Join :</b> <a href='https://t.me/kambichat143'>Python 3</a> \n<b>📚 വീഡിയോ :</b> <a href='https://t.me/Kambichat_1'>Pyrogram {__version__}</a> \n<b>🚀 Video :</b> <a href='https://t.me/MaIlu_xxx'>Heroku</a> \n<b>📢 Channel :</b> <a href='https://t.me/MaIlu_xxx'>Madflix Botz</a> \n<b>🧑‍💻 Developer :</b> <a href='tg://user?id={OWNER_ID}'>ബിലാൽ ജോൺ Developer</a>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
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
