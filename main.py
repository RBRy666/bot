import telebot
from telebot import types
bot = telebot.TeleBot('5780986973:AAGlUFYtbCz6elWTsgEjjdXz1ILIw1yJUHI')

@bot.message_handler(commands=['start'])
def start(message):
    user = f'Hi, {message.from_user.first_name}'
    bot.send_message(message.chat.id, user)

# @bot.message_handler()
# def get_user_text(message):
#     if message.text == "Hi":
#         bot.send_message(message.chat.id, "Hi")
#     elif message.text == "id":
#         bot.send_message(message.chat.id, f"Your ID: {message.from_user.id}")
#
#     elif message.text == 'photo':
#         photo = open('icon.jpg', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else: bot.send_message(message.chat.id, "Print 'Hi' or 'id'")

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    bot.send_message(message.chat.id, "Nice photo")


@bot.message_handler(commands=['site'])
def site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Go site', url='https://google.com'))
    bot.send_message(message.chat.id, "You are going to site", reply_markup=markup)
@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    site = types.KeyboardButton("Go to site")
    start = types.KeyboardButton("Start")
    markup.add(site, start)
    bot.send_message(message.chat.id, "Press one of buttons", reply_markup=markup)

bot.polling(none_stop=True)



