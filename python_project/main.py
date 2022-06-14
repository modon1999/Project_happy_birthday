import class_for_create_congratulation
import telegram_bot_message
import additional_def
import schedule
import time

list_of_birthdays_today = class_for_create_congratulation.create_list_of_birthdays_today()  # Создание экземпляров классов из записей, у кого сегодня день рождение

i = 0
for item in list_of_birthdays_today:
    list_of_birthdays_today[i].create_site_congratulation(i)  # Создание сайтов-поздравлений
    list_of_birthdays_today[i].sending_congratulation_message()  # Отправка сообщений поздравлений
    i = i + 1


def job_that_executes_once(list_of_birthdays_today):
    """
    Удаление сайтов и выключение сервера
    """
    i = 0
    for item in list_of_birthdays_today:
        list_of_birthdays_today[i].destroy_site_congratulation()
        i = i + 1
    additional_def.shutdown()
    return schedule.CancelJob


schedule.every().day.at('20:00').do(job_that_executes_once,
                                    list_of_birthdays_today)  # Функция сработает в 20 часов по серверному времени

if list_of_birthdays_today != []:
    while True:
        schedule.run_pending()
        time.sleep(10)
else:
    telegram_bot_message.anyone_congratulation_message()  # Если поздравлять некого, то отсылает сообщение от том, что поздровлять сегодня некого
