from flask import render_template
from app import app
from app.forms import DataForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/calculate')
def inputing_data():
    form = DataForm()
    return render_template('calculate.html', title='Sign In', form=form)
