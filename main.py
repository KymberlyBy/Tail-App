from flask import Flask, request

app = Flask(__name__)


@app.route('/hello')
def new_app():
    return "<h1>this is a test!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  