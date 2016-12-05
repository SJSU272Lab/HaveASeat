from pymongo import MongoClient
import schedule
import time

##############
## This script will be deployed in bluemix with --no-route set to true

##############
con = MongoClient("mongodb://abcd:qwerty@ds111798.mlab.com:11798/have_a_seat")
db = con.have_a_seat

cursor = db.Bookings.find()

#Bookings is {customerName:"", customerEmail: "", customerPhone: "", Slot: ""}

dict = {}

db.Exploration.delete_many({})
db.Exploitation.delete_many({})
for i in range(4):  # Finding for all slots
    for c in cursor:
        if c['Slot'] == i and c['customerEmail'] not in dict.keys():
            dict[c['customerEmail']] = 1

        elif c['Slot'] == i and c['customerEmail'] in dict.keys():
            dict[c['customerEmail']] += 1

    tuples_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)

    print tuples_list

    print 'Completed for slot ', i

    db.Exploitation.insert({'Slot': i, 'customerEmail': tuples_list[0][0],
                            'customerName': db.Bookings.find_one({'customerEmail': tuples_list[0][0]})['customerName']})
    db.Exploration.insert({'Slot': i, 'customerEmail': tuples_list[len(tuples_list) - 1][0], 'customerName':
        db.Bookings.find_one({'customerEmail': tuples_list[len(tuples_list) - 1][0]})['customerName']})
