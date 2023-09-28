from .dbconfig import db
from datetime import datetime

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

    # powers = db.relationship(
    #     'Power',
    #     secondary='hero_powers',
    #     backref='heroes',
    # )
    hero_powers = db.relationship(
        'HeroPower',
        backref='associated_hero',
        primaryjoin="Hero.id == HeroPower.hero_id"  
    )

    powers = db.relationship(
        'Power',
        secondary='hero_powers',
        backref='heroes',
        overlaps="associated_hero,hero_powers"

    )



    def __repr__(self):
        return f"<Hero(id={self.id}, name='{self.name}', super_name='{self.super_name}')>"