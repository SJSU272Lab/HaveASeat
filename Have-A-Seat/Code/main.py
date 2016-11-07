from pymongo import MongoClient
import flask
from flask import Flask,url_for , redirect ,flash
from flask import request
from flask import render_template

con = MongoClient()
db = con.Have_A_Seat
Customers = db.Customers
Restaurants = db.Restaurants
Tables = db.Tables

app= Flask(__name__)
list=[]
dic={}

# this is the home page which loads first
@app.route('/', methods=['GET', 'POST'])
def Homepage():
    if (request.method == "POST"):
        restaurant_searched = request.form['search']
        print restaurant_searched
        restaurantList = Restaurants.find({"restName":restaurant_searched})
        for restaurant in restaurantList:
            list = str(restaurant['restName'])
            link = "/" + restaurant_searched + "/checkSeats"
            dic = {"Restaurant": [[list, link]]}
        return redirect(url_for('Restaurants'))

    return  render_template("index.html")


# when user searches for restaurent this page gets loaded
@app.route('/Restaurants/')
def Restaurants():
   # restaurantList = Restaurants.find({"restName": restaurant_seached})
   # for restaurant in restaurantList:
       # list= str(restaurant['restName'])
       # link="/" + restaurant_seached + "/checkSeats"
       # dic={"Restaurant" : [[list, link]]}
    return render_template("restaurant.html", dic = dic)

"""
@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')"""


# this function loads a html page which shows the seat details for a user selected restaurant
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
    Customer_booked_counter =0
    Available_counter =0
    Owner_booked_counter =0

    for i in totaltables:
        if(i["isAvailable"]==0):
            Available_counter +=1
        elif(i["isAvailable"]==1):
            Customer_booked_counter +=1
        elif (i["isAvailable"] == 2):
            Owner_booked_counter += 1
        total_counter +=1

    seat_details= "This Restaurant has "+ str(total_counter) + " seats of which "\
           + str(Available_counter)+"  Available , " \
           + str(Customer_booked_counter) + "  customer booked , " \
           + str(Owner_booked_counter) + " owner booked ."

    return render_template("restaurant.html", seat_details=seat_details, dic=dic)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8082)




