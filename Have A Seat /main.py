from pymongo import MongoClient
import flask
from flask import Flask,url_for , redirect, session ,flash,request
from flask import request
from flask import render_template
import bson.objectid
from bson.objectid import ObjectId
#import flask_login
import json

app= Flask(__name__)
con = MongoClient()
db = con.Have_A_Seat


#list=[]
#dic={}

@app.route('/', methods=['GET', 'POST'])
def Homepage():
    if (request.method == "POST"):
        restaurant_searched = request.form['search']
        print restaurant_searched
        restaurantList = db.Restaurants.find({"restName": restaurant_searched})
        for restaurant in restaurantList:
            list = str(restaurant['restName'])
            link = "/" + restaurant_searched + "/checkSeats"
            global dic
            dic = {"Restaurant": [[list, link]]}

        # print dic
        #return redirect(url_for('restaurantList'))

    return render_template("index.html")


# @app.route('/hello/', methods=['POST'])
# def index():
#     restaurant_searched = request.form['search']
#     print restaurant_searched


#
@app.route('/restaurants', methods=['POST'])
def restaurants():
    print  " Hello I am in"
    restaurant_searched = request.get_json()
    res=str(restaurant_searched['search'])
    print res
    return json.dumps([{'id': 123, 'name': 'aaa'}, {'id': 456, 'name': 'bbb'}, {'id': 789, 'name': 'ccc'}])

    #return render_template("index.html")

    restaurant_searched = request.get_json()
    # print restaurant_searched
    # restaurantList = db.Restaurants.find({"restName": str(restaurant_searched['search'])})
    # for restaurant in restaurantList:
    #     list = str(restaurant['restName'])
    #     link = "/" + restaurant_searched + "/checkSeats"
    #     global dic
    #     dic = {"Restaurant": [[list, link]]}

    #print restaurantList
    # return json.dumps([{'id':123,'name':'aaa'},{'id':456,'name':'bbb'},{'id':789,'name':'ccc'}])

#
#
# @app.route('/searchRestaurants', methods=['POST'])
# def searchRestaurants():
#     print 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx'
#     # print request.form['search']
#     return json.dumps([{'id':123,'name':'aaa'},{'id':456,'name':'bbb'},{'id':789,'name':'ccc'}])
#
#
# # this is the home page which loads first
# @app.route('/', methods=['GET', 'POST'])
# def Homepage():
#     if (request.method == "POST"):
#         restaurant_searched = request.form['search']
#         print restaurant_searched
#         restaurantList = db.Restaurants.find({"restName":restaurant_searched})
#         for restaurant in restaurantList:
#             list = str(restaurant['restName'])
#             link = "/" + restaurant_searched + "/checkSeats"
#             global dic
#             dic = {"Restaurant": [[list, link]]}
#
#         #print dic
#         return redirect(url_for('restaurantList'))
#
#     return  render_template("index.html")
#
#
#
# @app.route('/hello')
# def hello():
#     return json.dumps({id:123,'name':'aaa','name':'bbb','name':'ccc'})
#
#
# # when user searches for restaurent this page gets loaded
# @app.route('/restaurantList/')
# def restaurantList():
#    # restaurantList = Restaurants.find({"restName": restaurant_seached})
#    # for restaurant in restaurantList:
#        # list= str(restaurant['restName'])
#        # link="/" + restaurant_seached + "/checkSeats"
#        # dic={"Restaurant" : [[list, link]]}
#     global dic
#     #print dic
#     # return render_template("restaurantList.html", dic = dic)
#     return json.dump(dic)
#
# """
# @app.route('/dashboard/')
# def dashboard():
#     return render_template('dashboard.html')"""
#
#
# @app.route('/<string:restaurant_name>/checkSeats')
# def checkSeats(restaurant_name):
#     """user reaches here after selecting the restaurant name
#     """
#     #totalRestaurants = mongo.db.Restaurants
#
#     #rest_cursor = mongo.db.Restaurants.find({"restName": "subway"})
#
#     restID = db.Restaurants.find({"restName": restaurant_name},{"_id":1})
#     print restID
#     myrestID =0
#     for i in restID:
#         myrestID = i["_id"]
#         print myrestID
#     totaltables = db.Tables.find({"Restid": myrestID})
#     tup = []
#     for i in totaltables:
#         if i["isAvailable"] == 0:
#             i["isAvailable"] = "available"
#
#         if i["isAvailable"] == 1:
#             i["isAvailable"] = "booked"
#
#         if i["isAvailable"] == 2:
#             i["isAvailable"] = "unavailable"
#         tup.append((i["isAvailable"]))
#
#     #tup = tuple(tup)
#     #print tup
#     #total_counter = 0
#     #Customer_booked_counter =0
#     #Available_counter =0
#     #Owner_booked_counter =0
#     #availableTableNo = []
#     #CustomerbookedTableNo = []
#     #OwnerBookedTableNo = []
#
#
#     #for i in totaltables:
#     #    if(i["isAvailable"]==0):
#     #        #Available_counter +=1
#     #        #availableTableNo.append(i["TableNo"])
#     #   elif(i["isAvailable"]==1):
#     #        Customer_booked_counter +=1
#     #    elif (i["isAvailable"] == 2):
#     #        Owner_booked_counter += 1
#     #    total_counter +=1
#
#     """seat_details= "This Restaurant has "+ str(total_counter) + " seats of which "\
#            + str(Available_counter)+"  Available , " \
#            + str(Customer_booked_counter) + "  customer booked , " \
#            + str(Owner_booked_counter) + " owner booked ."
#     """
#     #return 'Hello'
#     return render_template("restaurant.html", seat_details=tup, restaurant_name=restaurant_name)
#
# @app.route('/seatBooked', methods = ['GET','POST'])
# def success():
#     if (request.method == "POST"):
#         table_updated = request.form['seatId']
#         print table_updated
#     return table_updated
#
# # this is the authenticate route
# @app.route('/register', methods=['GET','POST'])
# def Register():
#     # print 'u have readched login'
#     # print request.form.get('email')
#     # print request.form.get('password')
#     return render_template('register.html'), 200
#
# @app.route('/registerUser', methods=['POST'])
# def registerUser():
#     print 'u have readched regitserter user'
#     print request.form.get('email')
#     print request.form.get('password')
#     email = request.form.get('email')
#     password = request.form.get('password')
#
#     # restID = db.Users.insert_one({'email':email,'password':password})
#     restID = db.Customers.update_one({'email':email},{'$set':{'password':password}},upsert=True)
#     print restID
#     print 'inserted'
#     #print("you're logged in as:"+session['email'])
#     return render_template("index.html")
#
# @app.route('/login', methods=['GET','POST'])
# def Login():
#     if request.method=='GET':
#         return render_template("LogIn.html")
#     if request.method == 'POST':
#         print("In Post")
#         login_user = db.Customers.find_one({'email' : request.form['email']})
#         if login_user:
#             print("FOUNDDD")
#             print login_user['password']
#
#             if(request.form['password']==login_user['password']):
#                 session['email'] = request.form['email']
#                 if(session['email']=='abc@xyz.com'):
#                     return redirect(url_for('checkOwnerSeats',restaurant_name="subway"))
#                 return redirect(url_for('checkSeats', restaurant_name="subway"))
#             return("Invalid Password")
#
#          #   if bcrypt.hashpw(request.form['passwrd'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
#          #       return redirect(url_for('Restaurants'))
#             #print("Invalid Password")
#
#     return ("invalid username")
#         #db.Customers.find({'userame':username})
#
#    # restaurantList = Restaurants.find({"restName": restaurant_seached})
#    # for restaurant in restaurantList:
#        # list= str(restaurant['restName'])
#        # link="/" + restaurant_seached + "/checkSeats"
#        # dic={"Restaurant" : [[list, link]]}
#     #return render_template("Login.html", dic = dic)
#
# @app.route('/<string:restaurant_name>/checkOwnerSeats')
# def checkOwnerSeats(restaurant_name):
#     print("you're logged in as:" + session['email'])
#     """user reaches here after selecting the restaurant name
#     """
#     #totalRestaurants = mongo.db.Restaurants
#     #rest_cursor = mongo.db.Restaurants.find({"restName": "subway"})
#
#     restID = db.Restaurants.find({"restName": restaurant_name},{"_id":1})
#     print restID
#     myrestID =0
#     for i in restID:
#         myrestID = i["_id"]
#         print myrestID
#     totaltables = db.Tables.find({"Restid": myrestID})
#     tup = []
#     for i in totaltables:
#         if i["isAvailable"] == 0:
#             i["isAvailable"] = "available"
#
#         if i["isAvailable"] == 1:
#             i["isAvailable"] = "booked"
#
#         if i["isAvailable"] == 2:
#             i["isAvailable"] = "unavailable"
#         tup.append((i["isAvailable"]))
#     return render_template("restaurantOwner.html", seat_details=tup, restaurant_name=restaurant_name)
#
# @app.route('/logout')
# def logout():
#     if True:
#         session.clear()
#         #print("you're logged in as:" + session['email'])
#         return 'Logged out'
#     return "noone is logged in"
#

if __name__ == "__main__":
   # app.secret_key= 'mysecret'
    app.run(host="127.0.0.1", port=8089, debug=True)




