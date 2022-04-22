#from crypt import methods
#import imp
from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

#from flask_bootstrap import Bootstrap
#from requests import Session

app = Flask(__name__)
#Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:I_Like_P1e!@localhost/flasksql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "123456"

db = SQLAlchemy(app)

#@app.route('/')
#def index():
#    return render_template('index.html')

#DB
class Passenger(db.Model):
  __tablename__ = 'passenger'
  passenger_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  gender = db.Column(db.String(80))
  age = db.Column(db.Integer)
  username = db.Column(db.String(80), unique=True)
  password = db.Column(db.String(80))
  email = db.Column(db.String(80))
  phone = db.Column(db.String(80))

  def __init__(self, passenger_id, name, gender, age, username, password, email, phone):
    self.passenger_id = passenger_id
    self.name = name
    self.gender = gender
    self.age = age
    self.username = username
    self.password = password
    self.email = email
    self.phone = phone


class Book(db.Model):
  __tablename__ = 'book'
  ticket_id = db.Column(db.Integer)
  passenger_ID = db.Column(db.Integer, primary_key=True)

  def __init__(self, ticket_id, passenger_id):
    self.ticket_id = ticket_id
    self.passenger_id = passenger_id

class Plane_Ticket(db.Model):
  __tablename__ = 'ticket'
  ticket_ID = db.Column(db.Integer, primary_key=True)
  plane_ID = db.Column(db.Integer)
  departure_city = db.Column(db.String(80))
  arrival_city = db.Column(db.String(80))
  cost = db.Column(db.String(80))
  departure_time = db.Column(db.String(80))
  arrival_time = db.Column(db.String(80))
  boarding_time = db.Column(db.String(80))

  def __init__(self, ticket_ID, plane_ID, departure_city, arrival_city, cost, departure_time, arrival_time, boarding_time):
    self.ticket_ID = ticket_ID
    self.plane_ID = plane_ID
    self.departure_city = departure_city
    self.arrival_city = arrival_city
    self.cost = cost
    self.departure_time = departure_time
    self.arrival_time = arrival_time
    self.boarding_time = boarding_time

class corresponds(db.Model):
  __tablename__ = 'corresponds'
  ticket_ID = db.Column(db.Integer, primary_key=True)
  seat_number = db.Column(db.Integer, primary_key=True)

  def __init__(self, ticket_ID, seat_number):
    self.ticket_ID = ticket_ID
    self.seat_number = seat_number


class Seat(db.Model):
  __tablename__ = 'seat'
  ticket_ID = db.Column(db.Integer, primary_key=True)
  plane_ID = db.Column(db.Integer, primary_key=True)
  seat_number = db.Column(db.Integer)
  id = db.Column(db.Integer)

  def __init__(self, ticket_ID, plane_ID, seat_number, id):
    self.ticket_ID = ticket_ID
    self.plane_ID = plane_ID
    self.seat_number = seat_number
    self.id =id

class Plane(db.Model):
  __tablename__ = 'plane'
  plane_ID= db.Column(db.Integer, primary_key=True)
  type = db.Column(db.String(80))
  name = db.Column(db.String(80))
  num_seats = db.Column(db.Integer)

  def __init__(self, plane_ID, type, name, num_seats):
    self.plane_ID = plane_ID
    self.type = type
    self.name = name
    self.num_seats = num_seats











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
      #try:
      data = Passenger.query.filter_by(username=name, password=passw).first()
      if data is not None:
        session['logged_in'] = True
        return redirect(url_for('home'))
      else:
        return redirect(url_for('login'))

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
    db.create_all()
    app.debug = True
    app.run()