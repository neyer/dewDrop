console.log("and here we are");
$("a").each(function(element){
    console.log('got an element.');
    if (element.data('hovercard')){
        console.log("Got yo hovercard here "+element.data('hovercard'));
      }
});

console.log('to each his own');
