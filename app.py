from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///speczap.db'
app.config['SQLALCHEMY_TRACK_MOIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    telephone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), unique=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Article {self.id}"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ads')
def ads():
    return render_template('ads.html')


@app.route('/buy')
def buy():
    return render_template('buy.html')


@app.route('/sale')
def sale():
    return render_template('sale.html')






if __name__ == "__main__":
    app.run(debug=True)
