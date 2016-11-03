from pymongo import MongoClient
import flask
from flask import Flask, jsonify
from flask import request
from flask import render_template

con = MongoClient()
db = con.Have_A_Seat
Customers = db.Customers
Restaurants = db.Restaurants
Tables = db.Tables

app= Flask(__name__)
list=[]
list1=[]
@app.route('/')
def getRastaurent():
    check = Restaurants.find()
    for i in check:
        list= str(i['restName'])
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
    #for i in restID:
    #    myrestID = i["_id"]
    #    print myrestID
    totaltables = Tables.find({"Restid": restID["_id"]})
    total_counter = 0
    #booked_counter =0
    AvailableTablesNo = []
    AvailableTableCap = []
    BookedTablesNo  = []
    BookedTableCap = []
    InProgressTablesNo = []
    InProgressTableCap = []
    for i in totaltables:
        if(i["isAvailable"]==2): #isAvailable = 0 means free, 1 means booked by customer, 2 means booked by owner
            BookedTablesNo.append(i["TableNo"])
            BookedTableCap.append(i["Capacity"])
        if (i["isAvailable"] == 0):  # isAvailable = 0 means free, 1 means booked by customer, 2 means booked by owner
            AvailableTablesNo.append(i["TableNo"])
            AvailableTableCap.append(i["Capacity"])
        if (i["isAvailable"] == 1):  # isAvailable = 0 means free, 1 means booked by customer, 2 means booked by owner
            InProgressTablesNo.append(i["TableNo"])
            InProgressTableCap.append(i["Capacity"])

        total_counter +=1

    #return "This Restaurant has "+ str(total_counter) + " seats of which "+ str(len(BookedTables))+" are booked & "+str(len(AvailableTables)) +" are free & "+str(len(InProgressTables))+" are booked by customers"
    return render_template("restaurant.html",AvailableTablesNo = AvailableTablesNo,
                           BookedTablesNo = BookedTablesNo, InProgressTablesNo = InProgressTablesNo,
                           TotalSeats=total_counter, BookedTableCap = BookedTableCap, AvailableTableCap = AvailableTableCap,
                           InProgressTableCap = InProgressTableCap)

@app.route('/<string:restaurant_name>/userProfile/<int:TableNumber>')
def UserBookSeats(restaurant_name,TableNumber):
    """User reaches here after authentication"""
    TableID = Tables.find({"TableNo": TableNumber},{"_id":1})
    #Marking it booked by user
    result = Tables.update_one({"_id":TableID["_id"]},{"$set": {"isAvailable":1}})
    RestIDUpdated = TableID["RestID"]

    return render_template("restaurant.html", RestIDUpdated= RestIDUpdated,
                           TableNoUpdated= result["TableNo"], TableCapacity=result["Capacity"] )

@app.route('/<string:restaurant_name>/ownerProfile/<int:TableNumber>')
def OwnerBookSeats(restaurant_name,TableNumber):
    """Owner reaches here after the customer reaches at the restaurant"""
    TableID = Tables.find({"TableNo": TableNumber},{"_id":1})
    #Marking it booked by owner
    result = Tables.update_one({"_id":TableID["_id"]},{"$set": {"isAvailable":2}})
    RestIDUpdated = TableID["RestID"]

    return render_template("restaurant.html", RestIDUpdated= RestIDUpdated,
                           TableNoUpdated= result["TableNo"], TableCapacity=result["Capacity"] )

def OwnerReleaseSeats(restaurant_name,TableNumber):
    """Owner reaches here after the customer doesn't reach the restaurant"""
    TableID = Tables.find({"TableNo": TableNumber},{"_id":1})
    #Marking it booked by owner
    result = Tables.update_one({"_id":TableID["_id"]},{"$set": {"isAvailable":0}})
    RestIDUpdated = TableID["RestID"]

    return render_template("restaurant.html", RestIDUpdated= RestIDUpdated,
                           TableNoUpdated= result["TableNo"], TableCapacity=result["Capacity"] )


"""@app.route('/<string:restaurant_name>')
def getSeat(restaurant_name):
    check= Restaurant.find_one({"name": restaurant_name})
   # return  str(check['seat'])
"""
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8082, debug = True)




