angular.module('restaurants')
.component('restaurants', {
	templateUrl: 'static/restaurants/restaurants.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		'$routeParams',
		function ($http, $scope, $location,$routeParams) {
             var restaurantsCtrl = this;

            $http({
            method: 'POST',
            url: '/searchRestaurants',
            data:{
                search:$routeParams.search
            }
          }).then(function (res) {
            restaurantsCtrl.filteredRestaurants = res.data;
          });

          this.view = function(res){
             $location.path('/seats/'+res.id);
          }

		}]
});