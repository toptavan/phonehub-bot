import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "8521093134:AAFOgWnFJvgkzD7Rs0p0yhFEy3z0LQa4vYE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("Россия", callback_data="ru"),
                InlineKeyboardButton("Украина", callback_data="ua"),
                InlineKeyboardButton("Казахстан", callback_data="kz"))
    bot.send_message(message.chat.id, "Выбери страну для SIP-номера:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f"Конфиг {call.data.upper()} отправлен в ЛС!")

print("Бот запущен!")
bot.infinity_polling()
