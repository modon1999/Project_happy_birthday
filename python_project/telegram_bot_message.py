from telethon.sync import TelegramClient
import telebot

bot = telebot.TeleBot('5XXXXXXX:AXXXXXXXXXXXXXXXXXXXXXXX0')
api_hash = '7XXXXXXXXXXXXXXXXXXXXXX8'
api_id = 1XXXXXX7

phone = '+79XXXXXXX4'
username = 'mXXXXXXn'

# (2) Create the client and connect
client = TelegramClient(username, api_id, api_hash)
client.connect()

# Ensure you're authorized
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))
    client.sign_in(password=input('Password: '))


def anyone_congratulation_message():
    """
    Функция для отправки сообщения телеграмм-ботом о том, что сегодня некого поздравлять
    """

    @bot.message_handler(content_types=['text'])
    def anyone_congratulate_message():
        bot.send_message("3XXXXXXXX7", "Сегодня некого поздравлять!")

    anyone_congratulate_message()


def sending_congratulation_message(birthday_boy_username, birthday_boy_full_name, birthday_boy_name,
                                   site_congratulation):
    """
    Функция для отправки сообщения о поздравлении и уведомление телеграмм-бота о неотправленных поздравлениях
    """

    @bot.message_handler(content_types=['text'])
    def complete_congratulation_message():
        bot.send_message("3XXXXXXXX7", "Я поздравил " + birthday_boy_full_name + " с Днем Рождения!")

    @bot.message_handler(content_types=['text'])
    def error_congratulation_message():
        bot.send_message("3XXXXXXXX7",
                         "Я не смог поздравить " + birthday_boy_full_name + " с Днем Рождения! Сайт-поздравление: " + site_congratulation + '!')

    if birthday_boy_username == "unnamed_telegramm":
        error_congratulation_message()

    else:
        client.send_message(birthday_boy_username,
                            birthday_boy_name + '!' + ' Поздравляю с Днем Рождения! Сайт-поздравление: ' + site_congratulation + '! Никита Григорьев.')
        complete_congratulation_message()
