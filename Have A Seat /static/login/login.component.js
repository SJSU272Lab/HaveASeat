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
			var headerCtrl = this;

			this.login = function() {
                $scope.username;
				$scope.password;

				 $http({
                    method: 'POST',
                    url: '/login',
                    data:{
                        cred : { username : $scope.username , password: $scope.password}
                    }
                }).then(function (response) {
                    headerCtrl.loginDetails = response.data;
                     $rootScope.loginDetails = response.data;
                     $rootScope.hideHeader=true
                     $rootScope.logout=true


                     console.log($rootScope.loginDetails.name)



                });


                 $location.path("/index");


            }
		}]
});