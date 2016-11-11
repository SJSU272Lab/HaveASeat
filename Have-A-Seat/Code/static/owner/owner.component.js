angular.module('owner')
.component('owner', {
	templateUrl: 'static/owner/owner.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		function ($http, $scope, $location) {

             var resCtrl = this;
             $http({
			    method:'GET',
			    url:'/hello'}).then(function(res){
                 resCtrl.restaurants = res;
			    });
		}]
});