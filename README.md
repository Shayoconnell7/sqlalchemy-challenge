# sqlalchemy-challenge


## Step 1 - Climate Analysis and Exploration


* I used SQLAlchemy `create_engine` to connect to the sqlite database, followed by `automap_base()` to reflect those tables into classes, which I saved  references to called `Station` and `Measurement`.

### Precipitation Analysis

* After using DateTime to calculate and store a variable for the past year, I used a filter to retrieved the last 12 months of precipitation data.

* I loaded my query results into a Pandas DataFrame  called past_year_prcp, and set the index to the date column, which I also sorted by.

* I plotted the results using the into a line chart, and adjusted the line width and figure size to make it easy to see..

* I then used Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* I calculated the total number of stations usinf a for loop and .distinct().

* By using .count, .group_by, and .order_by, I found the most active station: 'USC00519281'.

* I then used filters to find the minimun, maximum, and average temperature for that station. 

* I then checked that that station had the most temperature data (it did) and retrieved the past year's worth of temperature observation data for that station.

* I turned my results into a dataframe called past_year_temps and plotted it as a histogram with 12 bins

## Step 2 - Climate App


### Routes

* `/`

  * I created a Home page.

  * It lists all routes that are available.

* `/api/v1.0/precipitation`

  * On this page it returns the JSON representation of a dictionary of precipitation with `date` as the key and `prcp` as the value.

* `/api/v1.0/stations`

  * On this page it returns a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  
  * On this page it returns a JSON list of temperature observations (TOBS) for the previous year for the most active station.

* `/api/v1.0/temperature/<start>` 

  * On this page it returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start.

* `/api/v1.0/temperature/<start>/<end>`
  * On this page it returns a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start-end range.
