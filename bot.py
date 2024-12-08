import telebot
from bs4 import BeautifulSoup
import requests

import cv2
from PIL import Image
import pytesseract

# Встановлюємо мову для розпізнавання тексту (необов'язково)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
lang = 'eng'

url = 'https://www.gismeteo.ua/ua/weather-kyiv-4944/now/'
response = requests.get(url, headers={
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
bs = BeautifulSoup(response.text, "lxml")
temp_now = bs.find('div', class_="weather-value")
sel = temp_now.find('temperature-value')
value = sel.get('value')
condition = bs.find('div', 'now-desc')
temp_res = 'Зараз у столиці ' + value.text + '. ' + condition.text
bot = telebot.TeleBot("6261638502:AAGMQRbxtslGCvtqCZwj8HnOF5t-cZXn-FQ")

@bot.message_handler(commands=['tempnow'])
def main(message):
    bot.send_message(message.chat.id, temp_res )
@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, '<--Зайди в меню пиздюк!' )

@bot.message_handler(content_types=['photo'])
def handle_image(message):
    # Отримуємо об'єкт зображення з повідомлення
    image_id = message.photo[-1].file_id

    # Завантажуємо зображення
    image_info = bot.get_file(image_id)
    image_path = image_info.file_path
    downloaded_image = bot.download_file(image_path)

    with open('image.jpg', 'wb') as image_file:

        image_file.write(downloaded_image)

        #Використовуємо pytesseract для розпізнавання тексту
        #custom_config = r'--oem 3 --psm 6 outputbase digits'
        recognized_text = pytesseract.image_to_string(Image.open('image.jpg'), lang=lang)
        result = recognized_text.replace(' ', '')
        #Відправляємо розпізнаний текст користувачеві
        # bot.reply_to(message, f'{recognized_text}')
        bot.reply_to(message, f'keke{result}')


bot.polling(none_stop=True)