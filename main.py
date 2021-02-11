 # -*- coding: utf-8 -*-
import telebot
import config
import time
from telebot import types

bot = telebot.TeleBot(config.TOKEN)

print('Бот начал свою работу..')
@bot.message_handler(commands=['start'])
def welcome(message):

	# keyboard
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	menu1 = types.KeyboardButton("💸 Сдать аккаунт 💸")
	menu2 = types.KeyboardButton("🚀 Мануал 🚀")
	menu3 = types.KeyboardButton("🆘 Саппорт 🆘")

	markup.row(menu1)
	markup.row(menu2)
	markup.row(menu3)

	bot.send_message(message.chat.id, "Приветствуем, воркер! \nВ данном боте вы можете сдать ваш тикток аккаунт!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def tiktok(message):
	if message.chat.type == 'private':
		if message.text == '💸 Сдать аккаунт 💸':
				msg = bot.send_message(message.chat.id, "🎰 Введите ваши аккаунты тикток 🎰\n Обязательно в виде https://www.tiktok.com/@(логин)")
				bot.register_next_step_handler(msg, yes)

		if message.text == '🚀 Мануал 🚀':		
			keyboard = types.InlineKeyboardMarkup()
			url_button = types.InlineKeyboardButton(text="Прочитать мануал", url='https://telegra.ph/Manual-o-zarobotke-v-TT-02-09')
			keyboard.add(url_button)
			bot.send_message(message.chat.id, "Чтобы прочитать мануал, нажми на кнопку ниже!", reply_markup=keyboard)
		if message.text == '🆘 Саппорт 🆘':
			bot.send_message(message.chat.id, "Чтобы связаться с тех.поддержкой\nНапиши ему: @" + config.support)

@bot.message_handler(content_types=['text'])
def yes(message):
		bot.send_message(message.chat.id, "Аккаунт успешно сдан!")
		tiktok1 = message.text
		worker = message.from_user.username
		bot.send_message(config.admin_id, "Пришел новый тикток!\nВоркер: @" + worker)
		bot.send_message(config.admin_id, "Ссылка на аккаунт: " + tiktok1)

# RUN
bot.polling(none_stop=True)