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
                });

             seatsCtrl.pizzaHutLayout =true;
             seatsCtrl.subwayLayout =true;
             seatsCtrl.starbucksLayout =true;
             seatsCtrl.mcDonaldsLayout =true;
             //seatsCtrl[seatsCtrl.selectedRestaurant.templateSeats] = false;

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


            $scope.changeToRed = function(){
                $scope.model.dynamic = "red";
            }

            $scope.changeToGreen = function(dynamic){
                $scope.model[dynamic] = "btn btn-warning";
            }

            this.updateStatus = function(table,dynamic){
                console.log(table);
                //will be changing based on logic
                if(table.status==='avail'){
                 $scope.changeToGreen(dynamic);
                }
            }
    }]
});