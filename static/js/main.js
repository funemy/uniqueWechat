function flex() {
    var width = $(window).innerWidth();
    if (width <= 800) {
        $("#logo").css("display", "none");
        $("#list").removeClass("col-xs-5").addClass("col-xs-10");
    } else if (width > 800) {
        $("#logo").css("display", "block");
        list = $("#list");
        if (list.hasClass("col-xs-10")) {
            list.removeClass("col-xs-10").addClass("col-xs-5");
        }
    }
}
$(window).bind("resize", flex);
$(window).bind("load", flex);
