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

		}]
});