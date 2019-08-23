from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
   return 'this is my homepage!'

@app.route('/profile')
def profile():
    id = request.args.get ('id')
    name = request. args.get ('name')
    return "info : " + id + ":" + name

@app.route('/register', methods=['POST'])
def register():
    header = request.headers['Content-Length']
    body = request.get_data(as_text=True)
    return body

@app.route('/writeComplete', methods=['POST'])
def writeComplete():
    contents = request.get_data(as_text=True)
    return render_template('writeComplete.html', contentsInHtml=contents)

@app.route('/write')
def write():
    return render_template('write.html')


if __name__ == '__main__':
   app.run(debug=True)

