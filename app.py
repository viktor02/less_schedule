from flask import Flask
from flask import render_template
from scheduleLoader import Loader
import datetime


app = Flask(__name__)

current_day_of_week = datetime.datetime.today().isoweekday()
is_odd_week = True if datetime.datetime.today().isocalendar()[1] % 2 == 0 else False

@app.route('/')
@app.route('/day/<dayofweek>/')
def main_page(dayofweek=current_day_of_week):
    schedule_loader = Loader()
    schedule = schedule_loader.get_lessons(dayofweek, is_odd_week)
    lesson_time = schedule_loader.get_time()

    return render_template('index.html', schedule=schedule, schedule_time=lesson_time)


@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
