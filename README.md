![alt text](https://github.com/SJSU272Lab/Fall16-Team5/blob/master/Have%20A%20Seat%20/static/sjsu.PNG)

#                             **CMPE 272 - Class Project**

#				TITLE: _HAVE A SEAT_

###                                Link [Here](http://haveaseat.mybluemix.net)
					            
##Problem Statement:
How many times has it occurred that you went to a diner and couldn’t find a seat? You probably ended up spending time in long queues, ruining your dining experience and getting frustrated – not knowing that there is a diner with available seats on the next street or there was a seat available just a few minutes ago when you stopped just for a small chat.
Moreover, restaurant owners lose revenue (as well as food!) when a customer enters the diner right after the owner closed the cash counter machine. So, there is a need to develop a platform on which the consumers and the restaurant owners can communicate real-time. 

##Target Audience:
###@Consumers: 
Foodies who wish to eat at a diner in a specific location without making prior reservations.

###@Owners: 
Restaurant owner who doesn’t want to waste food and have seats in their restaurant when nearby restaurant is full.

##Proposed Solution:
###@Consumers: 
Foodies can now look up in the app and see if there is a seat available at the location where they want to eat. They can submit the request to book the seat, and the app will give them a time-limit to reach to the restaurant. If they reach the restaurant in the specified time, the owner can check-in them and mark their seat as booked. As soon as the owner marks the seat as booked, it will be reflected across all the apps in real time.

##User Architectural Flow Diagram
![alt text](https://github.com/SJSU272Lab/Fall16-Team5/blob/master/Have%20A%20Seat%20/static/User%20Persona.png "User Flow Diagram")


###@Owners: 
Owners will get a notification via ML algorithm one-hour prior to closing time to send tweets/messages to the foodies based on the historical data accumulated by the app. Owner can then decide whether to call it a day & go home or to send the tweets to the foodie popped-out by the ML algorithm. Owners also get to disapprove the request for booking in case a favorite customer comes in before the ones who booked the seat via the app.

###Owner Architectural Flow Diagram
![alt text](https://github.com/SJSU272Lab/Fall16-Team5/blob/master/Have%20A%20Seat%20/static/owner%20persona.PNG "Owner Flow Diagram")

## Step-by-Step Explanation

###Welcome Page for Customer and Owner
This is the default landing page when a user (either customer/owner) enters the website. This page contains the basic introduction to the concept of “Have A Seat” as well as provides the links to facebook page of Have A Seat, contact information form at the end. User input fields are protected from XSS attacks and SQL Injection.
![alt text](https://github.com/SJSU272Lab/Fall16-Team5/blob/master/Have%20A%20Seat%20/static/Ss1.PNG)

###Search page  with search results and the “available seats“ on the restaurants
This page gives the live status of seats availability when user searches based on location and/or restaurant name. User input is filtered in the search box so that the search works even if the user enters keywords without spaces, in different cases (upper/lower) etc. Customer need not login to view the live seat availability.
![alt text](https://github.com/SJSU272Lab/Fall16-Team5/blob/master/Have%20A%20Seat%20/static/ss2.PNG)

###Seats view of restaurant for customer persona :
Customer can select the available/white seat(s) from the seat layout. User is given a ticker to contact the Have A Seat development team in case he/she has any concerns. Customer can also send reviews regarding the restaurant on this page. The user reviews are fed to a sentimental analysis using NLTK (Natural Language ToolKit) library available in Python-Flask framework. This analysis gives the insights in graphical format to the restaurant owner on his/her dashboard. Customer can only book seats after logging in but can view available seats without login.
![alt text](https://github.com/SJSU272Lab/Fall16-Team5/blob/master/Have%20A%20Seat%20/static/ss3.PNG)

##Future Scope:
Wider ML integration to suggest appropriate restaurants to the foodies based on their eating habits, and to suggest owners what food to prepare and how much in case a customer has booked a seat. With much data (real and accurate), we can scale the app to release APIs which can be used to develop other apps (or can also expand this app) and give recommendations of available seat based on time/season to the users.

##Benefits:
•  Increased revenue of the restaurant owners by allowing them to contact prospective customers thereby allowing them to fill up the seats at the last moment. 
Improve the opportunity costs for the restaurant owners when they have seats available.
Enables the owners to do targeted marketing and gain automated insights from the user reviews in graphical format.
Owners can reach out the customers which were previously out-of-scope by using Have A Seat Database.
 • Lots and lots of happiness to the Foodies!



##Overall Architectural Flow Diagram:

![artitecture flow diagram](https://cloud.githubusercontent.com/assets/21698271/19756814/120493d0-9bd4-11e6-9e3a-f96cbe620a41.png)

![machine learning 272](https://cloud.githubusercontent.com/assets/21698271/19756815/12053038-9bd4-11e6-8983-8a803a967978.png)

