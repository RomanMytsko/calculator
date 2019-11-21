import result as result
from flask import render_template
from app import app
from app.forms import DataForm
from flask import render_template, flash, redirect
import calculator as calc
import models as db
import db_connector_alchemy as session


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    form = DataForm()
    if form.validate_on_submit():
        expression = form.data['expression']
        user = form.data['user_name']
        first_number, second_number, action = calc.parse_expression(expression)
        alchemy_action = session.AlchemyActions()
        calculator = calc.Calculator(first_number, second_number, action)
        result = calculator.calculate()
        user_id = alchemy_action.user_id(user)
        if alchemy_action.user_in_table(user):
            alchemy_action.update_counter(user)
        else:
            user_to_table = db.Users(user, 1)
            alchemy_action.add_user(user_to_table)
        to_res = db.Results(first_number, action, second_number, result, user_id)
        alchemy_action.add_res(to_res)
        return redirect('/calculate')
    return render_template('calculate.html', title='Sign In', form=form)
