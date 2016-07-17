// JavaScript source code

$(function () {
    $(window).load(function () {
        $.getJSON($SCRIPT_ROOT + '/get_image_carousel',
        function (data) {
            $("#comment0").text(data.result.metadata[0].caption);
            $("#image0").prop("src", data.result.metadata[0].image_name);
            $("#comment1").text(data.result.metadata[1].caption);
            $("#image1").prop("src", data.result.metadata[1].image_name);
            $("#comment2").text(data.result.metadata[2].caption);
            $("#image2").prop("src", data.result.metadata[2].image_name);
            $("#comment3").text(data.result.metadata[3].caption);
            $("#image3").prop("src", data.result.metadata[3].image_name);
            $("#comment4").text(data.result.metadata[4].caption);
            $("#image4").prop("src", data.result.metadata[4].image_name);
            $("#comment5").text(data.result.metadata[5].caption);
            $("#image5").prop("src", data.result.metadata[5].image_name);
            $("#comment6").text(data.result.metadata[6].caption);
            $("#image6").prop("src", data.result.metadata[6].image_name);
            $("#comment7").text(data.result.metadata[7].caption);
            $("#image7").prop("src", data.result.metadata[7].image_name);
            $("#comment8").text(data.result.metadata[8].caption);
            $("#image8").prop("src", data.result.metadata[8].image_name);
            $("#comment9").text(data.result.metadata[9].caption);
            $("#image9").prop("src", data.result.metadata[9].image_name);
            $("#feedagram-button").fadeIn("slow");

        });
        return false;
    });
});
