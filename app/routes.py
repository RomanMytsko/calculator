from flask import render_template
from app import app
from app.forms import DataForm
from flask import render_template, flash, redirect


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    form = DataForm()
    if form.validate_on_submit():
        flash("This your's result")
        our_expression = form.data['expression']
        user_name = form.data['user_name']
        print('Username is - ', user_name)
        print('This is our expression', our_expression)
        return redirect('/index')
    return render_template('calculate.html', title='Sign In', form=form)
# new field for result
# write our data to db (history) using existing functional

