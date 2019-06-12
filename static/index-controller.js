var agenda = angular.module('agenda', ['ngMaterial', 'ngMessages'])

agenda.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('blue');
})

agenda.controller('Tabela', function($scope,$http) {
    $http.get('/contatos').then(function(response){
        $scope.pessoas = response.data
        console.log(response.data);
    }, function(error){
        console.log(error);
    });

});


agenda.controller('Index', function($scope) {
});