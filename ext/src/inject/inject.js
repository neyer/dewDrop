chrome.extension.sendMessage({}, function(response) {

  var alreadyBound = {};

  var menuElement = null;
  var currentUser = {};

  var updateMenuUser = function(userName, userId){
      currentUser.name = userName;
      currentUser.id = userId;
  };

  var updateMenu =  function(userName, trustCount, userId){
    var jup = [ 
       [ "h3", "DewDrop"],
       [ "p", { class : "user-handle" }, userName ],
       [ "p", { class : "trust-level" },
           "Trust count: " + trustCount ],
       [ "p", "Do you trust them?" ],
       [ "div", { class : "form-indicate-trust" },
          [ "button", { class : "indicate-trust" }, "Yes" ],
          [ "button", { class : "indicate-distrust" }, "No" ],
       ],
     ];
     menuElement.html(JUP.html(jup));
  };

  var applyLinks = function() {
  if (document.readyState === "complete") {
    // make the menu box if it doesn't exist
    if (menuElement == null){
      console.log("DewDrop: creating menu");
      var jup = [ "div", { id : "dewdrop-box-main"}];
      var html = JUP.html(jup);
      $("body").append(html);
      menuElement = $("#dewdrop-box-main");
   }
  // attach a 'trust' or 'check trust' link to each person
  // all the links with people have a 'hovercard' data attribute
  var personLinkRegex = /\/ajax\/hovercard\/user/;
  var personLinkRegex2 = /\/ajax\/hovercard\/hovercard.php/;
  $("a").off("mousedown");
  $("a").mousedown(function(e){
    var thisElement = $(this); 
    var userName = thisElement.text();
    if (!e.button == 2) return;
    if (thisElement.data('hovercard')){
        var hovercardVal = thisElement.data('hovercard');
        var withoutBase = false;
        if (personLinkRegex.test(hovercardVal)){
          //we have a person link. remove everything that isn't their id
          withoutBase = hovercardVal.substring(28);
        } else if (personLinkRegex2.test(hovercardVal)){
           withoutBase = hovercardVal.substring(32);
        }
        if (!withoutBase) return;
          //see if we have to chop off the '&'
          var indexOfAmp = withoutBase.indexOf('&');
          if (indexOfAmp != -1){
                withoutBase = withoutBase.substring(0,indexOfAmp);
          }
          thisElement.data('user-id', withoutBase);
          console.log('got id '+thisElement.data('user-id'));
          var offset = thisElement.offset();
          console.log(offset);
          updateMenu(userName, 10, withoutBase);
          menuElement.css(offset);
          e.preventDefault();
      }
   });
  }
  };
  applyLinks();
  setInterval(applyLinks, 5000);
});
