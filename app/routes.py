from flask import render_template
from app import app
from app.forms import DataForm
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/calculate', methods=['GET', 'POST'])
def inputing_data():
    form = DataForm()
    if form.validate_on_submit():
        flash("This your's result")
        return redirect('/index')
    return render_template('calculate.html', title='Sign In', form=form)
