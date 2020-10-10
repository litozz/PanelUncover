
import flask
from utils import reveal

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'PUT'])
def index():
    if flask.request.method == 'GET':
        return 'Welcome to PanelUncover game'
    elif flask.request.method == 'PUT':
        return reveal()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
