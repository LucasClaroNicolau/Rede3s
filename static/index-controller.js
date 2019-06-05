var app = angular.module('app', ['ngMaterial', 'ngMessages'])

.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('green');
})

.controller('IndexCtrl', function($scope, $http) {
 $scope.oi = 'oiassas';

 $http.get('http://www.mocky.io/v2/5cf7075c320000a5fb8cd580').then(function(response){
    console.log(response);
 }, function(error){
    console.log(error);
 });

});