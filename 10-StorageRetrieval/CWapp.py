#Import dependencies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#Set up database connection
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)


#Homepage listing available routes
@app.route("/")
def welcome():
    return (
        f"Welcome to the Honolulu Weather API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )


#Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of precipitation data gathered for the last 12 months"""
    session = Session(engine)
    annual = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()

    session.close()

    #Create a dictionary of the query results
    dailyprecip = []
    for date, prcp in annual:
        precip_dict = {}
        precip_dict["date"] = date
        precip_dict["prcp"] = prcp
        dailyprecip.append(precip_dict)

    return jsonify(dailyprecip)

#Station route
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of stations in Honolulu"""
    #Query all stations
    session = Session(engine)  
    stationlist = session.query(Measurement.station).group_by(Measurement.station).all()

    session.close()

    # Convert list of tuples into normal list
    all_stations = list(np.ravel(stationlist))

    return jsonify(all_stations)

#Temperature route
@app.route("/api/v1.0/tobs")
def temperature():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of temperatures over the last year"""
    session = Session(engine)
    temps = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= '2016-08-23').\
        group_by(Measurement.date).all()

    session.close()

    #Create a dictionary of the query results
    dailytobs = []
    for date, tobs in temps:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        dailytobs.append(tobs_dict)

    return jsonify(dailytobs)

#Start Date route
@app.route("/api/v1.0/<start>")
def startdate():
    return jsonify(TBD-startdate)

#Start & End Date route
@app.route("/api/v1.0/<start>/end")
def startenddate():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of temperatures over the period 2/28/2011 to 3/5/2011"""
    session = Session(engine)
    def calc_temps(start_date, end_date):
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    return jsonify(calc_temps('2011-02-28', '2011-03-05'))

if __name__ == "__main__":
    app.run(debug=True)
