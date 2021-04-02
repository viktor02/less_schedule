import calendar
from datetime import date

from flask import Flask
from flask import render_template

from LessonsLoader import LessonsLoader
from Notes import AddNoteForm, NoteLoader

app = Flask(__name__)


@app.route('/')
def main_page():
    today = date.today()
    return monthday_page(today.day, today.month, today.year)


@app.route('/day/<int:day>/')
@app.route('/date/<int:month>/<int:day>')
@app.route('/date/<int:year>/<int:month>/<int:day>')
def monthday_page(day, month=date.today().month, year=date.today().year):
    """ Render page with schedule"""
    try:
        schedule_loader = LessonsLoader('schedule.db')
        notes_loader = NoteLoader()

        weekday = date(year, month, day).isoweekday()
        is_odd_week = True if date(year, month, day).isocalendar()[1] % 2 == 0 else False

        schedule = schedule_loader.get_lessons(weekday, is_odd_week)
        time = schedule_loader.get_time()
        notes = notes_loader.get_notes(year, month, day)

        return render_template('index.html', schedule=schedule, schedule_time=time, notes=notes)
    except ValueError:
        return "Wrong value"


@app.route('/time')
def time_page():
    """ Render page with lessons time"""
    lessons = LessonsLoader()
    lesson_time = lessons.get_time()

    return render_template('time.html', schedule_time=lesson_time)


@app.route('/calendar/')
def calendar_main_page():
    today = date.today()
    return calendar_page(today.month, today.year)


@app.route('/calendar/<int:month>')
@app.route('/calendar/<int:year>/<int:month>')
def calendar_page(month, year):
    """ Render calendar page """
    try:
        cal = calendar.Calendar()
        days_matrix = cal.monthdayscalendar(year, month)

        return render_template("calendar.html", month=days_matrix)
    except calendar.IllegalMonthError:
        return "Wrong month value"


@app.route('/notes', methods=['GET', 'POST'])
def add_note():
    notes_loader = NoteLoader()
    form = AddNoteForm(meta={'csrf': False})
    notes = notes_loader.get_all_notes()
    if form.validate_on_submit():
        note = form.note.data
        year = form.date.data.year
        month = form.date.data.month
        day = form.date.data.day

        notes_loader.add_note(year, month, day, note)

    return render_template('notes.html',
                           form=form, notes=notes)


@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
