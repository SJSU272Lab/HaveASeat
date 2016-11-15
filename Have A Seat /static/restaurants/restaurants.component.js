angular.module('restaurants')
.component('restaurants', {
	templateUrl: 'static/restaurants/restaurants.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		'$routeParams',
        "$rootScope",
		function ($http, $scope, $location,$routeParams, $rootScope) {
             var restaurantsCtrl = this;

                $rootScope.restaurants;

		}]
});