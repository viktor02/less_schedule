import sqlite3


class Loader:
    def __init__(self, dbname='schedule.db'):
        self.conn = sqlite3.connect(dbname)
        self.cur = self.conn.cursor()
        self.create_db()

    def create_db(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS "lessons" (
                            "number"	INTEGER,
                            "day"	INTEGER,
                            "time"	INTEGER,
                            "lesson"	TEXT,
                            "teacher"	TEXT,
                            "odd"	INTEGER)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS "time" (
                            "numberoflesson"	INTEGER,
                            "time_start"	TEXT,
                            "time_end"	TEXT,
                            "is_short_day"	INTEGER)''')
        self.cur.execute('''CREATE TABLE IF NOT EXISTS "notes" (
                            "year"  INTEGER
                            "month"	INTEGER,
                            "day"	INTEGER,
                            "note"	TEXT)
                            ''')
