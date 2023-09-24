#!/usr/bin/env python3

from flask import Flask, make_response,request,jsonify
from flask_migrate import Migrate

from models import db, Hero,Power,HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# GET /heroes
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_list = [
        {"id": hero.id, "name": hero.name, "super_name": hero.super_name}
        for hero in heroes
    ]
    return jsonify(hero_list)

# GET /heroes/:id
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)

    if not hero:
        return jsonify({"error": "Hero not found"}), 404

    hero_data = {
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "powers": [
            {
                "id": power.id,
                "name": power.name,
                "description": power.description
            }
            for power in hero.powers
        ]
    }
    return jsonify(hero_data)

# GET powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    power_list = [
        {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        for power in powers
    ]
    return jsonify(power_list)

# GET /powers/:id
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)

    if not power:
        return jsonify({"error": "Power not found"}), 404

    power_data = {
        "id": power.id,
        "name": power.name,
        "description": power.description
    }
    return jsonify(power_data)



if __name__ == '__main__':
    app.run(port=5555)