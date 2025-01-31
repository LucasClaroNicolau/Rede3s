var agenda = angular.module('agenda', ['ngMaterial', 'ngMessages'])

agenda.config(function($mdThemingProvider) {
  $mdThemingProvider.theme('default')
    .primaryPalette('blue');
})

agenda.controller('Tabela', function($scope,$http,$mdDialog) {

    $scope.attContatos = function(){
        $http.get('/listcontatos').then(function(response){
            $scope.pessoas = response.data
        },function(error){
            console.log(error);
        });
    };

    $scope.attContatos();

     socket.on('buscar', function() {
        $scope.attContatos();
    });

    $scope.showAdvanced = function(ev) {
        $mdDialog.show({
            locals: {callback: $scope.attContatos},
            controller: DialogController,
            templateUrl: 'static/adicionar.html',
            targetEvent: ev,
            fullscreen: true
        })
    };

    function DialogController($scope, $mdDialog,$http, callback) {
        $scope.cancelar = function() {
            $mdDialog.hide();
        }

        $scope.add = function() {
            data = {
                "nome":""+$scope.nomeadd,
                "numero" : $scope.numeroadd
            }
            $http.post('/adccontato', data).then(function successCallback(response) {

                callback();

            }, function errorCallback(response) {

            });
            $mdDialog.hide();
        }
    }

    $scope.deletar = function(contatoId){
        $http.post('/rmvcontato', contatoId).then(function successCallback(response) {
                socket.on('buscar', function() {
                    $scope.attContatos();
                });

            }, function errorCallback(response) {

            });

     }
});



agenda.controller('Index', function($scope) {
});