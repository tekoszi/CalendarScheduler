import json
import os
from calendar import weekday, monthlen
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'db.json')
    current_month = datetime.today().month
    current_year = datetime.today().year
    current_day = datetime.today().day
    # keep those variables in localstorage
    # allways when home page is run those should be writen from localstorage
    # localStorage.setItem(key, value);
    # localStorage.getItem(key)

    # we should clear local storage for current month to be default when you run app again.
    #
    firstDay = weekday(current_year, current_month, 1)
    monthLength = monthlen(current_year, current_month)

    def loadDB():
        with open(filename, mode='r') as json_file:
            db = json.load(json_file)
            return db

    def witeDB(db):
        with open(filename, mode='w') as json_file:
            json.dump(db, json_file)

    db = loadDB()
    people = db["people"]
    numbersOfPeople = len(people)

    return render_template('main.html',
                           people=db['people'],
                           weekdays=db["weekdays"],
                           nameOfMonth=db["months"][current_month - 1],
                           numbersOfDays=monthLength,
                           numbersOfPeople=numbersOfPeople,
                           firstDay=firstDay,
                           current_month=current_month,
                           months=db['months']

                           )


@app.route("/calculateMonthDays", methods=["GET", "POST"])
def previousMonth():
    # decrement current month
    # keep those variables in localstorage
    # allways when home page is run those should be writen from localstorage
    # localStorage.setItem(key, value);
    # localStorage.getItem(key)
    return render_template('main.html')


def nextMonth():
    # increment current month
    # keep those variables in localstorage
    # allways when home page is run those should be writen from localstorage
    # localStorage.setItem(key, value);
    # localStorage.getItem(key)
    return render_template('main.html')
    # return render_template('main.html', monthrange=monthrange(year, month))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
