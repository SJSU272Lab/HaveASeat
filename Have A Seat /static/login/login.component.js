angular.module('login')
.component('login', {
	templateUrl: 'static/login/login.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
        '$rootScope',
        '$anchorScroll',
		function ($http, $scope, $location, $rootScope, $anchorScroll) {
			var loginCtrl = this;
		}]
});