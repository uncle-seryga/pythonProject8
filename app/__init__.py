from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "aksndvnasdnviu3bvbn3r"
from app import routes
from app import forms
