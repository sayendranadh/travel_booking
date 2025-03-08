
# 🚀 Flask Travel Booking System

**Flask Travel Booking System** is a web application built with the Flask framework. This system allows users to book bus, train, or flight tickets seamlessly. It is powered by a local MySQL database and features email integration for booking confirmations. Perfect for travelers seeking a user-friendly platform for their booking needs!

---

## 🌟 Features

- **User Signup:** Securely register with your username, email, and password.
- **Bus, Train, and Flight Booking:** Book tickets for your desired travel mode, including all required details such as departure, destination, date, and seating/class type.
- **Database Integration:** MySQL database to store and manage user information and bookings.
- **Email Notifications:** Automatic email confirmation of bookings to enhance user experience.

---

## 🛠️ Built With

- **Backend Framework:** Flask (Python)
- **Database:** MySQL
- **Email Integration:** SMTP for email notifications
- **Frontend:** HTML & Jinja2 Templates
- **Security:** Passwords hashed using Werkzeug's `generate_password_hash`

---

## 💾 Database Schema

The application uses the following MySQL tables:

### 1. `users`
| Column Name | Data Type   | Description                     |
|-------------|-------------|---------------------------------|
| id          | INT         | Primary Key (Auto Increment)   |
| username    | VARCHAR(50) | Username of the user           |
| email       | VARCHAR(100)| User's email (unique)          |
| password    | VARCHAR(255)| Hashed password                |
| created_at  | TIMESTAMP   | Timestamp of account creation  |

### 2. `bus_bookings`
| Column Name    | Data Type   | Description                     |
|----------------|-------------|---------------------------------|
| id             | INT         | Primary Key (Auto Increment)   |
| departure      | VARCHAR(100)| Departure location             |
| destination    | VARCHAR(100)| Destination location           |
| date           | DATE        | Travel date                   |
| seating_type   | VARCHAR(50) | Type of seating                |
| created_at     | TIMESTAMP   | Timestamp of booking creation  |

### 3. `train_bookings`
| Column Name    | Data Type   | Description                     |
|----------------|-------------|---------------------------------|
| id             | INT         | Primary Key (Auto Increment)   |
| departure      | VARCHAR(100)| Departure location             |
| destination    | VARCHAR(100)| Destination location           |
| date           | DATE        | Travel date                   |
| class_type     | VARCHAR(50) | Type of train class            |
| created_at     | TIMESTAMP   | Timestamp of booking creation  |

### 4. `flights`
| Column Name    | Data Type   | Description                     |
|----------------|-------------|---------------------------------|
| id             | INT         | Primary Key (Auto Increment)   |
| departure      | VARCHAR(100)| Departure location             |
| destination    | VARCHAR(100)| Destination location           |
| date           | DATE        | Travel date                   |
| passengers     | INT         | Number of passengers           |
| seating_type   | VARCHAR(50) | Type of seating                |
| created_at     | TIMESTAMP   | Timestamp of booking creation  |

---

## ⚙️ How It Works

1. **User Signup:**
   - Users register an account with their email, username, and password.
   - Passwords are hashed for security.

2. **Booking Process:**
   - Users can book tickets for bus, train, or flights by providing required details (departure, destination, date, etc.).
   - Booking details are securely stored in the MySQL database.

3. **Email Notifications:**
   - After completing a booking, the user receives a confirmation email with booking details.

---

## 🚀 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/travel_booking.git
   cd travel_booking
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the database:
   - Create a MySQL database with the required tables mentioned in the schema above.
   - Update the `Config` class in your `config.py` file with your MySQL credentials.

4. Run the Flask application:
   ```bash
   python app.py
   ```

5. Access the application:
   - Open your browser and navigate to `http://127.0.0.1:5000`.

---

## 📧 SMTP Email Configuration

To enable email notifications:
1. Update the SMTP details in your `Config` class in `config.py`:
   ```python
   MAIL_SERVER = 'smtp.your-email-provider.com'
   MAIL_PORT = 587
   MAIL_USERNAME = 'your-email@example.com'
   MAIL_PASSWORD = 'your-app-password'
   MAIL_USE_TLS = True
   ```

2. Replace placeholders with your email provider's SMTP settings.

---

## 🎉 Contribute

Want to make this project even better? Contributions are welcome! Fork the repository, make your changes, and submit a pull request. Let’s build something amazing together!

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

