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

$(document).ready(function() {
    $(".filter-checkbox, #price-filter-btn").on("click", function(){
        console.log("A checkbox is selected");

        let filter_object = {}

        let min_price = $("#max_price").attr("min")
        let max_price = $("#max_price").val()

        filter_object.min_price = min_price;
        filter_object.max_price = max_price;


        $(".filter-checkbox").each(function(){
            let filter_value = $(this).val()
            let filter_key = $(this).data("filter")

            // console.log("Filter value: " + filter_value);
            // console.log("Key: " + filter_key);

            filter_object[filter_key] = Array.from(document.querySelectorAll('input[data-filter=' + filter_key + ']:checked')).map(function(element){
                return element.value
            })
        })
        console.log("Filter object: ", filter_object);

        $.ajax({
            url: '/filter_products',
            data: filter_object,
            dataType: 'json',
            beforeSend: function(){
                console.log("Trying to filter products...");
            },
            success: function(response){
                console.log(response);
                console.log("Data filtered successfully");
                $("#filtered-product").html(response.data)
            },
        })
    })

    $("#max_price").on("blur", function(){
        let min_price = $(this).attr("min")
        let max_price = $(this).attr("max")
        let current_price = $(this).val()

        // console.log("Current price is: ", current_price);
        // console.log("min price is: ", min_price);
        // console.log("max price is: ", max_price);

        if (current_price < parseInt(min_price) || current_price > parseInt(max_price)) {
            console.log("Price out of range: ", current_price);

            min_price = Math.round(min_price * 100) / 100
            max_price = Math.round(max_price * 100) / 100
            // console.log("################################");
            // console.log("min price is: ", min_Price);
            // console.log("max price is: ", max_Price);
            alert("Price must be between $" +min_price + " and $" +max_price)
            $(this).val(min_price)
            $("#range").val(min_price)

            $(this).focus()

            return false
        }

    })

})

//! Add to cart functionality
$(".add-to-cart-btn").on("click", function(){

    let this_val = $(this)
    let index = this_val.attr("data-index")

    let quantity = $(".product-quantity-" + index).val()
    let product_id = $(".product-id-" + index).val()

    let product_title = $(".product-title-" + index).val()
    let product_price = $(".current-product-price-" + index).text()

    let product_pid = $(".product-pid-" + index).val()
    let product_image = $(".product-image-" + index).val()
    

    console.log("Quantity: ", quantity);
    console.log("Title: ", product_title);
    console.log("Price: ", product_price);
    console.log("Id: ", product_id);
    console.log("PId: ", product_pid);
    console.log("image: ", product_image);
    console.log("Index: ", index);
    console.log("Current Element: ", this_val);

    $.ajax({
        url: '/add_to_cart',
        data: {
            'id': product_id,
            'pid': product_pid,
            'image': product_image,
            'quantity': quantity,
            'title': product_title,
            'price': product_price,
        },
        dataType: 'json',
        beforeSend: function(){
            console.log("Adding products to cart...");
        },
        success: function(response)
        {
            this_val.html("✔")
            console.log("Added products to cart successfully!");
            $(".cart-items-count").text(response.total_cart_items)
        },
    })
})

// $("#add-to-cart-btn").on("click", function(){
//     let quantity = $("#product-quantity").val()
//     let product_id = $(".product-id").val()
//     let product_title = $(".product-title").val()
//     let product_price = $(".current-product-price").text()
//     let this_val = $(this)

//     console.log("Quantity: ", quantity);
//     console.log("Title: ", product_title);
//     console.log("Price: ", product_price);
//     console.log("Id: ", product_id);
//     console.log("Current Element: ", this_val);

//     $.ajax({
//         url: '/add_to_cart',
//         data: {
//             'id': product_id,
//             'quantity': quantity,
//             'title': product_title,
//             'price': product_price,
//         },
//         dataType: 'json',
//         beforeSend: function(){
//             console.log("Adding products to cart...");
//         },
//         success: function(response)
//         {
//             this_val.html("Item added successfully")
//             console.log("Added products to cart successfully!");
//             $(".cart-items-count").text(response.total_cart_items)
//         },
//     })
// })