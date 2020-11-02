# set up dependencies
from flask import Flask, render_template

# establish app
app = Flask(__name__)

# landing page route
@app.route("/")
def index():
    return render_template("index.html")

# cloudiness vizualization route
@app.route("/cloudiness")
def cloudiness():
    return render_template("cloudiness.html")

# humidity vizualization route
@app.route("/humidity")
def humidity():
    return render_template("humidity.html")

# temperature vizualization route
@app.route("/temperature")
def temperature():
    return render_template("temperature.html")

# windspeed vizualization route
@app.route("/windspeed")
def windspeed():
    return render_template("windspeed.html")

# comparisons route
@app.route("/Comparisons")
def comparisons():
    return render_template("comparisons.html")

# data route
@app.route("/Data")
def data():
    return render_template("data.html")

if __name__ == "__main__":
    app.run(debug=True)