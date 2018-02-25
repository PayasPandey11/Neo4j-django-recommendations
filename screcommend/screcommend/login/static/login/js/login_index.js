$(document).ready(function() {

  $("#signup-button").click(function(){
    var username = $("#signup-username").val()
    var email = $("#signup-email").val()
    var password = $("#signup-password").val()
    console.log(username,email,password)
    var data = {"username":username,"email":email,"password":password}
    $.ajax({
      url: "signup/",
      type: "post",
      data: data,
      success: function(data) {

        if (data =="Success"){
          window.location.replace("/home");

        }
        else{
            console.log(data);
            $('#error').text(data);
        }

    }})

  });
  $("#signin-button").click(function(){
    var email = $("#signin-email").val()
    var password = $("#signin-password").val()
    console.log(email,password)
    var data = {"email":email,"password":password}
    $.ajax({
      url: "signin/",
      type: "post",
      data: data,
      success: function(data) {

        if (data =="Success"){
          window.location.replace("/home");

        }
        else{
            console.log(data);
            $('#error').text(data);
        }

    }})

  });
  $("#login_heading").click(function() {
    $("#signin-div").addClass("active");
    $("#signup-div").addClass("inactive");
    $("#signin-div").removeClass("inactive");
    $("#signup-div").removeClass("active");
  });
  $("#signup_heading").click(function() {
    $("#signup-div").addClass("active");
    $("#signin-div").addClass("inactive");
    $("#signin-div").removeClass("active");
    $("#signup-div").removeClass("inactive");
  });
});
