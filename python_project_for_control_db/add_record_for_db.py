import sqlite3
import class_def_for_error_handling

"""
Добавление записей в базу данных из текстового файла list_of_birthdays.txt
"""

conn = sqlite3.connect('./list_of_birthdays.db')

cur = conn.cursor()

cur.execute("SELECT * FROM list_birthday;")
all_results = cur.fetchall()
list_of_birthday_boy = []
for record in all_results:
    list_of_birthday_boy.append(record[0])

file = 'list_of_birthdays.txt'
list_to_add_in_db = []
with open(file) as f:
    for iteration_number, line in enumerate(f, 1):
        line = line.strip()
        if len(line) == 0:  # Если строка пуста, то пропускает её
            continue
        record_of_birthday_boy = line.split(" ")
        record_of_birthday_boy[1] = record_of_birthday_boy[1].replace("_", " ")
        record_of_birthday_boy[3] = record_of_birthday_boy[3].replace("_", " ")
        class_def_for_error_handling.check_date(record_of_birthday_boy[0],
                                                iteration_number)  # Проверка параметра даты в файле list_of_birthdays.txt
        class_def_for_error_handling.check_sex(record_of_birthday_boy[2],
                                               iteration_number)  # Проверка переменной sex класса birthday_record
        class_def_for_error_handling.check_len_str(record_of_birthday_boy,
                                                   iteration_number)  # Проверка количества переменных в строке записи в базу данных
        if len(record_of_birthday_boy) == 4:
            record_of_birthday_boy.append('unnamed_telegramm')
        if record_of_birthday_boy[1] not in list_of_birthday_boy:
            list_for_help_add = []
            list_for_help_add.append(record_of_birthday_boy[1])
            list_for_help_add.append(record_of_birthday_boy[2])
            list_for_help_add.append(record_of_birthday_boy[3])
            list_for_help_add.append(record_of_birthday_boy[0])
            list_for_help_add.append(record_of_birthday_boy[4])
            list_to_add_in_db.append(list_for_help_add)

if list_to_add_in_db != []:
    cur.executemany("INSERT INTO list_birthday VALUES(?, ?, ?, ?, ?);", list_to_add_in_db)
    conn.commit()
