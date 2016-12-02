
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


             if(($rootScope.loginDetails !== undefined) && ($rootScope.loginDetails !== null) ){
                $scope.hideLoginSignup = true;
                $scope.showLogout= false;

            }

            this.searchRestaurants = function() {
                $scope.search;
                var restaurantsSearchUrl ='/restaurants/' + $scope.search;
                $location.path(restaurantsSearchUrl);
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

            ////////////////////////////////////

            $scope.countdown;
              function startTimer(duration, display) {
              duration = 60*15;
              minutes = 15;
              seconds = 60;
                var timer = duration, minutes, seconds;
              var countDownerMethod = setInterval(function () {
                    minutes = parseInt(timer / 60, 10)
                    seconds = parseInt(timer % 60, 10);

                    minutes = minutes < 10 ? "0" + minutes : minutes;
                    seconds = seconds < 10 ? "0" + seconds : seconds;

                    var elem = document.getElementById("countdown");
                    elem.textContent = minutes + ":" + seconds;

                    if (--timer < 0) {
                        console.log(' clearing the timer');
                        clearInterval(countDownerMethod);

                      var elem = document.getElementById("countdown");
                    elem.textContent = minutes + ":" + seconds;
                    }

                }, 1000);
                }


                    startTimer();
            ////////////////////////////////////




		}]
});
