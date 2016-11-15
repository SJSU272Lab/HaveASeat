angular.module('header')
.component('header', {
	templateUrl: 'static/header/header.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
        '$rootScope',
        '$anchorScroll',
		function ($http, $scope, $location, $rootScope, $anchorScroll) {
			var headerCtrl = this;

			this.searchRestaurants = function() {
                $scope.search;

                $http({
                    method: 'POST',
                    url: '/restaurants',
                    data:{
                        search:$scope.search
                    }
                }).then(function (res) {
                    //resCtrl.restaurants = res;
                    $rootScope.restaurants = res.data;
                    $anchorScroll('restaurantlist');
                });
            }
		}]
});