from flask import Flask, request, render_template, redirect, session, url_for
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve login credentials from the form
        username = request.form['username']
        password = request.form['password']

        # Authenticate the user
        user = get_user_from_database(username)
        if not user or not check_password_hash(user.password, password):
            error_message = "Invalid username or password"
            return render_template('login.html', error_message=error_message)

        # Create a session for the user
        session['username'] = user.username

        # Redirect the user to the main application page
        return redirect(url_for('main'))

    # If the request method is GET, render the login form
    return render_template('login.html')
