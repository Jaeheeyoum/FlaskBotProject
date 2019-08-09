from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return 'this is my homepage!'

@app.route('/profile')
def profile():
    return render_template('introduction.html')

if __name__ == '__main__':
   app.run(debug=True)

