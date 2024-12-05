import telebot
from datetime import datetime


TOKEN = '7675150046:AAF3y-zPC5Z5YKfVdQwXyk8iCDsDO89Pb5M'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне дату в формате ГГГГ-ММ-ДД, и я скажу тебе, сколько дней, часов и минут до этой даты.")

@bot.message_handler(func=lambda message: True)
def calculate_time_diff(message):
    try:
        # Попытка преобразовать текст сообщения в дату
        target_date = datetime.strptime(message.text, '%Y-%m-%d')
        now = datetime.now()

        if target_date <= now:
            bot.reply_to(message, "Эта дата уже прошла. Пожалуйста, введите будущую дату.")
            return

        # Вычисление разницы времени
        time_difference = target_date - now
        days = time_difference.days
        seconds_remaining = time_difference.seconds
        hours = seconds_remaining // 3600
        minutes = (seconds_remaining % 3600) // 60

        # Формирование ответа
        response = f"До даты {target_date.date()} осталось {days} дней, {hours} часов и {minutes} минут."
        bot.reply_to(message, response)
    except ValueError:
        bot.reply_to(message, "Пожалуйста, введите дату корректно в формате ГГГГ-ММ-ДД.")

# Запуск бота   
if __name__ == '__main__':
    bot.polling(none_stop=True)