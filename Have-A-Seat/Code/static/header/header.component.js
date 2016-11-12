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
//             $http({
//                    method: 'POST',
//                    url: '/searchRestaurants',
//                    data:{
//                    search:$scope.search
//                    }
//                  }).then(function (res) {
//                    headerCtrl.filteredRestaurants = res.data;
//                    $location.path('restaurants');
//                  });
                }
		}]
});