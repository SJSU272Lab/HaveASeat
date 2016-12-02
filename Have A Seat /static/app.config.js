angular.module('HaveASeat')
.config(['$locationProvider','$routeProvider',
         function config($locationProvider, $routeProvider){

             $locationProvider.hashPrefix('!');
			 $routeProvider.
		        when('/index', {
		          template: '<index></index>'
		        }).
		        when('/home', {
		          template: '<home></home>'
		        }).
                when('/restaurants/:search', {
		          template: '<restaurants></restaurants>'
		        }).
		         when('/seats/:resId', {
		          template: '<seats></seats>'
		        }).
		         when('/login', {
		          template: '<login></login>'
		        }).
		         when('/signup', {
		          template: '<signup></signup>'
		        }).
		         when('/admin/:resId', {
		          template: '<admin></admin>'
		        }).
		         when('/logout', {
		          template: '<logout></logout>'
		        }).
		        otherwise('/index');
		 }
]);

