$(document).ready(function() {
  var projects = $(".multiple-items");

  // Initial configuration
  initializeSlick();

  // Update configuration on window resize
  $(window).resize(function() {
    if ($(window).width() < 600) {
      destroySlick();
      initializeSlick();
    } else {
      destroySlick();
      initializeSlick();
    }
  });

  function initializeSlick() {
    $(projects).slick({
      dots: true,
      infinite: true,
      slidesToShow: $(window).width() < 600 ? 1 : 3,
      slidesToScroll: 1,
      autoplay: true,
      autoplaySpeed: 2000,
      arrows: $(window).width() >= 350,
      centerMode: $(window).width() >= 350,
    });
  }

  function destroySlick() {
    if ($(projects).hasClass('slick-initialized')) {
      $(projects).slick('unslick');
    }
  }
});
