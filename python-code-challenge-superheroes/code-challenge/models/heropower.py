from .dbconfig import db
from sqlalchemy import CheckConstraint
from datetime import datetime
from sqlalchemy.orm import validates


class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    hero = db.relationship('Hero', backref='hero_powers')
    power = db.relationship('Power', backref='hero_powers')

    @validates('strength')
    def validate_strength(self, key, value):
        strength_level = ['Strong', 'Weak', 'Average']
        if value not in strength_level:
            raise ValueError("Invalid strength value")
        return value


    def __repr__(self):
        return f"<HeroPower(id={self.id}, strength='{self.strength}', hero_id={self.hero_id}, power_id={self.power_id})>"
