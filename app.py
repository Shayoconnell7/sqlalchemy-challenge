from Flask import Flask

app = Flask(__name__)

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()
measurement = Base.classes.measurement
station = Base.classes.station


@app.route("/")
def home():
    return(
        f"Welcome to my homepage!<br/><br/>"  
        f"Here's what you can check out:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"

@app.route("/api/v1.0/precipitation<br/>")

session = Session(engine)
first_m_row = session.query(measurement).all()
first_m_row.__dict__





if __name__ == "__main__":
    app.run(debug=True)
