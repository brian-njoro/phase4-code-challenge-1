from random import choice as rc, randint
from faker import Faker
from app import app, db
from models.heropower import hero_power
from models.hero import Hero
from models.power import Power
import random

fake = Faker()

def make_power():
    Power.query.delete()
    power = []
    for i in range(50):
        name = fake.name()
        description = fake.text()
        while len(description) < 20:
            description = fake.text(max_nb_chars=20)
        p = Power(name=name, description=description)
        power.append(p)

    db.session.add_all(power)
    db.session.commit()

def make_hero():

    Hero.query.delete()
    
    heroes = []
    for i in range(50):
        h= Hero(name=fake.name(), super_name = fake.name())
        heroes.append(h)

    db.session.add_all(heroes)
    db.session.commit()


def make_hero_power():
    combination = set()
    strengths = ["Strong","Weak","Average"]
    for _ in range(30):
        hero_id = randint(1,20)
        power_id = randint(1,20)
        strength = rc(strengths)

        if (hero_id,power_id,strength) in combination:
            continue
        combination.add((hero_id,power_id,strength))
        hero_power_data = {
            "hero_id": hero_id,
            "power_id": power_id,
            "strength": strength

        }

        statement = db.insert(hero_power).values(hero_power_data)

        db.session.execute(statement)
        db.session.commit()





if __name__ == '__main__':
    with app.app_context():
        make_hero()
        make_power()
        make_hero_power()
      