from datetime import datetime
import os


def time_difference(value):
    """
    Функция сравнивает значение входящего значения даты с сегодняшним числом и возвращает True или False
    """
    date_format_value = datetime.strptime(value, '%d.%m.%Y')
    date_now = datetime.now()
    today_is_the_birthday = date_format_value.day == date_now.day and date_format_value.month == date_now.month
    return today_is_the_birthday


def shutdown():
    """
    Функция выключает сервер
    """
    os.system("shutdown -h now")
