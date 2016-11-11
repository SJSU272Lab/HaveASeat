angular.module('index')
.component('index', {
	templateUrl: 'static/index/index.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		function ($http, $scope, $location) {

             var indexCtrl = this;

		}]
});