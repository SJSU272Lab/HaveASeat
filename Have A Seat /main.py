import pymongo
from pymongo import MongoClient
import flask
from flask import Flask,url_for , redirect, session ,flash,request
from flask import request
from flask import render_template
import bson.objectid
from bson.objectid import ObjectId
#import flask_login
import json
from functools import  wraps
#from flask_login import LoginManager

app= Flask(__name__)
con = MongoClient("mongodb://abcd:qwerty@ds111798.mlab.com:11798/have_a_seat")
db = con.have_a_seat


#list=[]
#dic={}

#login_manager=LoginManager()
#login_manager.init_app(app)


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'email' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))
    return wrap

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

        print dic
    #return redirect(url_for('restaurantList'))

    return render_template("index.html")


# @app.route('/hello/', methods=['POST'])
# def index():
#     restaurant_searched = request.form['search']
#     print restaurant_searched




#
@app.route('/getSeats', methods=['POST'])
def getSeats():
    print  " Hello I am in"
    reqObj = request.get_json() #NEED REQUEST JSON
    #print reqObj
    rid=int(reqObj['restaurantId'])
    #print '------------------------'
    print rid
    rObj = db.Restaurants.find_one({"_id": rid})

    #'templateSeats':pizzaHutLayout - pizzaHutLayout
    #'templateSeats':mcDonaldsLayout - mcDonaldsLayout
    #'templateSeats':subwayLayout - subwayLayout
    #'templateSeats':starbucksLayout - starbucksLayout

    s_list = []
    sObj = db.Tables.find({"Restid":rid})

    for seat in sObj:
        print "Printing in sOBj"
        s_list.append({'sid':seat["_id"], 'status': seat['isAvailable']})

    print s_list

    return json.dumps({'id': rid, 'name': rObj["restName"], 'templateSeats':'pizzaHutLayout','seats':s_list})
    # return json.dumps({'id': 456, 'name': rObj["restName"], 'templateSeats':'subwayLayout','seats':[
    #     {'sid':101,'status':'available'},
    #     {'sid': 102, 'status': 'available'},
    #     {'sid': 103, 'status': 'booked'},
    #     {'sid': 104, 'status': 'available'},
    #     {'sid': 105, 'status': 'unavailable'},
    #     {'sid': 106, 'status': 'unavailable'},
    #     {'sid': 107, 'status': 'booked'},
    #     {'sid': 108, 'status': 'available'},
    #     {'sid': 109, 'status': 'booked'},
    #     {'sid': 110, 'status': 'unavailable'},
    #     {'sid': 111, 'status': 'unavailable'},
    #     {'sid': 112, 'status': 'available'},
    #     {'sid': 113, 'status': 'available'},
    #     {'sid': 114, 'status': 'unavailable'},
    #     {'sid': 115, 'status': 'available'},
    #     {'sid': 116, 'status': 'available'},
    # ]})


@app.route('/restaurants', methods=['POST'])
def restaurants():
    print  " Hello I am in"
    restaurant_searched = request.get_json()

    restname=str(restaurant_searched['search'])
    # print res
    dic=[]
    counter=1
    listOfRestaurants= db.Restaurants.find({"restName":restname})
    for i in listOfRestaurants:
        dic.append({"id":i['_id'], "name":str(i["restName"])})
    dic.append({"name": "Peanuts", "Street":"abc", "City": "nhb", "State":"CA"})
    print dic
    return json.dumps(dic)

    #return render_template("index.html")

    #restaurant_searched = request.get_json()
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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    print "I am inside"
    if (request.method == "POST"):
        cred = request.get_json()
        print cred
        obj = cred['cred']
        print obj
        firstname = obj['firstName']
        lastName = obj['lastName']
        emailid = obj['emailid']
        password = obj['password']
        checkIfExist=db.Customers.find_one({'email':emailid})
        if checkIfExist:
            print "Email already used"
            return "Email already used"
        try:
            print ("Inserted")
            db.Customers.insert_one({'customerName':firstname+" "+lastName,'email': emailid, 'password': password})
        except pymongo.errors.DuplicateKeyError:
            return "User Already Exists!!"
    print({'customerName': firstname + " " + lastName, 'email': emailid, 'password': password})
    return json.dumps({'customerName': firstname+" "+lastName, 'email': emailid, 'password': password})



@app.route('/login', methods=['GET','POST'])
def login():
    error= None
    if request.method == 'POST':

        cred = request.get_json()
        print cred
        obj = cred['cred']
       # print obj
        username = obj['username']
        password = obj['password']
        print username
        print password

        login_user = db.Customers.find_one({'Email': username})
        login_owner=db.Owners.find_one({'owner_email': username})
        if login_user:
            print (login_user['Password'])
            print("user is here")
            print login_user['Password']
            if(password == login_user['Password']):
                session['Email'] = username
                #return redirect(url_for('checkSeats', restaurant_name="subway"))
                print ("I am here")
                #return ("HII")
                return json.dumps({'email': login_user['Email'], 'name': login_user['customerName']})
            error = "Invalid Passowrd. Please try again."
           # return json.dumps({'email': username, 'name': login_user['customerName']})
            return render_template("LogIn.html", error=error)
        elif login_owner:
            print("owner is here")
            if(password == login_owner['owner_password']):
                ownerDetails = db.Owners.find_one({"owner_email": username})
                session['Email'] = username
                restaurantDetails=db.Restaurants.find_one({"_id": ownerDetails['Restid']})
                restaurantName=restaurantDetails['restName']
                return redirect(url_for('checkOwnerSeats', restaurant_name=restaurantName))
        error="Invalid Username"
        return render_template("LogIn.html", error=error)
    return render_template("LogIn.html", error=error)


@app.route('/<string:restaurant_name>/checkOwnerSeats')
@login_required
def checkOwnerSeats(restaurant_name):
    print("you're logged in as:" + session['email'])
    """user reaches here after selecting the restaurant name
         """
     #totalRestaurants = mongo.db.Restaurants
    #       #rest_cursor = mongo.db.Restaurants.find({"restName": "subway"})

    restID = db.Restaurants.find({"restName": restaurant_name},{"_id":1})
    print restID
    myrestID =0
    for i in restID:
        myrestID = i["_id"]
        print myrestID
    totaltables = db.Tables.find({"Restid": myrestID})
    tup = []
    for i in totaltables:
        if i["isAvailable"] == 0:
            i["isAvailable"] = "available"

        if i["isAvailable"] == 1:
            i["isAvailable"] = "booked"

        if i["isAvailable"] == 2:
            i["isAvailable"] = "unavailable"
        tup.append((i["isAvailable"]))
    return render_template("restaurantOwner.html", seat_details=tup, restaurant_name=restaurant_name)

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

@app.route('/bookSeat',methods=['POST'])
@login_required
def bookseat_user():
    print "Booking seats"
    seats = request.get_json()
    #Need RestaurantID/Name, seatsID,
    #I will update the DB



@app.route('/logout')
@login_required
def logout():
    if True:
        session.clear()
        #print("you're logged in as:" + session['email'])
        return 'Logged out'
    return "noone is logged in"

'''
def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if get_current_user_role() not in roles:
                return error_response()
            return f(*args, **kwargs)
        return wrapped
    return wrapper
'''

'''
@app.route('/user')
@required_roles('admin', 'user')
def user_page(self):
    return "You've got permission to access this page."
'''
if __name__ == "__main__":
    app.secret_key= 'mysecret'
    app.run(host="127.0.0.1", port=8000, debug=True)




