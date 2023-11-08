var text="This text will be written one by one.";
var delay=300;
var elem = $("#myText");
//text- string
//elem - jQuery element where text is to be attached
//delay - the delay in each text



var addTextByDelay = function(text,elem,delay){
    if(!elem){
        elem = $("body");
    }
    if(!delay){
        delay = 300;
    }
    if(text.length >0){
        //append first character
        elem.append(text[0]);
        setTimeout(
            function(){
                //Slice text by 1 character and call function again
                addTextByDelay(text.slice(1),elem,delay);
             },delay
            );
    }
}

addTextByDelay(text,elem,delay);
addTextByDelay(text,elem,delay);
