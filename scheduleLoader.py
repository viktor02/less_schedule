import sqlite3


class Loader:
    def __init__(self, dbname='schedule.db'):
        conn = sqlite3.connect(dbname)
        self.conn = conn.cursor()
        self.create_db()

    def create_db(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS "lessons" (
                            "number"	INTEGER,
                            "day"	INTEGER,
                            "time"	INTEGER,
                            "lesson"	TEXT,
                            "teacher"	TEXT,
                            "odd"	INTEGER)''')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS "time" (
                            "numberoflesson"	INTEGER,
                            "time_start"	TEXT,
                            "time_end"	TEXT,
                            "is_short_day"	INTEGER)''')
        self.conn.execute('''CREATE TABLE IF NOT EXISTS "notes" (
                            "day"	INTEGER,
                            "month"	INTEGER,
                            "note"	TEXT)
                            ''')

    def get_lessons(self, dayofweek=1, is_odd_week=True) -> list:
        lessons = self.conn.execute('''SELECT * FROM "lessons" WHERE "dayofweek" = ? and "odd" = ? ''',
                                    [dayofweek, int(is_odd_week)])
        lessons = self.conn.fetchall()
        return lessons

    def get_time(self, is_short_day=False) -> list:
        self.conn.execute('''SELECT * FROM "time" WHERE "is_short_day" = ?''',
                          [int(is_short_day)])
        time = self.conn.fetchall()
        return time

    def get_notes(self, month, day) -> list:
        self.conn.execute(''' SELECT note FROM "notes" WHERE "month" = ? and "day" = ?''',
                          [month, day])
        notes = self.conn.fetchall()
        return notes
