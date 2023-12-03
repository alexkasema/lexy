console.log("Working well");

$("#commentForm").submit(function(e) {
    e.preventDefault();

    $.ajax({
        data: $(this).serialize(),

        method: $(this).attr("method"),

        url: $(this).attr("action"),

        dataType: "json",

        success: function(response) {
            console.log("Review Saved to db...");

            if (response.bool == true) {
                $("#review-notification").html("Review Added successfully")
                $(".hide-comment-form").hide()
                $(".hide-review").hide()
            }
        }
    })
})