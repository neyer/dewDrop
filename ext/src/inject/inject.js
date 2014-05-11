chrome.extension.sendMessage({}, function(response) {

  // we use a single gui element for dewdrop menu
  // just reposition this thing
  var menuElement = null;
  var currentUser = {};
  var userIdInMenu = null;

  //base url for the backend
  var baseURL = "http://dewdewdrop.herokuapp.com";

  // this a locacl cache of what is kept in chrome's storage
  // since chrome's storage is async
  var userTrustLocalMap = {};


  // we define a key for each user
  // i should add 'facebook' to this so we specify domain, username
  var getTrustUserKey = function (userId){
    return "trust-user-"+userId;
  };


  // store the trust locally, in chrome's sync storage
  // we'd want to give people the option not to do this, as
  // chrome's sync storage is not scure
  // PLACE API HOOK HERE 
  var storeTrustInUser = function(userId, amount){
    var trustUserKey = getTrustUserKey(userId);
    userTrustLocalMap[userId] = amount;
    var trustQuery = {};
    trustQuery[trustUserKey] = amount;

    //id of the user who is logged in
    //we find the mini profile picture on the page, find it's prop id, split it based on _ and take the 4th entry of the returned array to get the facebook id
    var loggedInUserId = $('.headerTinymanPhoto').prop('id').toString().split('_')[3];
    var jqxhrTrust = $.ajax({
      type: "POST",
      url: baseURL + "/api/v1/users/facebook/" + loggedInUserId + "/supporters",
      data: {
        "network": "facebook", //should change with the social platform we are on
        "support": userId
      },
      success: function(data, textStatus, jqXHR){
        console.log("great success");
      },
      error: function(jqXHR, textStatus, err){
        console.error("Server is having trouble allowing " + loggedInUserId + " supporting " + userId + " error data: " + textStatus);
      },
      dataType: "json" //may need to change to allow client to make it's own best guess
    });

    chrome.storage.sync.set(trustQuery,
      function(){
        console.log("Stored trust in " + userId + " at " + amount);
      });
  };


  // get the trust from chrome's sync storage
  // again, give ppl the option to do this,
  // as chrome's sync storage is stored insecurely on local HD
  // PLACE API HOOK HEREE
  var getTrustInUser = function(userId){
    var trustUserKey = getTrustUserKey(userId);
    chrome.storage.sync.get(trustUserKey,
        // chrome storage api's are async
        function (record){
          console.log("trust record  for " + userId + 
                    " has value " + record[trustUserKey]);
          var trustLevel = record[trustUserKey];
          userTrustLocalMap[userId] = trustLevel;
          // update the dialog if we have it
          if(trustLevel > 0)
            $("#trust-level-user-"+userId).html("Is trusted.");
          else if (trustLevel < 0)
            $("#trust-level-user-"+userId).html("Is distrusted.");
      });
  };

  var hideMenu = function () {
      var offset = { top : - 1000};
      if (menuElement)
        menuElement.css(offset);
  }
  var updateMenu =  function(userName, trustCount, userId){
    userIdInMenu = userId;
    var trustQuestion = "Do you trust them?";
    var userDescription = "Is unknown";
        var currentTrust = userTrustLocalMap[userId];
    if (currentTrust == 1){
        userDescription = "Is trusted."
        trustQuestion =  "Do you still trust them?";
    } else if (currentTrust == -1) {
        userDescription = "Is distrusted";
    }


    // i'm using this library called jup to build the html
    // it's a way of representing html as javascript
    // i think it's simple and straightfoward
    // and it looks better than raw html in escaped strings
    var jup = [ 
       [ "h3", "dewDrop"],
       // i like camel casing the name
       // it's not what most people are used to seeing
       // but it makes perfect sense to programmers
       // it fits with the notion of alogrithmic trust
       // and there's a neat symmetry about it - the d and p are mirorrs
       // o and e are vowels; you can form one from the other
       // and a 'w' is like two upsidetown 'r's mirroring erach other
       // also, it's visuaslly representative of a dewdrop 
       // i.e. the bugle in the middle
       // i of course defer to you on stylistic matters
       [ "p", { class : "user-handle"}, userName],
       [ "p", { class : "trust-level",
                   id : "trust-level-user-"+userId },
           userDescription],
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
 
  // hook up global listeners
 $(document).on("scroll", function () {
    hideMenu();
  });
  // periodically apply this hook
  // so that as new links are added, they get the context menu
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
  // attach the dialog to each link with a person
  // all the links with people have a 'hovercard' data attribute
  var personLinkRegex = /\/ajax\/hovercard\/user/;
  var personLinkRegex2 = /\/ajax\/hovercard\/hovercard.php/;
  $("a").off("contextmenu");
  $("a").on("contextmenu", function(e){
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
        e.preventDefault();
        e.stopPropagation();

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
          var scrolltop = $(window).scrollTop();
          console.log("scrolltop is "+scrolltop);
          console.log(offset);
          offset.top = offset.top - scrolltop;
        
          menuElement.css(offset);
      }
   });
  }
  };
  applyLinks();
  setInterval(applyLinks, 5000);
});
