from app import app
from flask import render_template
from app.forms import TVSearchForm


@app.route('/')
def index():
    form = TVSearchForm()
    return render_template('index.html', form=form)