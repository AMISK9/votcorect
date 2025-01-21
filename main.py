from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TOKEN
from handlers.handlers import start_command, help_command, custom_command, button_callback, handle_message

if __name__ == "__main__":
    print("Pornire bot...")
    app = Application.builder().token(TOKEN).build()

    print("Bot configurat. Adăugare handleri...")

    # Comenzi
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("ajutor", help_command))
    app.add_handler(CommandHandler("personalizat", custom_command))

    # Butoane inline
    app.add_handler(CallbackQueryHandler(button_callback))

    # Mesaje libere
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Handleri adăugați. Bot în execuție...")

    # Pornire bot
    app.run_polling()