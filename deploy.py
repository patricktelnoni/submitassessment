from flask import Flask

app = FLask(__name__)

@app.route('/')
def index:
    return '<h1>deployed from heroku!!!</h1>'
