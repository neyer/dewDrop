chrome.extension.sendMessage({}, function(response) {

  var alreadyBound = {};

  var menuElement = null;
  var currentUser = {};
  var userIdInMenu = null;

  var userTrustLocalMap = {};

  var getTrustUserKey = function (userId){
    return "trust-user-"+userId;
  };

  var storeTrustInUser = function (userId, amount){
     var trustUserKey = getTrustUserKey(userId);
    userTrustLocalMap[userId] = amount;
    var trustQuery = {};
    trustQuery[trustUserKey] = amount;
    chrome.storage.sync.set(trustQuery,
        function () { console.log("Stored trust in "+userId+" at "+amount);
        });
  };

  var getTrustInUser = function(userId){
    var trustUserKey = getTrustUserKey(userId);
    chrome.storage.sync.get(trustUserKey,
        function (record){
          console.log("got trust record for user "+userId+ ": "+record);
          console.log("record has value " + record[trustUserKey]);
          userTrustLocalMap[userId] = record[trustUserKey];
      });
  };

  var updateMenu =  function(userName, trustCount, userId){
    userIdInMenu = userId;

    var trustQuestion = "Do you trust them?";
    var userDescription = userName;

    var currentTrust = userTrustLocalMap[userId];

    if (currentTrust == 1){
        userDescription = userName + " :)";
        trustQuestion =  "Do you still trust them?";
    } else if (currentTrust == -1) {
        userDescription = userName + " :(";
   }
    var jup = [ 
       [ "h3", "DewDrop"],
       [ "p", { class : "user-handle" }, userDescription],
       [ "p", { class : "trust-level" },
           "Trust count: " + trustCount ],
       [ "p", trustQuestion  ],
       [ "div", { class : "form-indicate-trust" },
          [ "button", { class : "indicate-trust" }, "Yes" ],
          [ "button", { class : "indicate-distrust" }, "No" ],
       ],
     ];

     // set the html for this thing
     menuElement.html(JUP.html(jup));
     // now update the click handler

     $("button.indicate-trust").on("click", function () {
        storeTrustInUser(userId, 1);
        updateMenu(userName, trustCount, userId);
     });
     $("button.indicate-distrust").on("click", function(){
        storeTrustInUser(userId, -1);
        updateMenu(userName, trustCount, userId);
     });
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
    e.preventDefault();
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
          var userId = withoutBase;
          thisElement.data('user-id', userId);
          console.log('got id '+userId);
          getTrustInUser(userId);
          updateMenu(userName, 10, userId);
          var offset = thisElement.offset();
          menuElement.css(offset);
      }
   });
  }
  };
  applyLinks();
  setInterval(applyLinks, 5000);
});
