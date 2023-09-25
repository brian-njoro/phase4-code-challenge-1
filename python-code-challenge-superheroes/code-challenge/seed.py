

from random import choice as rc
from faker import Faker
from app import app, db  
from models.heropower import HeroPower
from models.hero import Hero
from models.power import Power

fake = Faker()

with app.app_context():
    # Delete existing data if needed (optional)
    db.session.query(HeroPower).delete()
    db.session.query(Hero).delete()
    db.session.query(Power).delete()

    # Create and add sample powers
    sample_powers = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]

    powers = [Power(**power_data) for power_data in sample_powers]
    db.session.add_all(powers)

    # Create and add sample heroes
    sample_heroes = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        
    ]

    heroes = [Hero(**hero_data) for hero_data in sample_heroes]
    db.session.add_all(heroes)

    strengths = ["Strong", "Weak", "Average"]

    hero_powers = []
    for hero in heroes:
        for _ in range(3):  
            power = rc(powers)
            strength = rc(strengths)
            hero_power = HeroPower(hero=hero, power=power, strength=strength)
            hero_powers.append(hero_power)

    db.session.add_all(hero_powers)

    # Commit the changes to the database
    db.session.commit()

print("Data seeding complete.")
