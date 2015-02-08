<<<<<<< HEAD
// var app = angular.module("whoshome", []);

// app.config(function($httpProvider, $interpolateProvider) {
//     $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
//     $interpolateProvider.startSymbol('{$');
//     $interpolateProvider.endSymbol('$}');
// });

=======
>>>>>>> edce05ffd7c72f889cb84c06668c805e858eef8c
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

<<<<<<< HEAD
// app.controller("usersAtHomeCtrl", function($scope, $http){

// // 	$.ajax({
// //   dataType: "json",
// //   url: "http://www.whoshome.me/api/whoshome/",
// //   dataType: 'json',
// //   success: function (data) {
// //   		alert(data);
// //   		$scope.users = data;

// //   }
// // });
// 	 // $http.get('http://ip.jsontest.com/?callback=showMyIP').
// 	 //  success(function(data, status, headers, config) {
// 	 //    // this callback will be called asynchronously
// 	 //    // when the response is available

// 	 //    $scope.users = data;
// 	 //  }).
// 	 //  error(function(data, status, headers, config) {
// 	 //    // called asynchronously if an error occurs
// 	 //    // or server returns response with an error status.

// 	 //    $scope.users = "not good";
// 	 //  });

// });
=======
$(document).ready(function() {
  update_table();
});
>>>>>>> edce05ffd7c72f889cb84c06668c805e858eef8c
