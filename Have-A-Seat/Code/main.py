from pymongo import MongoClient
import flask
from flask import Flask, jsonify
from flask import request
from flask import render_template

con=MongoClient()
db=con.customers
employee=db.employee
Restaurant=db.Restaurant

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



"""@app.route('/<string:restaurant_name>')
def getSeat(restaurant_name):
    check= Restaurant.find_one({"name": restaurant_name})
   # return  str(check['seat'])
"""
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8082)




