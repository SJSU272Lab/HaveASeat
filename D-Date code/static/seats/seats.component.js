angular.module('seats')
.component('seats', {
	templateUrl: 'static/seats/seats.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		'$routeParams',
        "$rootScope",
        '$anchorScroll',
		function ($http, $scope, $location,$routeParams, $rootScope, $anchorScroll) {

             var seatsCtrl = this;

            $scope.showUser = false;
            $scope.showLogout = true;


               $http({
                    method: 'GET',
                    url: '/loggedinUser',
                }).then(function (res) {
                    if(res.data.Name){
                        $scope.userName = res.data.Name;
                        $scope.showUser = true
                        $scope.showLogout = false;
                    }
                });

//            $http({
//                    method: 'GET',
//                    url: '/loggedinUser',
//                }).then(function (res) {
//                    console.log(res);
//                    if(res.data.Name){
//                       $scope.userName = res.data.Name;
//                        $scope.showUser = true
//                        $scope.showLogout = false;
//                    }
//                });


                $scope.logoutZZ = function(){
                console.log('someeee');
                 $http({
                    method: 'GET',
                    url: '/logout',
                }).then(function (res) {
                    console.log(res);
                    console.log('Loggin out from admin');
                    console.log('root',$rootScope);
                    $rootScope.loginDetails = null;
                    $rootScope.hideAdminHeader = true;
                    $rootScope.hideHeader = true;
                    $rootScope.hideWelcomeHeader = true;
                    $rootScope.loggedIn = false;
                    $location.path('/');
                    });
                    }





            this.searchRestaurants = function() {
                $scope.search;
                var restaurantsSearchUrl ='/restaurants/' + $scope.search;
                $location.path(restaurantsSearchUrl);
            }

             if(($rootScope.loginDetails !== undefined) && ($rootScope.loginDetails !== null) ){
                $scope.hideLoginSignup = true;
                $scope.showLogout= false;

            }


            $scope.logout = function(){
			    console.log('Loggin out from admin');
			    console.log('root',$rootScope);
			    $rootScope.loginDetails = null;
			    $rootScope.hideAdminHeader = true;
			    $rootScope.hideHeader = true;
			    $rootScope.hideWelcomeHeader = true;
			    $rootScope.loggedIn = false;
                $location.path('/');
			}
             $scope.bookedTables = [];
             $scope.bookedTableIDs = [];
             $scope.restaurantId = $routeParams.resId;
             $scope.layout = {};

             $scope.layout.pizzahutLayout =true;
             $scope.layout.subwayLayout =true;
             $scope.layout.peanutsLayout =true;
             $scope.layout.mcDonaldsLayout =true;

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

                $http({
                    method: 'POST',
                    url: '/getSeats',
                    data:{
                          restaurantId:$scope.restaurantId
                        }
                }).then(function (res) {
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


                this.setTemplateSeatView = function(templateName){
                     $scope.pizzahutLayout =true;
                     $scope.subwayLayout =true;
                     $scope.peanutsLayout =true;
                     $scope.mcDonaldsLayout =true;
                     $scope[templateName] = false;
                }



            $scope.changeToEmpty = function(dynamic){
               $scope.model[dynamic] = "btn btn-default";
            };

            $scope.changeToGreen = function(dynamic){
                $scope.model[dynamic] = "btn btn-success";
            };

            $scope.addTableToList =function(table){
                    // if not already added then add
                if ($scope.bookedTableIDs.indexOf(table.selectedTable.sid) === -1)
                {
                    $scope.bookedTableIDs.push(table.selectedTable.sid);
                    table.selectedTable.status =1;
                    $scope.bookedTables.push(table);
                }
            }

            $scope.updateStatus = function(table,dynamic,tableIndex){
//                console.log(table);
                var tabObj = {selectedTable:table,dynamicTab:dynamic};

                //will be changing based on logic
                if(table.status===0){
                 $scope.changeToGreen(dynamic);
                 $scope.addTableToList(tabObj);
                }
            }

            $scope.sendReview= function ()
           {
                var review = $scope.customerReview;
               var restid=$scope.restaurantId
               console.log(review);

                $http({
                    method: 'POST',
                    url: '/setReview',
                    data: {Review: review, restID: restid}
                }).then(function (res) {

                    $scope.successReview = res.data['Message'];

                });

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
                   console.log($scope.bookedTables);
                   $scope.bookedTables = filteredTables;

                   var bookedTableIndex = $scope.bookedTableIDs.indexOf(table.selectedTable.sid);

                   if(bookedTableIndex !== -1){
                        $scope.bookedTableIDs.splice(bookedTableIndex, 1);
                        table.selectedTable.status = 0;
                   }
            }

           $scope.checkOut= function(restid){
           var seatsBooked  =$scope.bookedTables.length;
           if(seatsBooked  <1){
           alert('No Seats available / selected to book ');
            return;
           }
           $rootScope.loginDetails;
           if($rootScope.loginDetails===undefined
           || $rootScope.loginDetails === null
           || $rootScope.loginDetails=== "null")
           {
            console.log('login details not logged in ',$rootScope.loginDetails);
            alert("Please Login to book table.");
            $location.path('/login');
           }





            else{
                var onlyTables = [];

                    $scope.bookedTables.forEach(function (el) {
                    onlyTables.push(el.selectedTable);
                });

                $scope.seatsBookeddetails  = {Restid:restid,tables:onlyTables};

                $http({
                    method: 'POST',
                    url: '/seatsBooked',
                    data: $scope.seatsBookeddetails

                }).then(function (res) {
                    console.log(res);
                    alert("ThankYou for booking "+ seatsBooked  +" tables with Have A Seat");
                    $location.path("/logout");
                });
            }

           }
    }]
});
