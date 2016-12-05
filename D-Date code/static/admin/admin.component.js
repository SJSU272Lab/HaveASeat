angular.module('admin')
.component('admin', {
	templateUrl: 'static/admin/admin.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		'$routeParams',
        "$rootScope",
        '$anchorScroll',
		function ($http, $scope, $location,$routeParams, $rootScope, $anchorScroll) {

             var seatsCtrl = this;
             var seatsCtrl = this;
             $scope.bookedTables = [];
             $scope.bookedTableIDs = [];
             $scope.restaurantId = $routeParams.resId;
             $scope.layout = {};
             $scope.layout.pizzahutLayout =true;
             $scope.layout.subwayLayout =true;
             $scope.layout.peanutsLayout =true;
             $scope.layout.mcDonaldsLayout =true;

             $scope.tweet='';

              $http({
                    method: 'GET',
                    url: '/loggedinUser',
                }).then(function (res) {
                    console.log(res);
                    if(res.data.error){
                    $location.path('/');
                    }

                });

            this.searchRestaurants = function() {
                $scope.search;
                var restaurantsSearchUrl ='/restaurants/' + $scope.search;
                $location.path(restaurantsSearchUrl);
            }

            $scope.logout = function(){
			     $http({
                    method: 'GET',
                    url: '/logout',
                }).then(function (res) {
                    console.log(res);
                    console.log('Loggin out from admin');

                    $location.path('/');
                    });
			}


             $http({
                    method: 'GET',
                    url: '/loggedinUser',
                }).then(function (res) {

                      console.log(res.data.isValidAdmin);
                    console.log('isPOsrpto ',res.data.Restid+"" === $scope.restaurantId);

                        $scope.userName = res.data.Name;


                    if( (res.data.isValidAdmin==='True') && (res.data.Restid+"" === $scope.restaurantId)){
                         $http({
                        method: 'POST',
                        url: '/getSeats',
                        data:{
                              restaurantId:$scope.restaurantId
                            }
                    }).then(function (res) {

                             $rootScope.hideHeader=true
                             $rootScope.hideSearch=true
                             $rootScope.logout=true

                            $scope.selectedRestaurant = res.data;
                            console.log('$rootScope.showSeats  '+$rootScope.showSeats);

                            $scope.layout[$scope.selectedRestaurant.templateSeats] = false;
                            var seats = $scope.selectedRestaurant.seats;

                            var seatsLayout=[];

                       if($scope.selectedRestaurant.name==='pizzahut')
                       {
                                  seatsLayout = [0,3,5,7,8,10,11];
                       }
                       else if($scope.selectedRestaurant.name==='peanuts')
                       {
                                 seatsLayout = [1,2,4,5,6,7,8,9,10,11];
                       }
                       else if($scope.selectedRestaurant.name==='subway')
                       {
                              seatsLayout = [1,4,5,6,8,9,10,11,13];
                       }

                           var index=0;

                        seats.forEach(function (seat) {

                            var d = "dynamic";
                            if(seat.status===2){
                            d += seatsLayout[index];
                            $scope.model[d] = "btn btn-danger";
                            $scope.modelAvailForSelect[d]=true;
                           }
                           else if(seat.status===1){
                            d += seatsLayout[index];
                            $scope.model[d] = "btn btn-warning";
                            $scope.modelAvailForSelect[d]=true;
                           }
                            index++;
                        });

                    seatsCtrl.setTemplateSeatView(res.data.templateSeats);
                });
                    }


                else{
                    $rootScope.loginDetails = null;
                    $rootScope.hideAdminHeader = true;
                    $rootScope.hideHeader = true;
                    $rootScope.hideWelcomeHeader = true;
                    $rootScope.loggedIn = false;
                    $location.path('/');
                }


                });





            /* $scope.sendTweet = function(){
                console.log('can u see tweet '+$scope.tweet);

                    //sendTweet

                    $http({
                        method: 'POST',
                        url: '/sendTweet',
                        data:{
                            adminTweet:$scope.tweet
                        }
                    }).then(function (res) {
                        console.log('tweet send succesfully');
                        $scope.tweet='';
                    });

                 }*/
		$scope.sendTweet = function(){
                console.log('can u see tweet '+$scope.tweet);

                    //sendTweet

                    $http({
                        method: 'POST',
                        url: '/tweet',
                        data:{
                            //adminTweet:$scope.tweet
                            restid:$scope.restaurantId,
                            tweetmessage:$scope.tweet
                        }

                    }).then(function (res) {
                        console.log('tweet send succesfully');
                        $scope.tweet='';
                    });

                 }

                $scope.status = 'avail';
//                $scope.availTables = 0;
//                $scope.bookTables = 0;
//                $scope.dineTables = 0;

                $scope.model = {
                    dynamic0 : "btn btn-default",
                    dynamic1 : "btn btn-default",
                    dynamic2 : "btn btn-default",
                    dynamic3 : "btn btn-default",
                    dynamic4 : "btn btn-default",
                    dynamic5 : "btn btn-default",
                    dynamic6 : "btn btn-default",
                    dynamic7 : "btn btn-default",
                    dynamic8 : "btn btn-default",
                    dynamic9 : "btn btn-default",
                    dynamic10 : "btn btn-default",
                    dynamic11 : "btn btn-default",
                    dynamic12 : "btn btn-default",
                    dynamic13 : "btn btn-default",
                    dynamic14 : "btn btn-default",
                    dynamic15 : "btn btn-default"
             };


            $scope.modelAvailForSelect = {
                    dynamic0 : false,
                    dynamic1 : false,
                    dynamic2 : false,
                    dynamic3 : false,
                    dynamic4 : false,
                    dynamic5 : false,
                    dynamic6 : false,
                    dynamic7 : false,
                    dynamic8 : false,
                    dynamic9 : false,
                    dynamic10 : false,
                    dynamic11 : false,
                    dynamic12 : false,
                    dynamic13 : false,
                    dynamic14 : false,
                    dynamic15 : false
             };





            this.setTemplateSeatView = function(templateName){
                     $scope.pizzahutLayout =true;
                     $scope.subwayLayout =true;
                     $scope.peanutsLayout =true;
                     $scope.mcDonaldsLayout =true;
                     $scope[templateName] = false;
                }


            $scope.sendChangeCommand = function(table, status){
                    $http({
                    method: 'POST',
                    url: '/seatsBookedAdmin',
                    data: {Restid: $scope.restaurantId,tables:{sid:table.sid, status : status}}
                    // data: {
                    //       tableId:table.sid,
                    //       changeTo : status
                    //     }
                }).then(function (res) {
                        console.log('Changed the status from server');
                });
            }


            $scope.changeToEmpty = function(dynamic,table){
               $scope.model[dynamic] = "btn btn-default";
               console.log('at avail table',table);
               $scope.sendChangeCommand(table,0);
            };

            /*$scope.changeToGreen = function(dynamic,table){
                $scope.model[dynamic] = "btn btn-success";
            };*/

             $scope.changeToOrange= function(dynamic,table){
                $scope.model[dynamic] = "btn btn-warning";
                console.log('at booked table',table);
                $scope.sendChangeCommand(table,1);
            };

             $scope.changeToRed= function(dynamic,table){
                $scope.model[dynamic] = "btn btn-danger";
                console.log('at dine table',table);
                $scope.sendChangeCommand(table,2);
            };

            $scope.addTableToList =function(table){
                    // if not already added then add
                if ($scope.bookedTableIDs.indexOf(table.selectedTable.sid) === -1) {
                    $scope.bookedTableIDs.push(table.selectedTable.sid);
                    $scope.bookedTables.push(table);
                }
            }

            $scope.updateStatus = function(table,dynamic,tableIndex){
               $scope.selectedTable = table;
               $scope.selectedDynamic = dynamic;

//               console.log('you have selected this one ', table);
//
//               if(table.status==="available"){
//                 $scope.changeToGreen(dynamic);
////                 $scope.addTableToList(tabObj);
//                }

            }

            $scope.unBook= function(table){
                function filterTables(el) {
                       if(el.selectedTable.sid === table.selectedTable.sid){
                            console.log(el);
                            $scope.changeToEmpty(table.dynamicTab);
                       }
                      return el.selectedTable.sid !== table.selectedTable.sid ;
                   }

                   var filteredTables = $scope.bookedTables.filter(filterTables);
                   $scope.bookedTables = filteredTables;
                   var bookedTableIndex = $scope.bookedTableIDs.indexOf(table.selectedTable.sid);
                   if(bookedTableIndex !== -1){
                        $scope.bookedTableIDs.splice(bookedTableIndex, 1);
                   }
            }

           $scope.checkOut= function(){
           var seatsBooked  = $scope.bookedTables.length;

            alert("ThankYou for booking "+ seatsBooked  +" tables with Have A Seat");
            $location.path("/");
           }

           $scope.adminChange = function(){
            console.log('adminChnage.......');
            console.log('sattus '+$scope.status);
            console.log('seletect table ' +$scope.selectedTable);
            $scope.changeStatusOfTable();
           }

            $scope.changeStatusOfTable = function(){
                console.log('sattus '+$scope.status);
                 console.log('seletect table ' +$scope.selectedTable);
                 console.log('seletect dynamic ' +$scope.selectedDynamic);

                //will be changing based on logic
                if($scope.status==="0"){
                    console.log('Changing staus to GREEEN ');
                     $scope.changeToEmpty($scope.selectedDynamic,$scope.selectedTable);
                }

                if($scope.status==="1"){
                    console.log('Changing staus to ORbage');
                     $scope.changeToOrange($scope.selectedDynamic,$scope.selectedTable);
                }

                if($scope.status==="2"){
                    console.log('Changing staus to REDDDD');
                     $scope.changeToRed($scope.selectedDynamic,$scope.selectedTable);
                }

                $scope.status = '0';
            }

             $scope.exploration = function(){

            var timeSelected;
                 var slotCode;

                 if($scope.time==="0")
                 {
                     timeSelected="10:00 am - 1:00 pm";
                      slotCode=0;
                 }
                 if($scope.time==="1")
                 {
                     timeSelected="1:00pm - 4:00 pm";
                      slotCode=1;
                 }
                 if($scope.time==="2")
                 {
                        timeSelected="4:00pm - 7:00 pm";
                      slotCode=2;
                 }
                 if($scope.time==="3")
                 {
                       timeSelected="7:00pm - 10:00 pm";
                      slotCode=3;
                 }

                           console.log(timeSelected);

			     $http({
                    method: 'POST',
                    url: '/exploration',
                     data: {Slot: slotCode, timeSlot:timeSelected  }
                }).then(function (res)
                 {
                     console.log(res.data)     ;
                     $scope.name=  res.data['Name']  ;
                     $scope.email   =  res.data['Email']  ;
                     $scope.offerPhone= res.data['PhoneNumber']




                  //  $location.path('/');
                 });
			}

			 $scope.exploitation = function(){

                  var timeSelected;
                 var slotCode;

                       if($scope.time==="0")
                       {
                           timeSelected="10:00 am - 1:00 pm";
                           slotCode=0;

                       }
                       if($scope.time==="1")
                       {
                           timeSelected="1:00pm - 4:00 pm";
                           slotCode=1;
                       }
                       if($scope.time==="2")
                       {
                              timeSelected="4:00pm - 7:00 pm";
                           slotCode=2;
                       }
                       if($scope.time==="3")
                       {
                             timeSelected="7:00pm - 10:00 pm";
                           slotCode=3;
                       }

                                 console.log(timeSelected);


			     $http({
                    method: 'POST',
                    url: '/exploitation',
                     data:{Slot: slotCode, timeSlot:timeSelected  }
                }).then(function (res)
                 {
                        $scope.name1=  res.data['Name']  ;
                        $scope.email1   =  res.data['Email']  ;
                       $scope.offerPhone= res.data['PhoneNumber']

                 //   $location.path('/');
                 });
			}


			$scope.sendOffer=function () {

                var phoneNumber= $scope.offerPhone;
                console.log(phoneNumber)   ;

                $http({


                    method: 'POST',
                    url: '/sendOffer',
                    data: {phoneNumber: phoneNumber}

                }).then(function (res) {

                });
            }

            $scope.getAnalysis=function () {

                var restId=$scope.restaurantId;
                console.log(restId)   ;

                $http({


                    method: 'POST',
                    url: '/getReviewAnalysis',
                    data: {Restaurant: restId}

                }).then(function (res) {

                           $scope.positive=  res.data['positive']  ;
                           $scope.negative=  res.data['negative']  ;
                             htmlHelper($scope.positive);

                                            console.log($scope.positive) ;
                            console.log($scope.negative) ;




                });



            }

           $scope.sendmail= function ()
           {
                var email = $scope.emailHaveASeat;
               console.log(email);

                $http({
                    method: 'POST',
                    url: '/emailHaveASeat',
                    data: {restid: $scope.restaurantId, emailmessage: email}
                }).then(function (res) {

                    $scope.success = "your email has been successfully placed."

                });

            }


    }]
});
