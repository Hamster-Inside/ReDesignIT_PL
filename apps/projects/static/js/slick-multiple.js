$('.multiple-items').slick({
  dots: true,
  infinite: true,
  slidesToShow: 3,
  slidesToScroll: 1,
  autoplay: true,
  autoplaySpeed: 2000,
  centerMode: true,
});

$(window).resize(function() {
  var projects = document.querySelector(".multiple-items");
  if ($(window).width() < 900) {
    $(projects).slick('slickSetOption', 'slidesToShow', 1);
  }
  else {
    $(projects).slick('slickSetOption', 'slidesToShow', 3);
  }
});