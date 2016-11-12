angular.module('header')
.component('header', {
	templateUrl: 'static/header/header.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		function ($http, $scope, $location) {
			var headerCtrl = this;

			this.searchRestaurants = function(){
            $scope.search;

            $location.path('restaurants/'+$scope.search);
           }
		}]
});