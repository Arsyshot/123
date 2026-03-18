import telebot
from telebot import types

# Токен от @BotFather
TOKEN = "8688973097:AAFJUVbF_irhinxSNhxfoIJucz3BLf-pu54"  # ВСТАВЬТЕ СВОЙ ТОКЕН

# Создаем бота
bot = telebot.TeleBot(TOKEN)


# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Создаем клавиатуру
    keyboard = types.InlineKeyboardMarkup(row_width=1)

    # Добавляем кнопки
    btn1 = types.InlineKeyboardButton("🔢 Математика", callback_data="math")
    btn2 = types.InlineKeyboardButton("🎨 Рисование", callback_data="art")
    btn3 = types.InlineKeyboardButton("⚽ Спорт", callback_data="sport")
    btn4 = types.InlineKeyboardButton("💬 Общение", callback_data="social")

    keyboard.add(btn1, btn2, btn3, btn4)

    # Отправляем сообщение с кнопками
    bot.send_message(
        message.chat.id,
        "👋 Привет! Я помогу тебе выбрать профессию.\n\n"
        "Выбери, что тебе интересно:",
        reply_markup=keyboard
    )


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    # Убираем "часики" на кнопке
    bot.answer_callback_query(call.id)

    # Определяем текст ответа
    if call.data == "math":
        text = "🔢 Тебе подойдут профессии:\n\n• Программист\n• Аналитик данных\n• Инженер\n• Финансовый аналитик"
    elif call.data == "art":
        text = "🎨 Тебе подойдут профессии:\n\n• Дизайнер\n• Архитектор\n• Художник-иллюстратор\n• UX/UI-специалист"
    elif call.data == "sport":
        text = "⚽ Тебе подойдут профессии:\n\n• Фитнес-тренер\n• Спортивный врач\n• Организатор мероприятий\n• Физический терапевт"
    elif call.data == "social":
        text = "💬 Тебе подойдут профессии:\n\n• Психолог\n• Педагог\n• HR-специалист\n• Журналист"
    else:
        text = "Попробуй выбрать другой вариант!"

    # Отправляем сообщение
    bot.send_message(call.message.chat.id, text)


# Запускаем бота
if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()