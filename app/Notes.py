from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import TextAreaField, DateField
from wtforms.validators import DataRequired

from Loader import Loader


class AddNoteForm(FlaskForm):
    note = TextAreaField('Заметка', validators=[DataRequired()])
    date = DateField(
        label='Дата',
        format='%d-%m-%Y',
        validators=[DataRequired('')]
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.date.data:
            self.date.data = datetime.today()


class NoteLoader(Loader):
    def get_all_notes(self):
        self.cur.execute('''SELECT * FROM "notes"''')
        notes = self.cur.fetchall()
        return notes

    def get_notes(self, year, month, day) -> list:
        self.cur.execute('''SELECT note FROM "notes" WHERE "year" = ? and "month" = ? and "day" = ? ''',
                         [year, month, day])
        notes = self.cur.fetchall()
        return notes

    def add_note(self, year, month, day, note):
        with self.conn:
            return self.cur.execute('''INSERT INTO notes(year, month, day, note)  VALUES (?, ?, ?, ?)''',
                                    [year, month, day, note])
