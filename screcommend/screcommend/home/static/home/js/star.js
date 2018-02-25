$(document).ready(function() {
  $("label").click(function(){
    $(this).parent().find("label").css({"color": "#D8D8D8"});
    $(this).css({"color": "#7ED321"});
    $(this).nextAll().css({"color": "#7ED321"});
    var movie = $(this).parent().prev().prev().text();
    var rating = $(this).prev().val()
    console.log(window.location.pathname);
    var data = {"movie":movie,"rating":rating}
    $.ajax({
      url: "/home/ratings/",
      type: "post",
      data: data,
      success: function(data) {
        if (window.location.pathname == "/movies/"){
          console.log("rated");
          data=0;
        }
        else if (data == 5){

          window.location.replace("/home");

        }
        else{
            $('#error').text(data);
        }

    }})
  });
});
