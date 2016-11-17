angular.module('restaurants')
.component('restaurants', {
	templateUrl: 'static/restaurants/restaurants.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		'$routeParams',
        "$rootScope",
        '$anchorScroll',
		function ($http, $scope, $location,$routeParams, $rootScope, $anchorScroll) {
                var restaurantsCtrl = this;
                restaurantsCtrl.search = $routeParams.search;

                $http({
                    method: 'POST',
                    url: '/restaurants',
                    data:{
                        search: restaurantsCtrl.search
                    }
                }).then(function (res) {
                    restaurantsCtrl.restaurants = res.data;
                });

                this.view = function(restaurant){
                console.log(restaurant);
                var seatsUrl = '/seats/'+restaurant.id;
                $location.path(seatsUrl);
            }
		}]
});