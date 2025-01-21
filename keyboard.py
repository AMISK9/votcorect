from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Biografia lui Călin Georgescu", callback_data='biografie')],
        [InlineKeyboardButton("Avere și proprietăți", callback_data='avere')],
        [InlineKeyboardButton("Declarații publice și opinii", callback_data='declaratii')],
        [InlineKeyboardButton("Contradicții și schimbări de poziție", callback_data='contradictii')],
        [InlineKeyboardButton("Relația cu serviciile comuniste și Rusia", callback_data='relatii_rusia')],
        [InlineKeyboardButton("Cum a strâns semnăturile pentru prezidențiale", callback_data='semnaturi')],
        [InlineKeyboardButton("Conexiuni cu ideologia legionară", callback_data='legionarism')],
        [InlineKeyboardButton("Materiale media (video/imagini)", callback_data='media')],
        [InlineKeyboardButton("TikTok și echipa de boți", callback_data='tiktok_boti')],
        [InlineKeyboardButton("Situația geopolitică actuală", callback_data='context_geopolitic')]
    ])

def back_to_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Înapoi la meniul principal", callback_data='back_to_menu')]
    ])