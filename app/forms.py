from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class Search(FlaskForm):
    search = StringField(validators=[DataRequired()], render_kw={'placeholder': "Search city"})
    submit = SubmitField()

class Currency(FlaskForm):
    search = StringField(validators=[DataRequired()], render_kw={'placeholder': "Amount"})
    submit = SubmitField()