from waitress import serve
import os
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello_world():
     return 'Hello, World!'

@app.route('/textbox')
def textbox():
    return render_template('textbox.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')


if __name__ =='__main__':
   #  app.run(debug=True)
   serve(app, host = '0.0.0.0', port = int(os.environ.get('PORT', 8080)))









