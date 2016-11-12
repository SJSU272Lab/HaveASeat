angular.module('seats')
.component('seats', {
	templateUrl: 'static/seats/seats.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		'$routeParams',
		function ($http, $scope, $location,$routeParams) {

             var seatCtrl = this;

             seatCtrl.restaurantId = $routeParams.resId;
		}]
});