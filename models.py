# DB tables are defined here
from app import db


class Feedback(db.Model):
  __tablename__ = "feedback"
  
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(32))
  comment = db.Column(db.String(50))

  def __init__(self, username, comment):
    self.username = username
    self.comment = comment

  def __repr__(self):
      return f'id: {self.id}'


  # used when data is needed in JSON format
  # def serialize(self):
  #   return{
  #     'id': self.id,
  #     'Username': self.username,
  #     'Comment': self.comment
  #   }
