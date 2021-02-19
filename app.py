from flask import Flask
from flask import render_template

from scheduleLoader import Loader

import datetime
import calendar

app = Flask(__name__)

current_month = datetime.datetime.today().month
current_year = datetime.datetime.today().year


@app.route('/')
def main_page():
    current_weekday = datetime.datetime.today().isoweekday()
    is_odd_week = True if datetime.datetime.today().isocalendar()[1] % 2 == 0 else False

    schedule_loader = Loader()

    schedule = schedule_loader.get_lessons(current_weekday, is_odd_week)
    time = schedule_loader.get_time()

    return render_template('index.html', schedule=schedule, schedule_time=time)


@app.route('/day/<int:monthday>/')
def monthday_page(monthday):
    try:
        schedule_loader = Loader()

        weekday = datetime.date(current_year, current_month, monthday).isoweekday()
        is_odd_week = True if datetime.datetime.today().isocalendar()[1] % 2 == 0 else False

        schedule = schedule_loader.get_lessons(weekday, is_odd_week)
        time = schedule_loader.get_time()

        return render_template('index.html', schedule=schedule, schedule_time=time)
    except ValueError:
        return "Wrong value"


@app.route('/time')
def time_page():
    schedule_loader = Loader()
    lesson_time = schedule_loader.get_time()

    return render_template('time.html', schedule_time=lesson_time)


@app.route('/calendar/')
@app.route('/calendar/<int:month>')
def calendar_page(month=current_month, year=current_year):
    try:
        cal = calendar.Calendar()
        month_iter = cal.monthdayscalendar(year, month)

        return render_template("calendar.html", month=month_iter)
    except calendar.IllegalMonthError:
        return "Wrong month value"


@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
