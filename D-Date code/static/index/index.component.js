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
            $scope.showLogout= true;




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