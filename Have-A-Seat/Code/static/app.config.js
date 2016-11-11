angular.module('HaveASeat')
.config(['$locationProvider','$routeProvider',
         function config($locationProvider, $routeProvider){
			$locationProvider.hashPrefix('!');
			 $routeProvider.
		        when('/login', {
		          template: '<login></login>'
		        }).
		        when('/owner', {
		          template: '<owner></owner>'
		        }).
		        when('/restaurants', {
		          template: '<restaurants></restaurants>'
		        }).
		        when('/index', {
		          template: '<index></index>'
		        }).
		         when('/seats/:resId', {
		          template: '<seats></seats>'
		        }).
		        otherwise('/index');
		    }
]);