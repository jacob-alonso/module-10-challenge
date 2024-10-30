# Import the dependencies.
import datetime as dt
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:////Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine)
#################################################
# Database Setup
#################################################
Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis Api <br/>",
        f"Available Routes: <br/>",
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    prv_year = dt.date(2017,8,23) - dt.timedelta(days=365)

    precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prv_year).all()
session.close()
# reflect an existing database into a new model

# reflect the tables


# Save references to each table


# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################




#################################################
# Flask Routes
#################################################
