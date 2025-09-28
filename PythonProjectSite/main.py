from flask import render_template, url_for
from flask import Flask

app = Flask(__name__)

# login_manager = LoginManager()
# login_manager.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/connect_me')
def connect():
    return render_template('connect_me.html')
@app.route('/documents')
def documents():
    return render_template('documents.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/education')
def education():
    return render_template('education.html')

if __name__ == "__main__":
    app.run(debug=True)