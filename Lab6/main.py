import telebot
import requests

bot = telebot.TeleBot('')

@bot.message_handler(content_types=['text'])
def send_dog_photo(message):
    if message.text == 'Пришли мне собачку':
        url_1 = 'https://dog.ceo/api/breeds/image/random'
        res = requests.get(url=url_1)
        url_2 = res.json()['message']
        bot.send_photo(message.chat.id, url_2)
    else:
        bot.send_message(message.chat.id, 'Попробуй ещё раз')
    
bot.polling(non_stop=True)
