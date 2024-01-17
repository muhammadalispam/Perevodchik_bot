from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def translate_language_inline():
    btn = InlineKeyboardMarkup(row_width=3)

    btn.add(
        InlineKeyboardButton(
            text="🇷🇺Rus", callback_data="lang:ru"
        ),
        InlineKeyboardButton(
            text="🇺🇿Uzb", callback_data="lang:uz"
        ),
        InlineKeyboardButton(
            text="🇺🇸Eng", callback_data="lang:en"
        ),
        InlineKeyboardButton(
            text="Arab", callback_data="lang:ar"
        ),
        InlineKeyboardButton(
            text="Garman", callback_data="lang:de"
        ),
        InlineKeyboardButton(
            text="Hind", callback_data="lang:hi"
        ),
        InlineKeyboardButton(
            text="Indonaziya", callback_data="lang:id"
        ),
        InlineKeyboardButton(
            text="Italyan", callback_data="lang:it"
        ),
        InlineKeyboardButton(
            text="Koreys", callback_data="lang:ko"
        ),
        InlineKeyboardButton(
            text="Norvegiya", callback_data="lang:no"
        ),
        InlineKeyboardButton(
            text="Polsha", callback_data="lang:pl"
        ),
        InlineKeyboardButton(
            text="Portugal", callback_data="lang:pt"
        ),
        InlineKeyboardButton(
            text="Spanish", callback_data="lang:es"
        ),
        InlineKeyboardButton(
            text="Turk", callback_data="lang:tr"
        ),
        InlineKeyboardButton(
            text="Ukrain", callback_data="lang:uk"
        )
    )
    return btn
