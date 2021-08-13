from flask import Blueprint, request, render_template, redirect, url_for
import logging

from Database import geocode_table, db
from Geocoder import GEOCODER
from API_Key import API_Key
from Measure_Distance import Geodesic_dist  

Geocoder_Search = Blueprint('Geocoder_Search',__name__)

# Loggin configuration
logging.basicConfig(filename='MKAD_Distance_Searches.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

@Geocoder_Search.route('/', methods=['GET', 'POST'])
def index():
    Geocoder = GEOCODER(API_Key)

    if request.method == 'POST':
        # The address you want to find comes from this line
        Address_Content = request.form['Search_Address']      

        # The coordinates of the address searched using the Geocoder have been found.
        Coordinates = Geocoder.Coordinates(Address=Address_Content)

        # The distance between MKAD and specific address found.
        Distance_to_MKAD = Geodesic_dist(Coordinates).Km

        #The obtained data is prepared to be written to the database.
        New_Content = Geocode_Table(name = Address_Content, longitude = Coordinates[0], latitude = Coordinates[1], Distance_To_MKAD = Distance_to_MKAD)

        # The obtained data is written to the log file.
        logging.info(" Address: {}".format(Address_Content))
        logging.info(" Coordinates: {}".format(Coordinates))
        
        if(Distance_to_MKAD == 0):
            logging.info(" The location is already in MKAD")
        else:
            logging.info(" Distace to MKAD: {}".format(Distance_to_MKAD))

        # The prepared data is written to the database.
        try:
            db.session.add(New_Content)
            db.session.commit()
            return redirect('/')
        except:
            logging.error('There is a problem finding the address you want')
            return 'There is a problem finding the address you want'

    else:
        #It renders the Index.html page.
        Addresses = geocode_table.query.order_by(geocode_table.date_created).all()
        return render_template('index.html',Addresses = Addresses)
