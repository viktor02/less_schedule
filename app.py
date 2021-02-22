import calendar
import datetime

from flask import Flask
from flask import render_template

from scheduleLoader import Loader

app = Flask(__name__)

today = datetime.datetime.today()
current_day = today.day
current_month = today.month
current_year = today.year


@app.route('/')
def main_page():
    return monthday_page(current_day, current_month)


@app.route('/day/<int:day>/')
@app.route('/date/<int:month>/<int:day>')
def monthday_page(day, month=current_month):
    """ Render page with schedule"""
    try:
        schedule_loader = Loader()

        weekday = datetime.date(current_year, month, day).isoweekday()
        is_odd_week = True if datetime.date(current_year, month, day).isocalendar()[1] % 2 == 0 else False

        schedule = schedule_loader.get_lessons(weekday, is_odd_week)
        time = schedule_loader.get_time()
        notes = schedule_loader.get_notes(month, day)

        return render_template('index.html', schedule=schedule, schedule_time=time, notes=notes)
    except ValueError:
        return "Wrong value"


@app.route('/time')
def time_page():
    """ Render page with lessons time"""
    schedule_loader = Loader()
    lesson_time = schedule_loader.get_time()

    return render_template('time.html', schedule_time=lesson_time)


@app.route('/calendar/')
@app.route('/calendar/<int:month>')
def calendar_page(month=current_month, year=current_year):
    """ Render calendar page """
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
