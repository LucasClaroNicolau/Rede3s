var agenda = angular.module('agenda', ['ngMaterial', 'ngMessages'])

agenda.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('blue');
})

agenda.controller('Tabela', function($scope,$http,$mdDialog) {

    $http.get('/listcontatos').then(function(response){
        $scope.pessoas = response.data
        console.log(response.data);
    }, function(error){
        console.log(error);
    });

    $scope.showAdvanced = function(ev) {
        $mdDialog.show({
            controller: DialogController,
            templateUrl: 'static/adicionar.html',
            targetEvent: ev,
        })
    };

    function DialogController($scope, $mdDialog,$http ) {
        $scope.cancelar = function() {
            $mdDialog.hide();
        }

        $scope.add = function() {
            console.log($scope.nomeadd);
            console.log($scope.numeroadd);
            data = {
                "nome":""+$scope.nomeadd,
                "numero" : $scope.numeroadd
            }
            $http.post('/adccontato', data).then(function successCallback(response) {
                $http.get('/listcontatos').then(function(response){
                $scope.pessoas = response.data
            }, function(error){
                console.log(error);
            });
            }, function errorCallback(response) {

            });
            $mdDialog.hide();
        }
     }
});



agenda.controller('Index', function($scope) {
});