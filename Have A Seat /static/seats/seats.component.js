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
             seatsCtrl.bookedTables = [];
             seatsCtrl.restaurantId = $routeParams.resId;

                $http({
                    method: 'POST',
                    url: '/getSeats',
                    data:{
                          restaurantId:seatsCtrl.restaurantId
                        }
                }).then(function (res) {
                    seatsCtrl.selectedRestaurant = res.data;
                    console.log('$rootScope.showSeats  '+$rootScope.showSeats);
                 seatsCtrl[seatsCtrl.selectedRestaurant.templateSeats] = false;
                });

             seatsCtrl.pizzaHutLayout =true;
             seatsCtrl.subwayLayout =true;
             seatsCtrl.starbucksLayout =true;
             seatsCtrl.mcDonaldsLayout =true;

                this.setTemplateSeatView = function(templateName){
                     seatsCtrl.pizzaHutLayout =true;
                     seatsCtrl.subwayLayout =true;
                     seatsCtrl.starbucksLayout =true;
                     seatsCtrl.mcDonaldsLayout =true;
                     seatsCtrl[templateName] = false;
                }

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
             }


            this.changeToEmpty = function(dynamic){
               $scope.model[dynamic] = "btn btn-default";
            }

            $scope.changeToGreen = function(dynamic){
                $scope.model[dynamic] = "btn btn-warning";
            }

            this.addTableToList =function(table){
               seatsCtrl.bookedTables.push(table);
            }

            this.updateStatus = function(table,dynamic,tableIndex){
                console.log(table);
                var tabObj = {selectedTable:table,dynamicTab:dynamic};
                seatsCtrl.addTableToList(tabObj);
                //will be changing based on logic
                if(table.status==='avail'){
                 $scope.changeToGreen(dynamic);
                }
            }

            this.unBook= function(table){

                function filterTables(el) {
                       if(el.selectedTable.sid === table.selectedTable.sid){
                            console.log(el);
                            seatsCtrl.changeToEmpty(table.dynamicTab);
                       }
                      return el.selectedTable.sid !== table.selectedTable.sid ;
                   }

                   var filteredTables = seatsCtrl.bookedTables.filter(filterTables);
                   seatsCtrl.bookedTables = filteredTables;
                }
            //}
    }]
});