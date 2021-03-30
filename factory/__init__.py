import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
from threading import Lock
import time
import datetime

app = Flask(__name__)


####################
## Database Setup ##
####################

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

Migrate(app, db)


################################
## Blueprints ##################
################################
from factory.price.views import price
from factory.generals.views import endpoint

app.register_blueprint(price)
app.register_blueprint(endpoint)
