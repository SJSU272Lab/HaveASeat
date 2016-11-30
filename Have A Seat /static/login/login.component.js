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
            var loginUrl;

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


                     if(($rootScope.loginDetails.error==="Invalid Passowrd. Please try again.") || ($rootScope.loginDetails.error==="Invalid Username"))
                     {
                        $rootScope.hideHeader=false;
                        $rootScope.logout=false;
                        $rootScope.message=$rootScope.loginDetails.error;
                         loginUrl="/login"


                     }
                     else if($rootScope.loginDetails.login_type==="user")
                     {   $rootScope.hideHeader=true
                         $rootScope.logout=true
                         loginUrl="/index"

                     }

                     else if($rootScope.loginDetails.login_type==="owner")
                     {   $rootScope.hideHeader=true
                         $rootScope.hideSearch=true
                         $rootScope.logout=true
                         loginUrl="/admin/"+ $rootScope.loginDetails.restid;
                     }


                   $location.path(loginUrl);

                });



            }
		}]
});