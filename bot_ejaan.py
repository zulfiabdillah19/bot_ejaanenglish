import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from spellchecker import SpellChecker

# Buat stemmer
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# Buat spellchecker untuk bahasa Inggris (pengaturan default)
spell = SpellChecker()

# Fungsi untuk memulai bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Halo! Kirimkan teks bahasa inggris yang ingin kamu perbaiki ejaannya. Created by TobatBerutal')

# Fungsi untuk memperbaiki ejaan
async def correct_spelling(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    words = text.split()
    corrected_words = [spell.correction(word) for word in words]
    corrected_text = ' '.join(corrected_words)
    await update.message.reply_text(corrected_text)

# Fungsi utama untuk menjalankan bot
def main() -> None:
    # Token API bot dari BotFather
    TOKEN = '7479933323:AAHFB3KaXT0O3Kq7_2VsXsBgjr-WVT0vrCI'

    # Mengatur logging
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levellevel)s - %(message)s',
        level=logging.INFO
    )

    # Membangun aplikasi bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Menambahkan handler untuk perintah /start
    application.add_handler(CommandHandler('start', start))

    # Menambahkan handler untuk pesan teks
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, correct_spelling))

    # Mulai bot
    application.run_polling()

if __name__ == '__main__':
    main()
