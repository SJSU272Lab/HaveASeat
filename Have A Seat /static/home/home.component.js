/**
 * Created by amitpandey on 11/14/16.
 */
angular.module('home')
.component('home', {
	templateUrl: 'static/home/home.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
		'$routeParams',
        "$rootScope",
		function ($http, $scope, $location,$routeParams, $rootScope) {
             var indexCtrl = this;
            $scope.showLogout= true;


                $http({
                    method: 'GET',
                    url: '/loggedinUser',
                }).then(function (res) {
                    console.log(res);
                    if(res.data.error){
                    $location.path('/');
                    }
                    else{
                            console.log($rootScope.loginDetails);
                            $scope.userName  = res.data.Name;
                    }
                });

            $scope.logoutZZ = function(){
                console.log('someeee');
                 $http({
                    method: 'GET',
                    url: '/logout',
                }).then(function (res) {
                    console.log(res);
                    console.log('Loggin out from admin');
                    console.log('root',$rootScope);
                    $rootScope.loginDetails = null;
                    $rootScope.hideAdminHeader = true;
                    $rootScope.hideHeader = true;
                    $rootScope.hideWelcomeHeader = true;
                    $rootScope.loggedIn = false;
                    $location.path('/');
                    });
//                });


			}

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



			 $rootScope.hideHeader=false
			 $rootScope.logout=false

                if(!$rootScope.loggedIn)
            	 {
                     $rootScope.hideHeader=true;
                     $rootScope.hideWelcomeHeader = false;
                     $rootScope.hideAdminHeader = true;
            	 }

		}]
});