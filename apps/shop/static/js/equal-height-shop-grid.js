$(document).ready(function() {
  var maxHeight = 0;
  $('.product-item-prev').each(function() {
    var height = $(this).height();
    maxHeight = Math.max(maxHeight, height);
  });
  $('.product-item-prev').height(maxHeight);
});