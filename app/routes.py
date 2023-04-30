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


@app.route("/")
@app.route('/index', methods=['GET','POST'])
def index():
    form = forms.Search()
    if form.is_submitted():
        data = weather.Weather(form.search.data)
    else:
        data = weather.Weather(form.search.data)
    return flask.render_template("weather_new.html",
                                 dtime=data.time, sky=data.sky.lower(), temp=f"{int(data.temp)}°C",
                                 city=data.city, color1="yellow", color2="blue", lon=data.lon, lat=data.lat, form=form)
