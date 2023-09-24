from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import datetime
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

# hero_powers = db.Table(
#     'hero_powers',
#     db.Column('hero_id', db.Integer, db.ForeignKey('hero.id'), primary_key=True),
#     db.Column('power_id', db.Integer, db.ForeignKey('powers.id'), primary_key=True),
#     db.Column('strength', db.String(255)),
#     db.Column('created_at', db.DateTime, default=db.func.current_timestamp()),
#     db.Column('updated_at', db.DateTime, default=db.func.current_timestamp())
# )

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')

    powers = db.relationship(
        'Power',
        secondary='hero_powers',
        back_populates='heroes',
        viewonly=True,
        primaryjoin="Hero.id == hero_powers.c.hero_id",
        secondaryjoin="Power.id == hero_powers.c.power_id",
    )

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError('Description must be at least 20 characters long')
        return description

    hero_powers = db.relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')

    heroes = db.relationship(
        'Hero',
        secondary='hero_powers',
        back_populates='powers',
        viewonly=True,
        primaryjoin="Power.id == hero_powers.c.power_id",
        secondaryjoin="Hero.id == hero_powers.c.hero_id",
    )

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, CheckConstraint('strength IN ("Strong", "Weak", "Average")'))
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    hero = db.relationship('Hero', back_populates='hero_powers', primaryjoin=hero_id == Hero.id)
    power = db.relationship('Power', back_populates='hero_powers', primaryjoin=power_id == Power.id)
