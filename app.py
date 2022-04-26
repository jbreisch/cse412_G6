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

  def __init__(self, name, gender, age, username, password, email, phone):
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
  passenger_id = db.Column(db.Integer, primary_key=True)

  def __init__(self, ticket_id, passenger_id):
    self.ticket_id = ticket_id
    self.passenger_id = passenger_id

class Plane_Ticket(db.Model):
  __tablename__ = 'ticket'
  ticket_id = db.Column(db.Integer, primary_key=True)
  plane_ID = db.Column(db.Integer)
  departure_city = db.Column(db.String(80))
  arrival_city = db.Column(db.String(80))
  cost = db.Column(db.String(80))
  departure_time = db.Column(db.String(80))
  arrival_time = db.Column(db.String(80))
  boarding_time = db.Column(db.String(80))

  def __init__(self, ticket_ID, plane_ID, departure_city, arrival_city, cost, departure_time, arrival_time, boarding_time):
    #self.ticket_ID = ticket_ID
    #self.plane_ID = plane_ID
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

#Sign Up
@app.route('/register', methods=["GET", "POST"])
def register():
  if request.method == 'GET':
    return(render_template('register.html'))
  if request.method == 'POST':
    name = request.form['name']
    gender = request.form['gender']
    age = request.form['age']
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    phone = request.form['phone']

    data = Passenger(name, gender, age, username, password, email, phone)
    db.session.add(data)
    db.session.commit()
    session['logged_in'] = True
    return redirect(url_for('home'))

@app.route('/register_page', methods=["GET"])
def get_register():
  return(render_template('register.html'))



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

@app.route('/find_flights')
def find_flights():
  return render_template('book_flights.html', flights = Plane_Ticket.query.all())

@app.route('/select_flight', methods=['POST', 'GET'])
def select_flight():
  if request.method == 'GET':
    return render_template('book.html')
  if request.method == 'POST':

    flight_id = request.form['plane']
    user = request.form['user']
    passw = request.form['pass']

  #from sqlalchemy.sql import and_
  #s = select([Passenger.passenger_id]).where(and_(Passenger.c.username == user, Passenger.c.password == passw))

    #query = Passenger.select()
    result = Passenger.query.filter_by(username = user).first()
    #result = db.session.query(Passenger).filter(Passenger.username==user).filter(Passenger.password!=passw).group_by(Passenger.passenger_id).first()

    print(result.passenger_id)

    data = Book(flight_id, result.passenger_id)
    db.session.add(data)
    db.session.commit()

    return redirect(url_for('home'))

@app.route('/get_booked_flights', methods=['POST','GET'])
def get_booked_flights():
  user = request.form['user']
  passw = request.form['pass']

  id = Passenger.query.filter_by(username = user, password = passw).first()
  #print(id)
  flight = Book.query.filter_by(passenger_id = id.passenger_id).first()
  #print(flight)
  result = Plane_Ticket.query.filter_by(ticket_id = flight.ticket_id).first()
  #return str(result.ticket_id)
  return render_template('my_flights.html', flights = result)

@app.route('/search_user_flights')
def search_user_flights():
  return(render_template('search_my_flights.html'))







if __name__ == '__main__':
    db.create_all()
    app.debug = True
    app.run()