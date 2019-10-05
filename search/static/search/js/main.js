/* It's a small function for to spawn print of the spinner */
function connect() {
    $('#spinner').show(600);
}


/* These code line use js for change the input on page top */
document.getElementById('id_food');
{
    $('#id_food').toggleClass("color_find_base");
}


/* The function below record a click of the user
She records the click that selects a non-registered
    favorite food and will indicate it to the system to create the record */
$(document).on("click", "#check_saveFood", function () {
    var product = $(this).val();
    $(this).toggleClass('orange_back');
    console.log(product);
    console.log('True');

    $.ajax({
        url: '/search/favorites.html',
        data: {
            'product': product
        },
        dataType: 'json',
        success: function (data) {
            if (data['error_food']) {
                if (!document.getElementById("result_error")) {
                    $('#error_result').append('<p id="result_error" class="result_error">' + data['error_food'] + '</p>');
                }
            }
            if (data['success_save']) {
                if (!document.getElementById("result_success")) {
                    $('#error_result').append('<p id="result_success" class="result_success">' + data['success_save'] + '</p>');

                }
            }
        }
    });
});
