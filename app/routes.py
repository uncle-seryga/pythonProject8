import flask

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


@app.route('/', methods=['GET','POST'])
def index():
    form = forms.Search()
    if form.validate_on_submit():
        print('here')
        data = weather.Weather(form.search.data)
    else:
        print('or here')
        data = weather.Weather("Kyiv")
    return flask.render_template("weather.html",
                                 dtime=data.time, sky=data.sky.lower(), temp=f"{int(data.temp)}°C",
                                 city=data.city, color1="yellow", color2="blue", lon=data.lon, lat=data.lat, form=form)
