
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

             $http({
                    method: 'POST',
                    url: '/logout',
                    data:{
                          user: $rootScope.loginDetails
                        }
                }).then(function (res) {
                    $location.path('/');
                });




		}]
});
