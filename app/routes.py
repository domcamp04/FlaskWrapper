from app import app
from flask import render_template
from app.forms import TVSearchForm
from app.wrappers import TVMazeAPI

client = TVMazeAPI()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TVSearchForm()
    show_list = None
    if form.validate_on_submit():
        show = form.title.data
        show_list = client.search_shows(show)
    return render_template('index.html', form=form, show_list=show_list)
