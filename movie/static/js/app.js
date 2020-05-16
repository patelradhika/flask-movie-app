function main() {
    $('.card').hover(function() {
        $(this).find('.movies-image').css({"filter": "brightness(20%)"});
        $(this).find('.movies-star').toggleClass('hide');
        $(this).find('.movies-rating').toggleClass('hide');
        $(this).find('.movies-detail').toggleClass('hide');
    }, function() {
        $(this).find('.movies-image').css({"filter": "brightness(100%)"});
        $(this).find('.movies-star').toggleClass('hide');
        $(this).find('.movies-rating').toggleClass('hide');
        $(this).find('.movies-detail').toggleClass('hide');
    });
}

$(document).ready(main());