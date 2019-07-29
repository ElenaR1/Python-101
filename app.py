from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    print('g')
    return '<h1>Hello World gfre</h1>'


if __name__ == '__name__':
    app.run()

