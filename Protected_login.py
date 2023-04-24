@app.route('/protected')
def protected():
    # Check if the user has an active session
    if 'username' not in session:
        return redirect(url_for('login'))

    # Render the protected page
    return render_template('protected.html')
