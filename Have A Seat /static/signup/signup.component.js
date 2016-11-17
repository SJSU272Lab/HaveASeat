angular.module('signup')
.component('signup', {
	templateUrl: 'static/signup/signup.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
        '$rootScope',
        '$anchorScroll',
		function ($http, $scope, $location, $rootScope, $anchorScroll) {
			var signupCtrl = this;
		}]
});