/**
 * Created by amitpandey on 11/14/16.
 */
angular.module('index')
.component('index', {
	templateUrl: 'static/index/index.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		'$routeParams',
        "$rootScope",
		function ($http, $scope, $location,$routeParams, $rootScope) {
             var indexCtrl = this;

			 $rootScope.hideHeader=false
			 $rootScope.logout=false



		}]
});