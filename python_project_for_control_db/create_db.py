import sqlite3

conn = sqlite3.connect('./list_of_birthdays.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS list_birthday(
   name TEXT PRIMARY KEY,
   sex TEXT,
   nickname TEXT,
   date_of_birth TEXT,
   telegramm_username TEXT);
""")
