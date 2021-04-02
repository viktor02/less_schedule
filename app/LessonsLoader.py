from Loader import Loader


class LessonsLoader(Loader):
    def get_lessons(self, dayofweek=1, is_odd_week=True) -> list:
        lessons = self.cur.execute('''SELECT * FROM "lessons" WHERE "dayofweek" = ? and "odd" = ? ''',
                                   [dayofweek, int(is_odd_week)])
        lessons = self.cur.fetchall()
        return lessons

    def get_time(self, is_short_day=False) -> list:
        self.cur.execute('''SELECT * FROM "time" WHERE "is_short_day" = ?''',
                         [int(is_short_day)])
        time = self.cur.fetchall()
        return time
