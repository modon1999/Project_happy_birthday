import os
import time


class false_in_sex(Exception):
    """
    Создание класса для обработки ошибок переменной sex класса birthday_record
    """
    pass


class false_in_values_in_a_string(Exception):
    """
    Создание класса для обработки ошибок количества переменных в строке для класса birthday_record
    """
    pass


def notification(title, text):
    """
    Функция вывода уведомления, принимает заголовок и текст
    """
    command = f'''
    notify-send '"{text}" "{title}"'
    '''
    return os.system(command)


def check_date(date, iteration_number):
    """
    Функция провеки параметра даты в файле list_of_birthdays.txt, принимает дату
    и номер итерации в цикле для вывода уведомления
    """
    try:
        time.strptime(date, '%d.%m.%Y')
    except ValueError:
        notification("Ошибка в текстовом файле list_of_birthdays.txt",
                     "Проверьте значение даты в строке " + str(
                         iteration_number) + "!")
        exit()


def check_sex(sex, iteration_number):
    """
    Функция проверки переменной sex класса birthday_record
    """
    try:
        if sex not in ["man", "woman"]:
            raise false_in_sex()
    except false_in_sex:
        notification("Ошибка в текстовом файле list_of_birthdays.txt",
                     "Проверьте значение пола в строке " + str(
                         iteration_number) + "!")
        exit()
    except ValueError:
        notification("Ошибка в текстовом файле list_of_birthdays.txt",
                     "Проверьте значение пола в строке " + str(
                         iteration_number) + "!")
        exit()


def check_len_str(record_of_birthday_boy, iteration_number):
    """
    Функция проверки количества переменных в строке записи в базу данных
    """
    try:
        if len(record_of_birthday_boy) not in [4, 5]:
            raise false_in_values_in_a_string()
    except false_in_values_in_a_string:
        notification("Ошибка в текстовом файле list_of_birthdays.txt",
                     "Проверьте количество значение в строке " + str(
                         iteration_number) + "!")
        exit()
    except ValueError:
        notification("Ошибка в текстовом файле list_of_birthdays.txt",
                     "Проверьте количество значение в строке " + str(
                         iteration_number) + "!")
        exit()
    except TypeError:
        notification("Ошибка в текстовом файле list_of_birthdays.txt",
                     "Проверьте количество значение в строке " + str(
                         iteration_number) + "!")
        exit()
