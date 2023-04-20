from App import create_app 

app = create_app()

@app.route ('/')
def home():
    return 'Welcome to Tail, the app that keeps your loved ones safe!'

if __name__=='__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True)