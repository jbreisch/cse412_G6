from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-flights', methods = ['POST', 'GET'])
def getFLights():
  return


if __name__ == '__main__':
    app.run()