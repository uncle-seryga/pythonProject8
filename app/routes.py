import flask

import weather
from app import app
import database

"""
@app.route('/')
@app.route('/index')
def index():
    all_data = database.get_all_from_base()
    return flask.render_template("index.html", data=all_data, len=len(all_data))
"""


@app.route('/')
@app.route('/index')
def index():
    data = weather.Weather("Kyiv")
    return flask.render_template("weather.html",
                                 dtime=data.time, sky=data.sky.lower(), temp=f"{int(data.temp)}°C",
                                 city=data.city, color1="yellow", color2="blue")
