from flask import Flask

app = Flask(__name__)


@app.route('/')
def hi():
    return '<html><head><title>Hello</title></head><body>Hello</body></html>'

