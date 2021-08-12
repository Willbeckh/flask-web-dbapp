import psycopg2
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) # flask object instance

# app configs for DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:passwd123@localhost/feedbackdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'not so secret'
db = SQLAlchemy(app)

from models import Feedback

# db connect and cursor method
connection = psycopg2.connect(database='feedbackdb', user='postgres', password='passwd123', host='localhost', port='5432')
cursor = connection.cursor() #initiate a cursor

@app.route('/')
def index():
  return render_template('index.html', title='Feedback')


@app.route('/feedback')
def feedback():
  return render_template('form.html')


@app.route('/details', methods=['POST'])
def details():
  username = request.form['username']
  comment = request.form['comment']
  new_feed = Feedback(username, comment)
  # stage & push to db
  db.session.add(new_feed)
  db.session.commit()

  return render_template('index.html', title="Home")


# rendering the data to teplate
@app.route('/getfeedback', methods=['GET', 'POST'])
def getfeedback():
  cursor.execute('SELECT * FROM feedback')
  posts = cursor.fetchall()
  return render_template('feedback.html', data=posts)



if __name__ == '__main__':
  db.create_all() # create db data
  app.run(debug=True)
