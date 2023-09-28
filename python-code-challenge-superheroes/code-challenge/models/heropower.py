from .dbconfig import db
from datetime import datetime
from sqlalchemy.orm import validates

hero_power = db.Table(
    'hero_powers',
    db.Column('hero_id', db.Integer, db.ForeignKey('heroes.id'), primary_key=True),
    db.Column('power_id', db.Integer, db.ForeignKey('powers.id'), primary_key=True),
    db.Column("strength", db.String),
    db.Column("created_at", db.DateTime, server_default=db.func.now()),
    db.Column("updated_at", db.DateTime, onupdate=db.func.now())
)


@validates('strength')
def validate_strength(self, key, value):
        strength_level = ['Strong', 'Weak', 'Average']
        if value not in strength_level:
            raise ValueError("Invalid strength value")
        return value


def __repr__(self):
        return f"<HeroPower(id={self.id}, strength='{self.strength}', hero_id={self.hero_id}, power_id={self.power_id})>"
