from flask import Flask, Response

app = Flask(__name__)


@app.route('/users/')
def users():
    return "Hello world"


if __name__ == '__main__':
    app.run()
