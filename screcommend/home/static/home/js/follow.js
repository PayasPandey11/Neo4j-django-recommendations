$(document).ready(function() {
  $(".rec-follow").click(function(e){
    var follow_status = $(e.target).text();
    console.log(follow_status);
    var username = $(this).prev().attr('value');
    var data = {"username":username,"follow_status":follow_status};
    var p = e.currentTarget;
    $.ajax({
      url: "follow/",
      type: "post", // or "get"
      data: data,
      success: function(data) {
        console.log(data)
        if (data == "Follow"){
            console.log("f",data);
            $(p).html('Unfollow');

        }
        if (data == "Unfollow"){
            console.log("nf",data);
            $(p).html('Follow');
        }

    }})

  });
});
