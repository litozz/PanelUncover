
import flask
from utils import reveal

secrets={
    '3456':1,
    '4567':2,
    '4730':3,
    '6459':4,
    '6132':5,
    '0584':6,
    '6153':7,
    '6492':8,
    '9784':9
}

app = flask.Flask(__name__, template_folder='../static/html')
solved = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if flask.request.method == 'GET':
        return flask.render_template('index.html', secrets=secrets, solved=solved)
    elif flask.request.method == 'POST':
        panel_id = secrets.get(flask.request.form.get('text_code'))
        if panel_id is not None:
            solved.append(panel_id)
        return flask.render_template('index.html', secrets=secrets, solved=solved)
