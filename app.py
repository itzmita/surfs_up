from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name