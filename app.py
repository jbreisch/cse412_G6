from crypt import methods
import imp
from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap
from requests import Session

app = Flask(__name__)
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zblgrfkvbmcjoa:25c9290fe133061ad4b1afede41edbb3f2916f2c088719a0d3ec6752fdb00808@ec2-54-80-122-11.compute-1.amazonaws.com:5432/d2mh5ngopeuued'
db = SQLAlchemy(app)

#@app.route('/')
#def index():
#    return render_template('index.html')

#DB
class Passenger(db.Model):
  __tablename__ = 'passenger'
  passenger_ID = db.Column(db.Integer, db.ForeignKey('Book.passenger_ID'), primary_key=True)
  name = db.Column(db.String(80))
  gender = db.Column(db.String(80))
  age = db.Column(db.Integer)
  username = db.Column(db.String(80), unique=True)
  password = db.Column(db.String(80))
  email = db.Column(db.String(80))
  phone = db.Column(db.Sting(80))

  def __init__(self, passenger_ID, name, gender, age, username, password, email, phone):
    self.passenger_ID = passenger_ID
    self.name = name
    self.gender = gender
    self.age = age
    self.username = username
    self.password = password
    self.email = email
    self.phone = phone


class Book(db.Model):
  __tablename__ = 'book'
  ticket_ID = db.Column(db.Integer)
  passenger_ID = db.Column(db.Integer, db.ForeignKey('Passenger.passenger_ID'), primary_key=True)

class Plane_Ticket(db.Model):
  __tablename__ = 'passenger'
  ticket_ID = db.Column(db.Integer, db.ForeignKey('corresponds.ticket_ID'), primary_key=True)
  plane_ID = db.Column(db.Integer)
  departure_city = db.Column(db.String(80))
  arrival_city = db.Column(db.String(80))
  cost = db.Column(db.String(80))
  departure_time = db.Column()
  arrival_time = db.Column()
  boarding_time = db.Column()

class corresponds(db.Model):
  __tablename__ = 'corresponds'
  ticket_ID = db.Column(db.Integer, db.ForeignKey('Seat.ticket_ID'), db.ForeignKey('Plane_Ticket.ticket_ID'), primary_key=True)
  seat_number = db.Column(db.Integer, db.ForeignKey('Book.passenger_ID'), primary_key=True)

class Seat(db.Model):
  __tablename__ = 'seat'
  ticket_ID = db.Column(db.Integer,db.ForeignKey('corresponds.ticket_ID'), primary_key=True)
  plane_ID = db.Column(db.Integer, primary_key=True)
  seat_number = db.Column(db.Integer)
  id = db.Column(db.Integer)

class Plane(db.Model):
  __tablename__ = 'plane'
  plane_ID= db.Column(db.Integer, db.ForeignKey('Seat.plane_ID'), primary_key=True)
  type = db.Column(db.String(80))
  name = db.Column(db.String(80))
  num_seats = db.Column(db.Integer)










############################################################################################
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
          #return 'Dont Login'
          return redirect(url_for('login'))
      except:
        return "Dont Login"


@app.route('/search_flights', methods=['GET', 'POST'])
def search():
  departure = request.form.get('depart')
  arrival = request.form.get('arrive')
  session = Session()
  departCityList = []
  arriveCityList = []
  costList = []
  departTimeList = []
  arriveTimeList = []
  boardingTimeList = []
  results = session.query(PlaneTicket).all()
  #for i in results:
    #if ()



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