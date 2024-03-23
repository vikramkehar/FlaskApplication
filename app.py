# app.py
from flask import Flask
from models import db
from user_blueprint import user_blueprint
from flask_cors import CORS

print("hi")
app = Flask(__name__)
CORS(app)

# MySQL configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Register the user blueprint
app.register_blueprint(user_blueprint)

# Run create_tables function within Flask application context
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run('127.0.0.1',3002,debug=True)
