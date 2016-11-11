angular.module('header')
.component('header', {
	templateUrl: 'static/header/header.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		function ($http, $scope, $location) {
			var headerCtrl = this;
			headerCtrl.loggedIn = false;
			headerCtrl.loggedOut = true;
			console.log(headerCtrl.loggedIn);


			this.searchRestaurants = function(){
            $scope.search;
             $http({
                    method: 'POST',
                    url: '/searchRestaurants',
                    data:{
                    search:$scope.search
                    }
                  }).then(function (res) {
                    restaurantsCtrl.filteredRestaurants = res.data;
                  });
                }
		}]
});