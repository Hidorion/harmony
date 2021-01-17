$(document).ready(function(){
    if (document.getElementById("gallery") !== null) {
        $(".div-img-container").click(function(){
            if (($(this).find(".div-desc")).is(':visible')) {
                $(".div-desc").fadeOut();
            }
            else {
                $(".div-desc").fadeOut();
                $(this).find(".div-desc").fadeIn();
            }
        });
    } 
});