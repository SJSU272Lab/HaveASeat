from pymongo import MongoClient
import flask
from flask import Flask, jsonify
from flask import request
from flask import render_template

con = MongoClient()
db = con.hockey
Customers = db.Customers
Restaurants = db.Restaurants
Tables = db.Tables

app= Flask(__name__)
list=[]
list1=[]
@app.route('/')
def getRastaurent():
    check = Restaurant.find()
    for i in check:
        list= str(i['name'])
        list1.append(list)
    return render_template("restaurant.html", list = list1)

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/<string:restaurant_name>/checkSeats')
def checkSeats(restaurant_name):
    """user reaches here after selecting the restaurant name
    """
    #totalRestaurants = mongo.db.Restaurants

    #rest_cursor = mongo.db.Restaurants.find({"restName": "subway"})
    restID = Restaurants.find({"restName": restaurant_name},{"_id":1})
    print restID
    myrestID =0
    for i in restID:
        myrestID = i["_id"]
        print myrestID
    totaltables = Tables.find({"Restid": myrestID})
    total_counter = 0
    booked_counter =0
    for i in totaltables:
        if(i["isBooked"]):
            booked_counter +=1
        total_counter +=1

    return "This Restaurant has "+ str(total_counter) + " seats of which "+ str(booked_counter)+" are booked"


"""@app.route('/<string:restaurant_name>')
def getSeat(restaurant_name):
    check= Restaurant.find_one({"name": restaurant_name})
   # return  str(check['seat'])
"""
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8082)




