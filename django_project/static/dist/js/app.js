var app = angular.module("whoshome", []);

app.config(function($httpProvider, $interpolateProvider) {
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
});

function update_table() {
  console.log("THIS FUNC RUNNING");
  $.ajax({
    type: "GET",
    url: "http://www.whoshome.me/api/whoshome/",
    success: function() {
      alert("ASDF");
    }
  });
}

app.controller("usersAtHomeCtrl", function($scope, $http) {

  });
  // $http.get('http://ip.jsontest.com/?callback=showMyIP').
  //  success(function(data, status, headers, config) {
  //    // this callback will be called asynchronously
  //    // when the response is available

  //    $scope.users = data;
  //  }).
  //  error(function(data, status, headers, config) {
  //    // called asynchronously if an error occurs
  //    // or server returns response with an error status.

  //    $scope.users = "not good";
  //  });

});
