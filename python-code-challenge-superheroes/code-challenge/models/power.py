from .dbconfig import db
from .heropower import hero_power
from datetime import datetime
from sqlalchemy.orm import validates

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError('Description must be at least 20 characters long')
        return description

    
    heroes = db.relationship(
        'Hero',
        secondary=hero_power, 
        back_populates='powers'
    )

    def __repr__(self):
        return f"<Power(id={self.id}, name='{self.name}', description='{self.description}')>"

