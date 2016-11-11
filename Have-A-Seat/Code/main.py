from pymongo import MongoClient
import flask
from flask import Flask,url_for , redirect, session ,flash
from flask import request
from flask import render_template
from flask_oauth import OAuth

app= Flask(__name__)
con = MongoClient()
db = con.Have_A_Seat


list=[]
dic={}

# this is the home page which loads first
@app.route('/', methods=['GET', 'POST'])
def Homepage():
    if (request.method == "POST"):
        restaurant_searched = request.form['search']
        print restaurant_searched
        restaurantList = db.Restaurants.find({"restName":restaurant_searched})
        for restaurant in restaurantList:
            list = str(restaurant['restName'])
            link = "/" + restaurant_searched + "/checkSeats"
            global dic
            dic = {"Restaurant": [[list, link]]}

        #print dic
        return redirect(url_for('restaurantList'))

    return  render_template("index.html")


# when user searches for restaurent this page gets loaded
@app.route('/restaurantList/')
def restaurantList():
   # restaurantList = Restaurants.find({"restName": restaurant_seached})
   # for restaurant in restaurantList:
       # list= str(restaurant['restName'])
       # link="/" + restaurant_seached + "/checkSeats"
       # dic={"Restaurant" : [[list, link]]}
    global dic
    #print dic
    return render_template("restaurantList.html", dic = dic)

"""
@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')"""


@app.route('/<string:restaurant_name>/checkSeats')
def checkSeats(restaurant_name):
    """user reaches here after selecting the restaurant name
    """
    #totalRestaurants = mongo.db.Restaurants

    #rest_cursor = mongo.db.Restaurants.find({"restName": "subway"})

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

    #tup = tuple(tup)
    #print tup
    #total_counter = 0
    #Customer_booked_counter =0
    #Available_counter =0
    #Owner_booked_counter =0
    #availableTableNo = []
    #CustomerbookedTableNo = []
    #OwnerBookedTableNo = []


    #for i in totaltables:
    #    if(i["isAvailable"]==0):
    #        #Available_counter +=1
    #        #availableTableNo.append(i["TableNo"])
    #   elif(i["isAvailable"]==1):
    #        Customer_booked_counter +=1
    #    elif (i["isAvailable"] == 2):
    #        Owner_booked_counter += 1
    #    total_counter +=1

    """seat_details= "This Restaurant has "+ str(total_counter) + " seats of which "\
           + str(Available_counter)+"  Available , " \
           + str(Customer_booked_counter) + "  customer booked , " \
           + str(Owner_booked_counter) + " owner booked ."
    """
    #return 'Hello'
    return render_template("restaurant.html", seat_details=tup, restaurant_name=restaurant_name)

@app.route('/seatBooked', methods = ['GET','POST'])
def success():
    if (request.method == "POST"):
        table_updated = request.form['seatId']
        print table_updated
    return table_updated

# this is the authenticate route
@app.route('/register', methods=['GET','POST'])
def Register():
    # print 'u have readched login'
    # print request.form.get('email')
    # print request.form.get('password')
    return render_template('register.html'), 200

@app.route('/registerUser', methods=['POST'])
def registerUser():
    print 'u have readched regitserter user'
    print request.form.get('email')
    print request.form.get('password')
    email = request.form.get('email')
    password = request.form.get('password')

    # restID = db.Users.insert_one({'email':email,'password':password})
    restID = db.Users.update_one({'email':email},{'$set':{'password':password}},upsert=True)
    print restID
    print 'inserted'
    return render_template("index.html")

@app.route('/login', methods=['GET','POST'])
def Login():
    if request.method=='GET':
        return render_template("login.html")
    if request.method == 'POST':
        print("In Post")
        login_user = Customers.find_one({'username' : request.form['username']})
        if login_user:
            print("FOUNDDD")
            print login_user['password']

            if(request.form['password']==login_user['password']):
                return("logged in")
            return("Invalid Password")

         #   if bcrypt.hashpw(request.form['passwrd'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
         #       session['username']==request.form['username']
         #       return redirect(url_for('Restaurants'))
            #print("Invalid Password")

    return ("invalid username")
        #db.Customers.find({'userame':username})

   # restaurantList = Restaurants.find({"restName": restaurant_seached})
   # for restaurant in restaurantList:
       # list= str(restaurant['restName'])
       # link="/" + restaurant_seached + "/checkSeats"
       # dic={"Restaurant" : [[list, link]]}
    #return render_template("Login.html", dic = dic)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8082)
