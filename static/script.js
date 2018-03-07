$(document).ready(function(){
    $("button").click(function(){
        color = $(this).attr("id");
        $.get("color", {"color": color}, function(res){
            output = "<h1>You chose " + res.name + "!</h1>";
            output += "<img src='static/img/" + res.file + "'>";
            $("#turtle").html(output);
        },"json");
    });
    $("form").submit(function(){
        color = $("#color_txt").val();
        $.get("color", {"color": color}, function(res){
            output = "<h1>You chose " + res.name + "!</h1>";
            output += "<img src='static/img/" + res.file + "'>";
            $("#turtle").html(output);
        },"json");
        return false;
    });
});