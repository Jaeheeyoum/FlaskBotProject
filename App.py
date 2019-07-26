from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
   return 'this is my homepage!'

@app.route('/profile')
def profile():
    address = request.args.get('address')
    return render_template('introduction.html', address = address)

if __name__ == '__main__':
   app.run()

