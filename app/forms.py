from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class TVSearchForm(FlaskForm):
    title = StringField('Show Title')
    submit = SubmitField()
