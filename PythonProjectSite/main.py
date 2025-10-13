import random
import re
import bcrypt
from random import randint
from datetime import datetime, timedelta
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user
from flask_register import *
cube_face = 0

# def hashed_password(plain_text_password):
#     # Мы добавляем "соль" к нашему пароль, чтобы сделать его декодирование невозможным
#     return bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
#
#
# def check_password(plain_text_password, hashed_password):
#     return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password)

app = Flask(__name__)

all_orders = []

app.config.update(
    SECRET_KEY='WOW SUCH SECRET'
)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = "login"


# class User(UserMixin):
#     def __init__(self, id):
#         self.id = id


# @login_manager.user_loader
# def load_user(login):
#     return User(login)


# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         for key in request.form:
#             if request.form[key] == '':
#                 return render_template('register.html', message='Все поля должны быть заполнены!')
#
#         row = db.users.get('login', request.form['login'])
#         if row:
#             return render_template('register.html', message='Такой пользователь уже существует!')
#
#         if request.form['password'] != request.form['password_check']:
#             return render_template('register.html', message='Пароли не совпадают')
#         data = dict(request.form)
#         data.pop('password_check')
#         db.users.put(data=data)
#         return render_template('register.html', message='Регистрация прошла успешно')
#     return render_template('register.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    random_number = None
    error = None
    min_val = 1
    max_val = 100

    if request.method == 'POST':
        try:
            # Получаем числа из формы
            min_str = request.form['min_number']
            max_str = request.form['max_number']

            # Проверяем, что введенные значения - числа
            if not min_str.isdigit() or not max_str.isdigit():
                error = "Пожалуйста, введите только целые числа."
            else:
                min_val = int(min_str)
                max_val = int(max_str)

                # Генерируем случайное число
                random_number = random.randint(min_val, max_val)
        except KeyError:
            error = "Произошла ошибка при получении данных формы."
        except ValueError:
            error = "Произошла ошибка при преобразовании чисел, -18 меньше, чем -12, 6 меньше, чем 28."

    return render_template('index.html', random_number=random_number, error=error)
@app.route('/connect_me')
def connect():
    return render_template('connect_me.html')
@app.route('/documents')
def documents():
    return render_template('documents.html')
# @app.route('/login')
# def login():
#     return render_template('login.html')
# @app.route('/register')
# def register():
#     return render_template('register.html')
@app.route('/education')
def education():
    return render_template('education.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         row = db.users.get('login', request.form['login'])
#         gh = db.users.get('email', request.form['email'])
#         if not row:
#             return render_template('login.html', error='Неправильный(ая) логин или пароль или почта')
#         if not gh:
#             return render_template('login.html', error='Неправильный(ая) логин или пароль или почта')
#         if request.form['password'] == row.password:
#             user = User(login)  # Создаем пользователя
#             login_user(user)  # Логинем пользователя
#             return redirect(url_for('index'))
#         else:
#             return render_template('login.html', error='Неправильный(ая) логин или пароль или почта')
#     return render_template('login.html')


# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return 'Пока'

if __name__ == "__main__":
    app.run(debug=True)