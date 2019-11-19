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
        flash("This your's result")
        our_expression = form.data['expression']
        our_user = form.data['user_name']
        print('this is our ex', type(our_expression))

        first_number, second_number, action = calc.parse_expression(our_expression)
        alchemy_action = session.AlchemyActions()
        calculator = calc.Calculator(first_number, second_number, action)
        result = calculator.calculate()
        our_user_id = alchemy_action.user_id(our_user)
        if alchemy_action.user_in_table(our_user):
            alchemy_action.update_counter(our_user)
        else:
            our_user_to_table = db.Users(our_user, 1)
            alchemy_action.add_user(our_user_to_table)
        to_res = db.Results(first_number, action, second_number, result, our_user_id)
        alchemy_action = session.AlchemyActions()
        alchemy_action.add_res(to_res)
        return redirect('/index')
    return render_template('calculate.html', title='Sign In', form=form)
# new field for result
# write our data to db (history) using existing functional

