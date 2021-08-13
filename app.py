from flask import Flask
from Geocoder_Search import Geocoder_Search
from Database import db
import logging
from gevent.pywsgi import WSGIServer


def create_app():
    app = Flask(__name__)

    # Database configuration and creating a database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Address.db'

    db.init_app(app)

    with app.app_context():
        #db.drop_all()
        db.create_all()

    return app

# Creating an app
app = create_app()

# Registering a geo_search blueprint
app.register_blueprint(Geocoder_Search)

if __name__ == "__main__":
    app.run(debug=True)
