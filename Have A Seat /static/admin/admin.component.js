angular.module('admin')
.component('admin', {
	templateUrl: 'static/admin/admin.template.html',
	controller: [
		'$http',
		'$scope',
		'$location',
        '$rootScope',
        '$anchorScroll',
		function ($http, $scope, $location, $rootScope, $anchorScroll) {
			var headerCtrl = this;

			$http({
                    method: 'GET',
                    url: '/<string:restaurant_name>/checkOwnerSeats'
                }).then(function (res) {
                    var restaurants = res.data;
                });
		}]
});