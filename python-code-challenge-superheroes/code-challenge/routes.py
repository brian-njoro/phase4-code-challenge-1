from flask import Flask, current_app, make_response, request, jsonify, g
from models.power import Power
from models.hero import Hero, db
from flask_cors import CORS
import os

def create_app():
    app = Flask(__name__)
    
    # Allow CORS for all routes
    CORS(app)
    app.config.from_object('config.Config')
    db.init_app(app)

    @app.before_request
    def app_path():
        g.path = os.path.abspath(os.getcwd())

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

    # PATCH /powers/:id
    @app.route('/powers/<int:id>', methods=['PATCH'])
    def update_power(id):
        data = request.json
        description = data.get('description')

        power = Power.query.get(id)

        if not power:
            return jsonify({"error": "Power not found"}), 404

        if description is not None:
            power.description = description

        try:
            db.session.commit()
            return jsonify({
                "id": power.id,
                "name": power.name,
                "description": power.description
            })
        except Exception as e:
            return jsonify({"errors": ["validation errors"]}), 400

    return app
