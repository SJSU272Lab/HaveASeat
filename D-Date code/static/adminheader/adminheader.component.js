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
			    console.log('root',$rootScope);
			    $rootScope.loginDetails = null;
			    $rootScope.hideAdminHeader = true;
			    $rootScope.hideHeader = true;
			    $rootScope.hideWelcomeHeader = true;
			    $rootScope.loggedIn = false;
                $location.path('/');
			}

		}]
});
