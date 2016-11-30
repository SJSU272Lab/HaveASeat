
angular.module('logout')
.component('logout', {
	templateUrl: 'static/logout/logout.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		'$routeParams',
        "$rootScope",
		function ($http, $scope, $location,$routeParams, $rootScope) {
             console.log('logout');

            $rootScope.hideHeader=true;
            $rootScope.hideWelcomeHeader = false;
            $rootScope.hideAdminHeader = true;
		}]
});