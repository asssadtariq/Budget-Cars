from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("home.html", title="Budget Cars | Home")

@app.route("/showroom")
def showroom():
    return render_template("showroom.html", title="Budget Cars | Showroom")

@app.route("/vans")
def vans():
    return render_template("vehicles.html", title="Budget Cars | Showroom")

@app.route("/cars")
def cars():
    return render_template("vehicles.html", title="Budget Cars | Cars")

@app.route("/parts-exchange")
def parts_exchange():
    return render_template("parts_exchange.html", title="Budget Cars | Parts Exchange")

@app.route("/warranty")
def warranty():
    return render_template("warranty.html", title="Budget Cars | Warranty")

@app.route("/finance")
def finance():
    return render_template("finance.html", title="Budget Cars | Finance")

@app.route("/contact-us")
def contact_us():
    return render_template("contact.html", title="Budget Cars | Contact Us")

if __name__ == "__main__":
    app.run(debug=True)


