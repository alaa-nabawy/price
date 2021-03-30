import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import time
import datetime

app = Flask(__name__)


####################
## Database Setup ##
####################

basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = '3ca90a04c1a9ff7715ace458401960f674cd9ed84ef93004242e3bfc6e44735d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://cvpimsytamrpwe:3ca90a04c1a9ff7715ace458401960f674cd9ed84ef93004242e3bfc6e44735d@ec2-3-231-194-96.compute-1.amazonaws.com:5432/d2f00l61k9nd4h'
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
