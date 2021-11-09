from app import app
from flask import render_template
from app.forms import TVSearchForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TVSearchForm()
    if form.validate_on_submit():
        show = form.title.data
        print('Form Submitted!', show)
    return render_template('index.html', form=form)