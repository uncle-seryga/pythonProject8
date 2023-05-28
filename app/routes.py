import flask

import currency
import weather
from app import app
from app import forms

"""
@app.route('/')
@app.route('/index')
def index():
    all_data = database.get_all_from_base()
    return flask.render_template("index.html", data=all_data, len=len(all_data))
"""


@app.route("/")
@app.route('/index', methods=['GET', 'POST'])
def index():
    list_of_currency_names = [x for x in currency.set_currency()]
    list_of_currency_names_full = currency.set_currency()
    form = forms.Currency()
    if form.is_submitted():
        a = flask.request.form.get("currencies-list-1")
        b = flask.request.form.get("currencies-list-2")
        print(form.submit.data)  # todo return False, input data expected -> research
        result = currency.convert(a, b, form.submit.data)
        return flask.render_template("currency_main.html", currency_list=list_of_currency_names_full,
                                     input_amount=form.search, result=0, form=form)
    return flask.render_template("currency_main.html", currency_list=list_of_currency_names_full,
                                 input_amount=form.search, result=0, form=form)
