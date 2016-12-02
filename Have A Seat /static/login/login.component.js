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


             if(($rootScope.loginDetails !== undefined) && ($rootScope.loginDetails !== null) ){
                $scope.hideLoginSignup = true;
                $scope.showLogout= false;

            }

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

             this.searchRestaurants = function() {
                $scope.search;
                var restaurantsSearchUrl ='/restaurants/' + $scope.search;
                $location.path(restaurantsSearchUrl);
            }

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
//                        $rootScope.hideHeader=false;
//                        $rootScope.logout=false;
//                        $rootScope.message=$rootScope.loginDetails.error;
                         loginUrl="/login"


                     }
                     else if($rootScope.loginDetails.login_type==="user")
                     {   $rootScope.hideHeader=false;
                         $rootScope.hideWelcomeHeader = true;
                         $rootScope.hideAdminHeader = true;
                         $rootScope.loggedIn=true
                         loginUrl="/home"

                     }

                     else if($rootScope.loginDetails.login_type==="owner")
                     {
                         $rootScope.hideHeader=true;
                         $rootScope.hideWelcomeHeader = true;
                         $rootScope.hideAdminHeader = false;
                         $rootScope.loggedIn=true
                         loginUrl="/admin/"+ $rootScope.loginDetails.restid;
                     }


                   $location.path(loginUrl);


                });



            }
		}]
});