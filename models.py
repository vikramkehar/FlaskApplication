# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    date_of_birth = db.Column(db.Date)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), server_onupdate=db.func.current_timestamp())
    projectid=db.Column(db.Integer)
    projects = db.relationship('Project', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(64), index=True)
    alloted_date = db.Column(db.Date)
    username = db.Column(db.String(80), db.ForeignKey('user.username'), nullable=False)

    def __repr__(self):
        return '<Project %r>' % self.project_id