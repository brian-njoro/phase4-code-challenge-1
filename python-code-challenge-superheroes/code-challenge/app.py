#!/usr/bin/env python3
from flask_migrate import Migrate
from routes import db
from routes import create_app
# app initialization
app = create_app()

# Configure the FLASK migrations 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Migrate(app,db)

if __name__ == '__main__':
    app.run(debug=True, port=5000)