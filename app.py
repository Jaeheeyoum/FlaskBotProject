from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
   return 'this is my homepage!'

@app.route('/profile')
def profile():
    myName = request.args.get('name')
    return render_template('introduction.html', mynameinHTML = myName)

if __name__ == '__main__':
   app.run()

