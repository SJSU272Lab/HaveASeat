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
			var headerCtrl = this;

			this.signup = function() {
				$scope.firstName;
				$scope.lastName;
                $scope.emailid;
				$scope.password;

				 $http({
                    method: 'POST',
                    url: '/signup',
                    data:{
                        cred : { firstName : $scope.firstName ,lastName: $scope.lastName, emailid: $scope.emailid ,password: $scope.password}
                    }


                }).then(function (response) {
                    headerCtrl.registerDetails= response.data;
					 $rootScope.registerDetails=response.data;
					 $rootScope.message=" you are registerd , Please login to proceed";

                });



            },

            redirct= function() {

				 $location.path("/login");

			}

		}]

});