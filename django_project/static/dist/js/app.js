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

$(document).ready(function() {
  update_table();
});
