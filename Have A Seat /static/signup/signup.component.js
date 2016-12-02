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


            this.searchRestaurants = function() {
                $scope.search;
                var restaurantsSearchUrl ='/restaurants/' + $scope.search;
                $location.path(restaurantsSearchUrl);
            }

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