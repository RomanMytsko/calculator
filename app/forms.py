from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class DataForm(FlaskForm):
    datafield = StringField('Please input first number, action and second number', validators=[DataRequired()])
    submit = SubmitField('Calculate')
