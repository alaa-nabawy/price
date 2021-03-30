from flask import render_template, Blueprint, jsonify
from factory.models import Price

endpoint = Blueprint('endpoint', __name__)

@endpoint.route('/api_endpoint')
def api_endpoint():
    price_value = Price.query.get(1)

    return jsonify({'value': price_value.value})