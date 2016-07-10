$(function () {
    $(".item").hover(
        function () {
            var that = this;
            item1Timer = setTimeout(function () {
                $(that).find(".p_content").animate({"top":80}, 30, function () {
                    $(that).find("span").fadeIn(0);
                    $(that).find(".p_status").fadeIn(0);
                    $(that).find(".p_desc").fadeIn(0);
                });
            }, 30);

        },
        function () {
            var that = this;
            clearTimeout(item1Timer);
            $(that).find("span").fadeOut(0);
            $(that).find(".p_status").fadeOut(0);
            $(that).find(".p_desc").fadeOut(0);
            $(that).find(".p_content").animate({"top":198}, 100);
        }
    )
});