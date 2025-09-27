from email.policy import default

from flask import render_template, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# login_manager = LoginManager()
# login_manager.init_app(app)
db=SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    title = db.Column(db.String(100), primary_key=True, nullable=False)
    intro = db.Column(db.String(300), primary_key=True, nullable=False)
    text = db.Column(db.Text, primary_key=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Article %r>' % self.id
@app.route('/')
def index():
    return render_template('index.html')
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

if __name__ == "__main__":
    app.run(debug=True)