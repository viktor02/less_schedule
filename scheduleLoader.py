import sqlite3


class Loader():
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
                            "odd"	INTEGER)
                            ''')

    def get_lessons(self, dayofweek=1, is_odd_week=True) -> list:
        lessons = self.conn.execute('''SELECT * FROM "lessons" WHERE "dayofweek" = ? and "odd" = ? ''',
                                    [dayofweek, int(is_odd_week)])
        lessons = self.conn.fetchall()
        return lessons

    def get_time(self) -> list:
        self.conn.execute('''SELECT * FROM "time" ''')
        time = self.conn.fetchall()
        return time