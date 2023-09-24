# from models import Hero, HeroPower,Power,db

# # from app.app import db,app
# import random

# # Create sample powers
# sample_powers = [
#     {"name": "super strength", "description": "gives the wielder super-human strengths"},
#     {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
#     {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
#     {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
# ]

# for power_data in sample_powers:
#     power = Power(**power_data)
#     db.session.add(power)

# # Create sample heroes
# sample_heroes = [
#     {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
#     {"name": "Doreen Green", "super_name": "Squirrel Girl"},
#     {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
#     {"name": "Janet Van Dyne", "super_name": "The Wasp"},
#     {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
#     {"name": "Carol Danvers", "super_name": "Captain Marvel"},
#     {"name": "Jean Grey", "super_name": "Dark Phoenix"},
#     {"name": "Ororo Munroe", "super_name": "Storm"},
#     {"name": "Kitty Pryde", "super_name": "Shadowcat"},
#     {"name": "Elektra Natchios", "super_name": "Elektra"}
# ]

# for hero_data in sample_heroes:
#     hero = Hero(**hero_data)
#     db.session.add(hero)

# db.session.commit()

# # Create relationships between heroes and powers
# strengths = ["Strong", "Weak", "Average"]
# heroes = Hero.query.all()
# powers = Power.query.all()

# for hero in heroes:
#     for _ in range(random.randint(1, 3)):
#         power = random.choice(powers)
#         strength = random.choice(strengths)
#         hero_powers = HeroPower(hero=hero, power=power, strength=strength)
#         db.session.add(hero_powers)

# db.session.commit()

# print("🦸‍♀️ Done seeding!")





from models import Hero, HeroPower, Power, db
from app.app import app
import random

# Create sample powers
sample_powers = [
    {"name": "super strength", "description": "gives the wielder super-human strengths"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
]

# Create sample heroes
sample_heroes = [
    {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
    {"name": "Doreen Green", "super_name": "Squirrel Girl"},
    {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
    {"name": "Janet Van Dyne", "super_name": "The Wasp"},
    {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
    {"name": "Carol Danvers", "super_name": "Captain Marvel"},
    {"name": "Jean Grey", "super_name": "Dark Phoenix"},
    {"name": "Ororo Munroe", "super_name": "Storm"},
    {"name": "Kitty Pryde", "super_name": "Shadowcat"},
    {"name": "Elektra Natchios", "super_name": "Elektra"}
]

# Create relationships between heroes and powers
strengths = ["Strong", "Weak", "Average"]

if __name__ == '__main__':
    with app.app_context():
        for power_data in sample_powers:
            power = Power(**power_data)
            db.session.add(power)

        for hero_data in sample_heroes:
            hero = Hero(**hero_data)
            db.session.add(hero)

        db.session.commit()

        heroes = Hero.query.all()
        powers = Power.query.all()

        for hero in heroes:
            for _ in range(random.randint(1, 3)):
                power = random.choice(powers)
                strength = random.choice(strengths)
                hero_powers = HeroPower(hero=hero, power=power, strength=strength)
                db.session.add(hero_powers)

        db.session.commit()

    print("Done seeding!")

