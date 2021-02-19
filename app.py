from flask import Flask
from flask import render_template

from scheduleLoader import Loader

import datetime
import calendar

app = Flask(__name__)

current_day_of_week = datetime.datetime.today().isoweekday()
current_month = datetime.datetime.today().month
current_year = datetime.datetime.today().year
is_odd_week = True if datetime.datetime.today().isocalendar()[1] % 2 == 0 else False


@app.route('/')
def main_page():
    schedule_loader = Loader()

    schedule = schedule_loader.get_lessons(current_day_of_week, is_odd_week)
    time = schedule_loader.get_time()

    return render_template('index.html', schedule=schedule, schedule_time=time)


@app.route('/day/<monthday>/')
def monthday_page(monthday):
    schedule_loader = Loader()

    weekday = datetime.date(current_year, current_month, int(monthday)).isoweekday()
    is_odd_week = True if datetime.datetime.today().isocalendar()[1] % 2 == 0 else False

    schedule = schedule_loader.get_lessons(weekday, is_odd_week)
    time = schedule_loader.get_time()

    return render_template('index.html', schedule=schedule, schedule_time=time)


@app.route('/time')
def time_page(dayofweek=current_day_of_week):
    schedule_loader = Loader()
    lesson_time = schedule_loader.get_time()

    return render_template('time.html', schedule_time=lesson_time)


@app.route('/calendar/')
@app.route('/calendar/<month>')
def calendar_page(month=current_month, year=current_year):
    cal = calendar.Calendar()
    month_iter = cal.monthdayscalendar(year, month)

    return render_template("calendar.html", month=month_iter)


@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
