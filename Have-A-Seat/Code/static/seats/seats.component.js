angular.module('seats')
.component('seats', {
	templateUrl: 'static/seats/seats.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		'$routeParams',
		function ($http, $scope, $location,$routeParams) {

             var indexCtrl = this;

             indexCtrl.restaurantId = $routeParams.resId;
		}]
});