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
             $scope.bookedTables = [];
             $scope.bookedTableIDs = [];
             $scope.restaurantId = $routeParams.resId;

             $scope.pizzaHutLayout =true;
             $scope.subwayLayout =true;
             $scope.starbucksLayout =true;
             $scope.mcDonaldsLayout =true;

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
                        $scope[$scope.selectedRestaurant.templateSeats] = false;
                        var seats = $scope.selectedRestaurant.seats;
                        var index = 0;
                        seats.forEach(function (seat) {
                            var d = "dynamic";
                            if(seat.status==="unavailable"){
                            d += index;
                            $scope.model[d] = "btn btn-danger";
                            $scope.modelAvailForSelect[d]=true;
                           }
                           else if(seat.status==="booked"){
                            d += index;
                            $scope.model[d] = "btn btn-warning";
                            $scope.modelAvailForSelect[d]=true;
                           }
                            index++;
                        });
                });


                this.setTemplateSeatView = function(templateName){
                     $scope.pizzaHutLayout =true;
                     $scope.subwayLayout =true;
                     $scope.starbucksLayout =true;
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
                if ($scope.bookedTableIDs.indexOf(table.selectedTable.sid) === -1) {
                    $scope.bookedTableIDs.push(table.selectedTable.sid);
                    $scope.bookedTables.push(table);
                }
            }

            $scope.updateStatus = function(table,dynamic,tableIndex){
//                console.log(table);
                var tabObj = {selectedTable:table,dynamicTab:dynamic};

                //will be changing based on logic
                if(table.status==="available"){
                 $scope.changeToGreen(dynamic);
                 $scope.addTableToList(tabObj);
                }
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
            }

           $scope.checkOut= function(){
           var seatsBooked  = $scope.bookedTables.length;

            alert("ThankYou for booking "+ seatsBooked  +" tables with Have A Seat");
            $location.path("/");
           }
    }]
});