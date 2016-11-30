angular.module('welcomeheader')
.component('welcomeheader', {
	templateUrl: 'static/welcomeheader/welcomeheader.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
        '$rootScope',
        '$anchorScroll',
		function ($http, $scope, $location, $rootScope, $anchorScroll) {
			var headerCtrl = this;

			console.log('welcomeheader');


		}]
});