from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class DataForm(FlaskForm):
    expression = StringField('Please input your expression', validators=[DataRequired()])
    user_name = StringField('Please enter your name', validators=[DataRequired()])
    result = IntegerField('This is your result')
    submit = SubmitField('Calculate')
