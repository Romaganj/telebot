import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from PIL import Image
import pytesseract

# Встановлюємо мову для розпізнавання тексту (необов'язково)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
lang = 'eng'

# Налаштування логування
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Токен вашого бота
TOKEN = '6261638502:AAGMQRbxtslGCvtqCZwj8HnOF5t-cZXn-FQ'

# Створення екземпляру бота
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Обробник команди /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привіт! Надішліть мені зображення, і я розпізнаю текст на ньому.')

# Обробник зображення
def handle_image(update: Update, context: CallbackContext) -> None:
    # Отримуємо об'єкт зображення з повідомлення
    image = update.message.photo[-1].get_file()

    # Завантажуємо зображення
    image_path = 'image.jpg'
    image.download(image_path)

    # Використовуємо pytesseract для розпізнавання тексту
    recognized_text = pytesseract.image_to_string(Image.open(image_path), lang=lang)

    # Відправляємо розпізнаний текст користувачеві
    update.message.reply_text(f'Розпізнаний текст: {recognized_text}')

# Додаємо обробники команд та повідомлень
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

image_handler = MessageHandler(Filters.photo, handle_image)
dispatcher.add_handler(image_handler)

# Запускаємо бота
updater.start_polling()

# Зупиняємо бота при натисканні Ctrl+C
updater.idle()