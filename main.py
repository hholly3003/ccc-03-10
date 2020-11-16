#main.py should only concern in creating the application itself

#Loading environment variables
from dotenv import load_dotenv
load_dotenv()

#Flask application creation
from flask import Flask
app = Flask(__name__)

#Database connection
from database import init_db
db = init_db(app)

#Setup Serialization and Deserialization
from flask_marshmallow import Marshmallow
ma = Marshmallow(app)

#Controller registrations
from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)