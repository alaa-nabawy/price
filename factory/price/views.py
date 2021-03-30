from flask import render_template, Blueprint
from factory import db
from factory.models import Price
import random
import schedule
import time

price = Blueprint('price', __name__)

def value():
    value = random.randint(1,1000000)

    price_value = Price.query.get(1)

    if price_value is not None:

        price_value.value = value
        db.session.commit()

    else:

        new_price = Price(value = value)
        db.session.add(new_price)
        db.session.commit()

    price_value = Price.query.get(1)

@price.route('/refresh')
def change():

    schedule.every(0.5).seconds.do(value)

    while True:
        schedule.run_pending()
        time.sleep(0.5)