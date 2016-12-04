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
import tweepy
from random import randint
import bcrypt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from time import gmtime, strftime

app= Flask(__name__)
con = MongoClient("mongodb://abcd:qwerty@ds111798.mlab.com:11798/have_a_seat")
db = con.have_a_seat



#list=[]
#dic={}

#login_manager=LoginManager()
#login_manager.init_app(app)


r1= "This restaurant gives huge discounts at 9:00 pm...Love it!"
r2= "Awesome food, great service ! Book the seats when you find one..because you may not find it later"
r3= "I wish I could find more seats here... :("
r4= "Love the ambience inside !! Worth the money"
r5= "Quick and fast service--just go for it !"
r6= "Service is not good"

u1= "Anthony Stone"
u2= "Norris Wallace"
u3= "Bobby Fischer"
u4= "Samual Hunt"
u5= "Chris Newman"
u6= "Ronald Ross"

review_list=[r1,r2,r3,r4,r5]
user_list=[u1,u2,u3,u4,u5]


def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

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
    reqObj = request.get_json()
    rid=int(reqObj['restaurantId'])
    rObj = db.Restaurants.find_one({"_id": rid})

    #'templateSeats':pizzaHutLayout - pizzaHutLayout
    #'templateSeats':mcDonaldsLayout - mcDonaldsLayout
    #'templateSeats':subwayLayout - subwayLayout
    #'templateSeats':starbucksLayout - starbucksLayout

    s_list = []
    sObj = db.Tables.find({"Restid":rid})

    for seat in sObj:
        s_list.append({'sid':seat["TableNo"], 'status': seat['isAvailable']})

    print s_list
    layout=str(rObj["restName"] +'Layout')

    print layout
    return json.dumps({'id': rid, 'name': rObj["restName"], 'templateSeats': layout,'seats':s_list})



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


# @app.route('/seatBooked', methods=['POST'])
# def SeatBooked():
#     print "hellooooooo"
#     seatSelected= request.get_json()
#     print "hellooooooo"
#     print seatSelected;





@app.route('/restaurants', methods=['POST'])
def restaurants():
    #counter=0
    print  " Hello I am in Restaurents"
    restaurant_searched = request.get_json()


    restname=str(restaurant_searched['search'])

    print restname
    restname=restname.lower().replace(" ", "")

    dic=[]
    counter=0
    listOfRestaurants= db.Restaurants.find({"restName":restname})

    if listOfRestaurants.count()==0:
        listOfRestaurants=db.Restaurants.find({"City": restname})
    
    global user_list
    global review_list

    quotes = []

    for i in listOfRestaurants:
        sObj = db.Tables.find({"Restid": i['_id']})
        for seat in sObj:
            if(seat['isAvailable']==0):
                counter+=1
        quotes.append({"rname": user_list[randint(0, len(user_list) - 1)],
                       "review": review_list[randint(0, len(review_list) - 1)]})

#     for i in range(listOfRestaurants.count()):
#         quotes_dict[user_list[randint(0,len(user_list)-1)]] = review_list[randint(0,len(review_list)-1)]




        dic.append({"quotes": quotes,"Availability":counter, "name":str(i["restName"]), "address":str(i['Street']),"id":i['_id']})
    #dic.append({"name": "Peanuts", "Street":"abc", "City": "nhb", "State":"CA"})
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
        checkIfExist=db.Customers.find_one({'Email':emailid})
        if checkIfExist:
            result= "Email already used"
            return json.dumps({'result':result})
        try:

            hashpass=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            print hashpass
            db.Customers.insert_one({'customerName':firstname+" "+lastName,'Email': emailid, 'Password': hashpass})
            print ("Inserted")
            print "done"
        except pymongo.errors.DuplicateKeyError:
            print "In Except"
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
            #if(password == login_user['Password']):
            if bcrypt.hashpw(password.encode('utf-8'),
                             login_user['Password'].encode('utf-8')) == login_user['Password'].encode('utf-8'):
                print("password found")
                session['Email'] = username
                #return redirect(url_for('checkSeats', restaurant_name="subway"))
                print ("I am here")
                #return ("HII")
                return json.dumps({'templateSeats':'pizzaHutLayout','login_type':'user','email': login_user['Email'], 'name': login_user['customerName']})
            print("password NOT found")
            error = "Invalid Passowrd. Please try again."
           # return json.dumps({'email': username, 'name': login_user['customerName']})
            #return render_template("LogIn.html", error=error)

        elif login_owner:
            print("owner is here")
            print password.encode('utf-8')
          #  if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) ==
           #         login_user['password'].encode('utf-8'):
            #if bcrypt.hashpw(password.encode('utf-8'),
            #                 login_owner['owner_password'].encode('utf-8')) == login_owner['owner_password'].encode('utf-8'):
            #if(password == login_owner['owner_password']):
            if (password == login_owner['owner_password']):
                print "Owner has signed in"
                ownerDetails = db.Owners.find_one({"owner_email": username})
                session['Email'] = username
                restaurantDetails=db.Restaurants.find_one({"_id": ownerDetails['Restid']})
                restaurantName=restaurantDetails['restName']

                return json.dumps({'templateSeats':'pizzaHutLayout','restid':ownerDetails['Restid'], 'login_type':'owner','email': login_owner['owner_email'], 'name': login_owner['owner_name']})
            error = "Invalid Passowrd. Please try again."
                #return redirect(url_for('checkOwnerSeats', restaurant_name=restaurantName))
        else:
            error="Invalid Username"
            print ("Invalid user")
        return json.dumps({'error': error})


@app.route('/isValidAdmin', methods=['POST'])
def isValidAdmin():
    res = request.get_json() #request object is of form {'Restid': 123, 'tables': [{"sid": 1, "status":0},{"sid":2,"status":2}]}
    print res

    return json.dumps({'isValidAdmin':'true'})



@app.route('/seatsBooked', methods=['POST'])
def seatsBooked():
    res = request.get_json() #request object is of form {'Restid': 123, 'tables': [{"sid": 1, "status":0},{"sid":2,"status":2}]}
    restID = int(res['Restid'])
    CustomerBooking = str(res['customerBooking'])
    CustomerName = ""
    CustomerEmail = ""
    CustomerPhone = ""
    if(CustomerBooking == 'Yes'):
        CustomerName = str(res['customerName'])
        CustomerEmail = str(res['customerEmail'])
        CustomerPhone = str(res['customerPhone'])
    print res

    tables = (res['tables'])
    print tables

    session['Tables'] = tables
    counter=0
    slot = 0
    bookedRest = db.Restaurants.find_one({"_id": restID})
    dateTime = strftime("%Y-%m-%d %H:%M:%S")
    date, time = dateTime.split(" ")
    if time[0:time.index(':')] < 13:
        slot = 0
    elif time[0:time.index(':')] < 17:
        slot = 1
    elif time[0:time.index(':')] < 20:
        slot = 2
    else:
        slot = 3
    if(CustomerBooking == 'Yes'):
        db.Bookings.insert({'customerName':CustomerName, 'customerEmail': CustomerEmail, 'customerPhone': CustomerPhone, 'Slot': slot})
    for table in tables:
        print int(table["sid"])
        print "hello----->",int(table["status"])


        db.Tables.update({"Restid": restID, "TableNo": int(table["sid"])},{'$set': {"isAvailable":int(table["status"])}}, upsert=False)
        print "updated", table["sid"]
        counter=counter+1
    if counter>0:
        emailCustomer(counter,bookedRest['restName'], bookedRest['City'])


    dict = {}
    dict['status'] = "success" #just for returning something
    return json.dumps(dict)



@app.route('/seatsBookedAdmin', methods=['POST'])
def seatsBookedAdmin():
    res = request.get_json() #request object is of form {'Restid': 123, 'tables': [{"sid": 1, "status":0},{"sid":2,"status":2}]}
    restID = int(res['Restid'])

    print res

    tables = (res['tables'])
    print tables

    session['Tables'] = tables

    db.Tables.update({"Restid": restID, "TableNo": int(tables["sid"])},{'$set': {"isAvailable":int(tables["status"])}}, upsert=False)
   # print "updated", table["sid"]


    dict = {}
    dict['status'] = "success" #just for returning something
    return json.dumps(dict)




@app.route("/timerout")
def revertseats():
    res = request.get_json() # request object is of form {'restid': 123} ---May or may not give the table numbers
    tables = session['Tables'] # if table ids not given in request object
    for table in tables:
        db.Tables.update({"Restid": restID, "TableNo": table["sid"]}, {'$set': {"isAvailable": 0}},upsert=False)
        print "reverted back", table["sid"]

    dict = {}
    dict['status'] = "success" #just for returning something
    return json.dumps(dict)



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

@app.route('/loggedinUser', methods=['GET'])
def loggedinUser():
    if 'Email' in session:
        currentUserEmail=session['Email']
        login_user = db.Customers.find_one({'Email': currentUserEmail})
        login_owner = db.Owners.find_one({'owner_email': currentUserEmail})

        if login_user:
            return json.dumps({"Role":"Customer", "isValidAdmin":'False', "Email":login_user['Email'], "Name":login_user['customerName']})
        if login_owner:
            ownerDetails = db.Owners.find_one({"owner_email": currentUserEmail})
            restaurantDetails = db.Restaurants.find_one({"_id": ownerDetails['Restid']})
            restaurantName = restaurantDetails['restName']
            return json.dumps({"Role":"Owner", "Restid":ownerDetails['Restid'], "isValidAdmin":'True', "Email":ownerDetails['owner_email'], "Name":ownerDetails["owner_name"]})
    return json.dumps({"error":"no user loggedin"})


@app.route('/tweet')
def tweet():
  # Fill in the values noted in previous step here
  cfg = {
    "consumer_key"        : "TNiA7eKg5UmSKhZd77rHSQ3sJ",
    "consumer_secret"     : "i3aOZi7wQBkg9QRtB8VfhDjAgNuZ1QsxyB8dDFdxtUoFyIqW1f",
    "access_token"        : "803523740172632064-dbuOv0OWdzWZKVowoHkvLF9rjXFwrz1",
    "access_token_secret" : "1ABNMundXyNGinSgTCs6PeVuI2wmJyd9WDgPyneqLwni5"
    }
  res = request.get_json()
  restID = res["restid"]
  restTweet = res["tweetmessage"]
  restObj = db.Restaurants.find_one({'_id':restID})
  api = get_api(cfg)
  tweet = restObj['restName'] + "says: "+restTweet
  status = api.update_status(status=tweet)
  dict = {"status":"success"}
  return json.dumps(dict)

@app.route('/logout', methods=['GET', 'POST'])
#@login_required
def logout():
    if 'Email' in session:
        session.clear()
        #print("you're logged in as:" + session['email'])
        return 'Logged out'
    return "noone is logged in"

def emailCustomer(counter, name, city):
    sender ="haveaseat.team5@gmail.com"
    receiver = "sidanasparsh@gmail.com"
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = "Seats Booked, Happy Dining!"
    print("Please reach the restaurant within the next 15 minutes!")
    body = "You have booked "+str(counter)+" seats(s) at " + " "+ name+", "+ city + ". Please reach the restaurant within the next 15 minutes"
    message.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, "haveaseat")
    server.sendmail(sender, receiver, message.as_string())
    server.quit()

@app.route('/exploration')
def exploration():
    data=request.get_json()
    slot=data['Slot']
    winner=db.Exploration.find_one({"Slot":slot})
    return json.dumps({'Name':winner['CustomerName'], 'Email': winner['CustomerEmail']})


@app.route('/exploitation')
def exploitation():
    data=request.get_json()
    slot=data['Slot']
    winner= db.Exploration.find_one({"Slot":slot})
    return json.dumps({'Name':winner['CustomerName'], 'Email': winner['CustomerEmail']})
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
if __name__ == "__main__":  #main source running
    app.secret_key= 'mysecret'
    app.run(host="0.0.0.0", port=5000, debug=True)


    
