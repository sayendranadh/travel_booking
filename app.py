from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from config import Config
from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.config.from_object(Config)


# Function to create a database connection
def get_db_connection():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        port=app.config['MYSQL_PORT'],
    )

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# User signup
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        # Connecting to MySQL
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                        (username, email, password))
            conn.commit()
            flash('Account created successfully!', 'success')
        except mysql.connector.Error as err:
            flash(f"Error: {err}", 'danger')
        finally:
            cur.close()
            conn.close()
        return redirect(url_for('index'))
    return render_template('signup.html')
# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Bus booking
@app.route('/bus', methods=['GET', 'POST'])
def bus():
    if request.method == 'POST':
        departure = request.form['departure']
        destination = request.form['destination']
        date = request.form['date']
        seating_type = request.form['seating_type']

        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO bus_bookings (departure, destination, date, seating_type) VALUES (%s, %s, %s, %s)", (departure, destination, date, seating_type))
            conn.commit()
            cur.close()
            conn.close()
            
            booking_details = {
                'departure': departure,
                'destination': destination,
                'date': date,
                'seating_type': seating_type
            }
            
            return render_template('bus_success.html', booking_details=booking_details)
        
        except mysql.connector.Error as e:
            conn.rollback()
            cur.close()
            conn.close()
            return str(e)
    return render_template('bus.html')

# Train booking
@app.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        departure = request.form['departure']
        destination = request.form['destination']
        date = request.form['date']
        class_type = request.form['class_type']

        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute( "INSERT INTO train_bookings (departure, destination, date, class_type) VALUES (%s, %s, %s, %s)", (departure, destination, date, class_type))
            conn.commit()
            cur.close()
            conn.close()
            
            booking_details = {
                'departure': departure,
                'destination': destination,
                'date': date,
                'class_type': class_type
            }
            
            return render_template('train_success.html', booking_details=booking_details)
        
            
        except mysql.connector.Error as e:
            conn.rollback()
            cur.close()
            conn.close()
            return str(e)
    return render_template('train.html')


# Route for the flight booking page
@app.route('/book-flights', methods=['GET', 'POST'])
def book_flight():
    if request.method == 'POST':
        # Retrieve form data
        departure = request.form['departure']
        destination = request.form['destination']
        date = request.form['date']
        passengers = request.form['passengers']
        seating_type = request.form['seating_type']

        # Connecting to MySQL
        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO flights (departure, destination, date, passengers, seating_type) VALUES (%s, %s, %s, %s, %s)",
                        (departure, destination, date, passengers, seating_type))
            conn.commit()
            cur.close()
            conn.close()
            
            booking_details = {
                'departure': departure,
                'destination': destination,
                'date': date,
                'passengers': passengers,
                'seating_type': seating_type
            }
            
            return render_template('flight_success.html', booking_details=booking_details)
        
        except mysql.connector.Error as e:
            conn.rollback()
            cur.close()
            conn.close()
            return str(e)
    return render_template('book_flight.html')

if __name__ == '__main__':
    app.run(debug=True)
