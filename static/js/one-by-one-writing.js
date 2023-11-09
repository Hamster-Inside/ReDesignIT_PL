var text = "私に連絡して";
var delay = 150;
var elem = $("#myText");

var addTextByDelay = function (text, elem, delay) {
  if (!elem) {
    elem = $("body");
  }
  if (!delay) {
    delay = 150;
  }

  var index = 0;
  var reverse = false;

  var updateText = function () {
    elem.text(text.slice(0, index));

    if (!reverse) {
      index++;

      if (index > text.length) {
        reverse = true;
        setTimeout(updateText, delay * 2);
      } else {
        setTimeout(updateText, delay);
      }
    } else {
      index--;

      if (index >= 0) {
        setTimeout(updateText, delay);
      } else {
        setTimeout(function () {
          reverse = false;
          index = 0;
          updateText(); // Start the loop again
        }, delay * 2);
      }
    }
  };

  updateText();
};

addTextByDelay(text, elem, delay);
