import imp
from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

#@app.route('/')
#def index():
#    return render_template('index.html')

@app.route('/get-flights', methods = ['POST', 'GET'])
def getFLights():
  return



@app.route('/', methods=['GET'])
def home():
  """Session Control"""
  if not session.get('logged_in'):
    return render_template('index.html')
  else:
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
      return render_template('login.html')
    else:
      name = request.form['uname']
      passw = request.form['psw']
      try:
        #data = User.query.filter_by(username=name, password=passw).first()
        #if data is not None:
        if name == 'jp' and passw == 'test':  
          session['logged_in'] = True
          #return render_template('index.html')
          return redirect(url_for('home'))
        else:
          return 'Dont Login'
      except:
        return "Dont Login"


@app.route('/home', methods=["GET"])
def get_home():
  return(render_template('index.html'))

@app.route("/logout")
def logout():
    """Logout Form"""
    session['logged_in'] = False
    return redirect(url_for('home'))

@app.route("/book")
def get_booking():
  return(render_template('book_flights.html'))

@app.route("/myflights")
def get_my_flights():
  return(render_template('my_flights.html'))


if __name__ == '__main__':
    app.secret_key = "123456"
    app.debug = True
    app.run()