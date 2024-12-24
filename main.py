from flask import Flask, render_template, redirect, url_for, request
from db_connect import *

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/after')
def after():
    return render_template('after.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/signin', methods=['POST'])
def check_user():
    username = request.form.get('username')
    password = request.form.get('password')
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)
    dbc.execute(query, values)
    user = dbc.fetchone()

    if user:
        return redirect(url_for('/after'))
    else:
        error_message = "Bunday foydalanuvchi mavjud emas!"
        return redirect(url_for('/', error= error_message))


@app.route('/create_account', methods=['POST'])
def create_account():
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if password != confirm_password:
        error_message = 'Parolni tasdiqlang!'
        return redirect(url_for('register', error = error_message))

    query = "SELECT * FROM users WHERE email = %s"
    value = (email)
    dbc.execute(query, value)
    used_email = dbc.fetchone()

    query = "SELECT * FROM users WHERE username = %s"
    value = (username)
    dbc.execute(query, value)
    used_username = dbc.fetchone()



    if used_username and used_email:
        error_message = "Bunday foydalanuvchi mavjud!"
        return redirect(url_for('register', error = error_message))
    elif used_username:
        error_message = "Bunday username mavjud!"
        return redirect(url_for('register', error = error_message))
    elif used_email:
        error_message = "Bunday email mavjud!"
        return redirect(url_for('register', error = error_message))

    query = "INSERT INTO users (name, username, email, password) VALUES (%s, %s, %s, %s)"
    values = (name, username, email, password)
    dbc.execute(query, values)
    return redirect(url_for('/after'))



if __name__ == '__main__':
    app.run(debug=True)
