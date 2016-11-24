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
                }).then(function (res) {
                    restaurantsCtrl.restaurants = res.data;
                });

            }
		}]
});