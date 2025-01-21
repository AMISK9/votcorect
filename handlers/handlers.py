from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, CommandHandler, MessageHandler, filters
from messages import Messages
from keyboard import main_menu_keyboard
from handlers.biografie import send_biografie  # Importă funcția pentru secțiunea „Biografie”
from handlers.avere import send_avere  # Importă funcția pentru secțiunea „Avere și proprietăți”
from handlers.declaratii import send_declaratii
from handlers.contradictii import send_contradictii
from handlers.relatii_rusia import send_relatii_rusia

# Dicționar global pentru a stoca ultimul mesaj al fiecărui utilizator
user_last_message = {}

async def delete_previous_message(context, chat_id):
    """Șterge ultimul mesaj trimis de bot utilizatorului, dacă există."""
    if chat_id in user_last_message:
        try:
            message_id = user_last_message[chat_id]
            await context.bot.delete_message(chat_id, message_id)
        except Exception as e:
            print(f"Nu s-a putut șterge mesajul: {e}")
        finally:
            user_last_message.pop(chat_id, None)  # Elimină mesajul după încercare

async def send_new_message(context, chat_id, text, reply_markup=None, parse_mode=None):
    """Trimite un mesaj nou și actualizează `user_last_message`."""
    message = await context.bot.send_message(
        chat_id=chat_id,
        text=text,
        reply_markup=reply_markup,
        parse_mode=parse_mode
    )
    user_last_message[chat_id] = message.message_id  # Salvează ID-ul mesajului

async def start_command(update: Update, context):
    """Gestionează comanda /start."""
    chat_id = update.effective_chat.id
    await delete_previous_message(context, chat_id)  # Șterge mesajul anterior

    # Trimite meniul principal
    await send_new_message(
        context,
        chat_id,
        Messages.START_MESSAGE,
        reply_markup=main_menu_keyboard()
    )

async def help_command(update: Update, context):
    """Gestionează comanda /ajutor."""
    chat_id = update.effective_chat.id
    await delete_previous_message(context, chat_id)  # Șterge mesajul anterior

    # Trimite mesajul de ajutor
    await send_new_message(context, chat_id, Messages.HELP_MESSAGE)

async def custom_command(update: Update, context):
    """Gestionează o comandă personalizată."""
    chat_id = update.effective_chat.id
    await delete_previous_message(context, chat_id)  # Șterge mesajul anterior

    # Trimite mesaj personalizat
    await send_new_message(context, chat_id, 'Comanda personalizată.')

async def button_callback(update: Update, context):
    """Gestionează apăsarea butoanelor din meniu."""
    query = update.callback_query
    chat_id = query.message.chat_id

    await delete_previous_message(context, chat_id)  # Șterge mesajul anterior
    await query.answer()

    # Opțiuni din meniu
    if query.data == 'biografie':
        # Redirecționează către funcția din biografie.py
        await send_biografie(update, context)
    elif query.data == 'avere':
        # Redirecționează către funcția din avere.py
        await send_avere(update, context)
    elif query.data == 'declaratii':
        await send_declaratii(update, context)
    elif query.data == 'contradictii':
        await send_contradictii(update, context)
    elif query.data == 'relatii_rusia':
        await send_relatii_rusia(update, context)
    elif query.data == 'semnaturi':
        await send_new_message(
            context,
            chat_id,
            text=(
                "*Cum a strâns semnături*\n\n"
                "Detalii despre procesul de colectare a semnăturilor pentru candidatura sa."
            ),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Înapoi către meniul principal", callback_data='back_to_menu')]
            ])
        )
    elif query.data == 'legionarism':
        await send_new_message(
            context,
            chat_id,
            text=(
                "*Conexiuni cu ideologia legionară*\n\n"
                "Analiză a discursurilor și afilierilor lui Călin Georgescu."
            ),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Înapoi către meniul principal", callback_data='back_to_menu')]
            ])
        )
    elif query.data == 'media':
        await send_new_message(
            context,
            chat_id,
            text=(
                "*Materiale media*\n\n"
                "Accesează videoclipuri și imagini relevante despre activitatea sa."
            ),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Înapoi către meniul principal", callback_data='back_to_menu')]
            ])
        )
    elif query.data == 'tiktok_boti':
        await send_new_message(
            context,
            chat_id,
            text=(
                "*TikTok și echipe de boți*\n\n"
                "Detalii despre utilizarea TikTok și strategiile de promovare."
            ),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Înapoi către meniul principal", callback_data='back_to_menu')]
            ])
        )
    elif query.data == 'context_geopolitic':
        await send_new_message(
            context,
            chat_id,
            text=(
                "*Situația geopolitică actuală*\n\n"
                "Analiză a discursului său în context geopolitic actual."
            ),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Înapoi către meniul principal", callback_data='back_to_menu')]
            ])
        )
    elif query.data == 'back_to_menu':
        # Revine la meniul principal
        await send_new_message(
            context,
            chat_id,
            Messages.BACK_TO_MENU,
            reply_markup=main_menu_keyboard()
        )

async def handle_message(update: Update, context):
    """Gestionează mesajele text libere."""
    chat_id = update.effective_chat.id
    await delete_previous_message(context, chat_id)  # Șterge mesajul anterior

    text = update.message.text.lower()

    # Răspunsuri bazate pe cuvinte-cheie
    if 'salut' in text:
        response = Messages.GREETING_REPLY
    elif 'ce faci' in text:
        response = "Sunt bine, mulțumesc! Cum te pot ajuta?"
    elif 'ajutor' in text or 'help' in text:
        response = Messages.HELP_MESSAGE
    elif 'cine esti' in text:
        response = "Sunt un bot care te ajută să te informezi corect despre alegeri și să previi dezinformarea."
    elif 'multumesc' in text:
        response = "Cu plăcere! Dacă ai nevoie de ajutor, sunt aici."
    elif 'bye' in text or 'la revedere' in text:
        response = Messages.BYE_REPLY
    else:
        response = Messages.UNRECOGNIZED_REPLY

    # Trimite răspunsul
    await send_new_message(context, chat_id, response)