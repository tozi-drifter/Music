import re
from pyrogram import filters
import random
from DAXXMUSIC import app


@app.on_message(filters.command(["gn","n","oodnight","ood Night","ood night"], prefixes=["/","g","G"]))
def goodnight_command_handler(_, message):
    sender = message.from_user.mention
    send_sticker = random.choice([True, False])
    if send_sticker:
        sticker_id = get_random_sticker()
        app.send_sticker(message.chat.id, sticker_id)
        message.reply_text(f"Goodnight, {sender}! Sleep tight. 🌙")
    else:
        emoji = get_random_emoji()
        app.send_message(message.chat.id, emoji)
        message.reply_text(f"Goodnight, {sender}! Sleep tight. {emoji}")


def get_random_sticker():
    stickers = [
        "CAACAgUAAxkBAAI9hmXw2tzh9xyHRSljDUQQsIjd0IX-AAJkCAAC0vBpVtXQG48anAPxHgQ", # Sticker 1
        "CAACAgUAAxkBAAI9i2Xw2wxG0CM6xcJRzA2OiOcAAZdiMwACSwcAAvqZWVT5N90fK8dgEx4E", # Sticker 2
        "CAACAgIAAx0Ce9_hCAACaFBlwn8AAZNB9mOUvz5oAyM7CT-5pjAAAtEKAALa7NhLvbTGyDLbe1IeBA", # Sticker 3
        "CAACAgUAAx0CcmOuMwACldVlwn9ZHHF2-S-CuMSYabwwtVGC3AACOAkAAoqR2VYDjyK6OOr_Px4E",
        "CAACAgIAAx0Ce9_hCAACaFVlwn-fG58GKoEmmZpVovxEj4PodAACfwwAAqozQUrt2xSTf5Ac4h4E",
    ]
    return random.choice(stickers)


def get_random_emoji():
    emojis = [
        "😴",
        "😪",
        "💤",
    ]
    return random.choice(emojis)
