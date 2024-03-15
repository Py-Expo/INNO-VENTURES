from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Render the 'index2.html' template for the '/' route

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']
        confirm_password = request.form['psw-repeat']

        # Here you can perform validation, database operations, etc.
        # For simplicity, let's just print the received data
        print(f'Email: {email}, Password: {password}, Confirm Password: {confirm_password}')
        return 'Registration successful!'  # Response for successful registration
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register form.html")

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['psw']
        confirm_password = request.form['psw-repeat']

        # Here you can perform validation, database operations, etc.
        # For simplicity, let's just print the received data
        print(f'Email: {email}, Password: {password}, Confirm Password: {confirm_password}')
        return 'Registration successful!'  # Response for successful registration

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode
