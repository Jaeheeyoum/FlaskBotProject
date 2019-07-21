from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return 'this is my homepage!'

@app.route('/jaehee')
def jaehee():
    return render_template('introduction.html')

if __name__ == '__main__':
   app.run()
