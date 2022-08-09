# import dependencies
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Grants access and allows us to query SQLite database file hawaii
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes

Base = automap_base()
Base.prepare(engine, reflect=True)

#Save references to each table (the same ones as earlier in the module)
#Create variable for each class so that they can be referenced later

Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link from Python to database
session = Session(engine)

# Define flask app
app = Flask(__name__)

# Define welcome route ( which is root/homepage)
@app.route("/")

# Add routing information for other routes
# Create function with return statement as f-strings that reference the other routes
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# begin route for precipitation
@app.route("/api/v1.0/precipitation")

#create precipitation function
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

#create route to stations 
@app.route("/api/v1.0/stations")

# create stations function

def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

# create monthly temperature route
@app.route("/api/v1.0/tobs")

#create monthly temperature function

def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# create starting and ending date for temperatures
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# create stats function

def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

