#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db, render_as_batch=True)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = []
    for bakery in Bakery.query.all():
        dict = bakery.to_dict()
        bakeries.append(dict)
    response = make_response(
        jsonify(bakeries), 200, {"Content-Type": "application/json"}
    )
    return response

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    baked = Bakery.query.filter(Bakery.id == id).first()
    baked_dict = baked.to_dict()

    response = make_response(baked_dict, 200)
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    goods = []
    for good in BakedGood.query.order_by(BakedGood.price.desc()).all():
        dict = good.to_dict()
        goods.append(dict)
    response = make_response(jsonify(goods), 200)
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    pricey = BakedGood.query.order_by(BakedGood.price.desc()).first()
    dict = pricey.to_dict()

    response = make_response(dict, 200)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
