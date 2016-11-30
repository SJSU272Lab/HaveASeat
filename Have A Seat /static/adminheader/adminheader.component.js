angular.module('adminheader')
.component('adminheader', {
	templateUrl: 'static/adminheader/adminheader.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
        '$rootScope',
        '$anchorScroll',
		function ($http, $scope, $location, $rootScope, $anchorScroll) {
			var headerCtrl = this;

			console.log('adminheader');

			$scope.logout = function(){
			    console.log('Loggin out from admin');
			    //should send logging out request to server here
                $location.path('/logout');
			}

		}]
});