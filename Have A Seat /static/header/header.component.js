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
				console.log('roooot'+$rootScope.hideSearch);


			this.searchRestaurants = function() {
                $scope.search;
                var restaurantsSearchUrl ='/restaurants/' + $scope.search;
                $location.path(restaurantsSearchUrl);
            }

            $scope.logout = function(){
			    console.log('Loggin out from user');
			    //should send logging out request to server here
                $location.path('/logout');
			}
		}]
});