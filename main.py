from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Dhanu@9090@#$'
app.config['MYSQL_DB'] = 'Minvazhi thoodhu'

mysql = MySQL(app)

# Route to render registration form
@app.route('/register')
def register():
    return render_template('register.html')

# Route to handle registration form submission
@app.route('/register', methods=['POST'])
def register_user():
      username = request.form['username']
      password = request.form['password']
    
#     # Insert user data into database
cursor = mysql.connection.cursor()
cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
mysql.connection.commit()
cursor.close()
# Redirect to homepage after registration
def home():
    return redirect(url_for('home'))  

if __name__ == '_main_':
    app.run(debug=True)