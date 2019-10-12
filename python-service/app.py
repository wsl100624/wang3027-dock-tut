from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Service Python is alive! \n'

@app.route('/1/<y>')
def return_value(y):
    return '%s \n' % y 

@app.route('/2/<anyString>')
def return_string(anyString):
    return '%s \n' % anyString

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
