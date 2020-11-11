from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import sqlalchemy
import numpy as np
import datetime as dt

app = Flask(__name__)

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
Measurement = Base.classes.measurement
Station = Base.classes.station


@app.route("/")
def home():
    return(
        f"Welcome to my homepage!<br/><br/>"  
        f"Here's what you can check out:<br/><br/>"
        f"To see precipitation data, add this to the URL: /api/v1.0/precipitation<br/>"
        f"To see a list of stations, add this to the URL: /api/v1.0/stations<br/>"
        f"To see temperature data for the past year, add this to the URL: /api/v1.0/tobs<br/>"
        f"To see min/max/avg temperature data since a specific date, add this to the URL, and simply include your chosen date (format yyyy-mm-dd) at the end: /api/v1.0/temperature/<start><br/>"
        f"To see min/max/avg temperature data for a specific range of dates, add this to your URL, with your chosen start date and end date on either side of the final / : /api/v1.0/temperature_range/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    date_prcp = session.query(Measurement.date, Measurement.prcp).all()
    session.close()
    result = {date:prcp for date,prcp in date_prcp}
    return jsonify(result)

@app.route("/api/v1.0/stations")
def station():
    session = Session(engine)
    station_list = session.query(Station.station).all()
    session.close()
    result = list(np.ravel(station_list))
    return jsonify(result)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
        
    tobs_list = session.query(Measurement.tobs).\
                filter(Measurement.station == 'USC00519281').\
                filter(Measurement.date >= year_ago).all()
    session.close()
    result = list(np.ravel(tobs_list))
    return jsonify(result)
        
@app.route("/api/v1.0/temperature/<start>")
def temperature(start=None):
    session = Session(engine)
    temp_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).all()
    session.close()
    result = list(np.ravel(temp_stats))
    return jsonify(result)

@app.route("/api/v1.0/temperature_range/<start>/<end>")
def temperature_range(start=None, end=None):
    session = Session(engine)
    temp_stats2 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).\
    filter(Measurement.date <= end).all()
    session.close()
    result = list(np.ravel(temp_stats2))
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)