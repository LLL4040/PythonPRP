$(function()
{
    $(".meun-item").click(function() 
    {
        $(".meun-item").removeClass("meun-item-active");
        $(this).addClass("meun-item-active");
        var itmeObj = $(".meun-item").find("img");
        itmeObj.each(function() 
        {
            var items = $(this).attr("src");
            items = items.replace("_grey.png", ".png");
            items = items.replace(".png", "_grey.png");
            $(this).attr("src", items);
        });
        var attrObj = $(this).find("img").attr("src");
        attrObj = attrObj.replace("_grey.png", ".png");
        $(this).find("img").attr("src", attrObj);
    });
    $(".toggle-btn").click(function() 
    {
        $("#leftMeun").toggleClass("show");
        $("#rightContent").toggleClass("pd0px");
    });
    $("#topAD").click(function() {
        $("#topA").toggleClass("glyphicon-triangle-right");
        $("#topA").toggleClass("glyphicon-triangle-bottom");
    });
    $("#topBD").click(function() {
        $("#topB").toggleClass("glyphicon-triangle-right");
        $("#topB").toggleClass("glyphicon-triangle-bottom");
    });
    $("#topaD").click(function() {
        $("#topa").toggleClass("glyphicon-triangle-right");
        $("#topa").toggleClass("glyphicon-triangle-bottom");
    });
    $("#topbD").click(function() {
        $("#topb").toggleClass("glyphicon-triangle-right");
        $("#topb").toggleClass("glyphicon-triangle-bottom");
    });
    $("#topcD").click(function() {
        $("#topc").toggleClass("glyphicon-triangle-right");
        $("#topc").toggleClass("glyphicon-triangle-bottom");
    });
    $("#topdD").click(function() {
        $("#topd").toggleClass("glyphicon-triangle-right");
        $("#topd").toggleClass("glyphicon-triangle-bottom");
    });
});

$(function () { 
    $('#topAD').collapse('hide');
    $('#topBD').collapse('hide');
    $('#topaD').collapse('hide');
    $('#topbD').collapse('hide');
    $('#topcD').collapse('hide');
    $('#topdD').collapse('hide');
});

$(function() 
{
    $(".hovertable").hide();
});

$(document).ready(function()
{
    $("#show").click(function () 
    {
        $(".hovertable").show();
    });
    $("#download").click(function () 
    {
        window.open("/download");
    });
});


