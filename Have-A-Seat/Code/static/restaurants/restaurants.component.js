angular.module('restaurants')
.component('restaurants', {
	templateUrl: 'static/restaurants/restaurants.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		function ($http, $scope, $location) {
             var restaurantsCtrl = this;

            $http({
            method: 'GET',
            url: '/restaurants',

          }).then(function (res) {
            restaurantsCtrl.filteredRestaurants = res.data;
          });

          this.view = function(res){
             $location.path('/seats/123');
          }

		}]
});