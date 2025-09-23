import re
from random import randint
from datetime import datetime, timedelta
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_register import *
from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'ght' # Замените на надежный ключ
# login_manager = LoginManager()
# login_manager.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/connect_me')
def connect():
    return render_template('connect_me.html')
# @app.route('/login')
# def login():
#     return render_template('login.html')
# @app.route('/register')
# def register():
#     return render_template('register.html')
@app.route('/education')
def education():
    return render_template('education.html')

if __name__ == "__main__":
    app.run(debug=True)