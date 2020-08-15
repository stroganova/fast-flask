from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def render_main():
    tours = {}
    for i in range(1, 7):
       tours[i] = data.tours[i]
    return render_template('index.html',
                           tours=tours,
                           title=data.title,
                           subtitle=data.subtitle,
                           description=data.description)


@app.route('/departures/<departure>/')
def render_departure(departure):
    tours = {key: tour for key, tour in data.tours.items() if tour['departure'] == departure}
    departure_string = data.departures[departure]
    return render_template('departure.html',
                           tours=tours,
                           departure=departure_string)


@app.route('/tours/<id>/')
def render_tour(id):
    tour = data.tours[int(id)]
    departure_string = data.departures[tour['departure']]
    return render_template('tour.html',
                           tour=tour,
                           departure=departure_string)


if __name__ == '__main__':
    app.run()