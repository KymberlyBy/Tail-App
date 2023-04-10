from flask import Flask 

app = Flask(__name__)


@app.route ('/')
def home():
    return 'This is the home page, hello!'


app.run(host='0.0.0.0', port=8080)