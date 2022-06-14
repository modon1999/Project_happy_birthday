import additional_def
import class_def_for_error_handling
import def_for_terraform
import telegram_bot_message
import sqlite3


class birthday_record:
    """
    Инициализация класса для создания экземпляров дня рождения и метода сreate для создания сайта-поздравления
    """

    def __init__(self, date_of_birth, name, sex, nickname, telegramm_username, workspace, site_congratulation):
        self.date_of_birth = date_of_birth  # Дата рождения
        self.name = name  # Имя
        self.sex = sex  # Пол
        self.nickname = nickname  # Прозвище
        self.telegramm_username = telegramm_username  # Контакт для телеграмм бота
        self.workspace = workspace  # Workspace, будет заполнен позже после того как будут созданы сайты по количеству сегоднешных дней рождения
        self.site_congratulation = site_congratulation  # Адрес сайта-поздравления, будет заполнен позже после того как будут созданы сайты по количеству сегоднешных дней рождения

    def sending_congratulation_message(self):
        """
        Отправка сообщения о поздравлении и уведомление телеграмм-бота о неотправленных поздравлениях
        """
        telegram_bot_message.sending_congratulation_message(self.telegramm_username, self.name, self.nickname,
                                                            self.site_congratulation)

    def create_site_congratulation(self, iteration_number):
        """
        Создаем сайт поздравление для данного экземпляра класса
        """
        self.workspace, self.site_congratulation = def_for_terraform.create_congratulation(self.nickname, self.sex,
                                                                                           iteration_number)

    def destroy_site_congratulation(self):
        """
        Уничтожаем сайт поздравление для данного экземпляра класса
        """
        def_for_terraform.destroy_congratulation(self.nickname, self.sex, self.workspace)


def create_list_of_birthdays_today(file="list_of_birthdays.db"):
    """
    Функция чтения базы данных и создание списка экземпляров класса birthday_record, возвращает список сегодняшных дней рождения
    """
    connect_db = sqlite3.connect(file)  # Соединение с БД
    cur = connect_db.cursor()
    cur.execute("SELECT * FROM list_birthday;")
    all_results = cur.fetchall()  # Вывод содержимого БД в переменую all_results в виде списка кортеджей

    list_of_birthdays_today = []
    for iteration_number, record_of_list_birthday in enumerate(all_results, 1):
        class_def_for_error_handling.check_date(record_of_list_birthday[3],
                                                iteration_number)  # Проверка параметра даты в файле list_of_birthdays.txt
        class_def_for_error_handling.check_sex(record_of_list_birthday[1],
                                               iteration_number)  # Проверка переменной sex класса birthday_record
        if additional_def.time_difference(
                record_of_list_birthday[3]):  # Проверка соответствия даты рождения с сегоднешней датой
            list_of_birthdays_today.append(birthday_record(record_of_list_birthday[3], record_of_list_birthday[0],
                                                           record_of_list_birthday[1], record_of_list_birthday[2],
                                                           record_of_list_birthday[4],
                                                           "unnamed_workspace", "unnamed_site_congratulation"))
    return list_of_birthdays_today
