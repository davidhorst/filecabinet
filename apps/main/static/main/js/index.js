/***************************************/
/* CSRF TOKEN FUNCTIONS: DO NOT MODIFY */
/***************************************/

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/*******************************/
/* END OF CSRF TOKEN FUNCTIONS */
/*******************************/

function loadProperties(){
    $.ajax({
      url: "/properties",
      method: "get",
      success: function(serverResponse) {
        $('#main-dashboard').html(serverResponse);
      }
    });
    $.ajax({
      url: "/sidebar",
      method: "get",
      success: function(serverResponse) {
        $('#static-side-menu').html(serverResponse);
        $('#slide-side-menu').html(serverResponse);

      }
    });
}

function loadProperty(prop_id) {
    $.ajax({
        url: `/property/${prop_id}/events`,
        method: "get",
        success: function(serverResponse) {
            $('#main-dashboard').html(serverResponse);
        }
    });
    $.ajax({
      url: "/sidebar",
      method: "get",
      success: function(serverResponse) {
        $('#static-side-menu').html(serverResponse);
        $('#slide-side-menu').html(serverResponse);

      }
    });
}

function addNote(args) {
    $.ajax({
        url:  `/property/${args[0]}/event/${args[1]}/add_note`,
        method: "get",
        success: function(serverResponse) {
            $('#main-dashboard').html(serverResponse);
        }
    });
    $.ajax({
      url: "/sidebar",
      method: "get",
      success: function(serverResponse) {
        $('#static-side-menu').html(serverResponse);
        $('#slide-side-menu').html(serverResponse);

      }
    });
}

function addEvent(args) {
    $.ajax({
        url:  `/property/${args[0]}/add_event`,
        method: "get",
        success: function(serverResponse) {
            $('#main-dashboard').html(serverResponse);
        }
    });
    $.ajax({
      url: "/sidebar",
      method: "get",
      success: function(serverResponse) {
        $('#static-side-menu').html(serverResponse);
        $('#slide-side-menu').html(serverResponse);

      }
    });
}

function addProperty() {
    $.ajax({
        url: "/add_property",
        method: "get",
        success: function(serverResponse) {
            $('#main-dashboard').html(serverResponse);
        }
    });
    $.ajax({
      url: "/sidebar",
      method: "get",
      success: function(serverResponse) {
        $('#static-side-menu').html(serverResponse);
        $('#slide-side-menu').html(serverResponse);

      }
    });
}


    function loadNotes(args){
    $.ajax({
      url: `/property/${args[0]}/event/${args[1]}`,
      method: "get",
      success: function(serverResponse) {
        $('#main-dashboard').html(serverResponse);
      }
    });
    $.ajax({
      url: "/sidebar",
      method: "get",
      success: function(serverResponse) {
        $('#static-side-menu').html(serverResponse);
        $('#slide-side-menu').html(serverResponse);

      }
    });
}





function loadNote(args){
$.ajax({
  url: `/property/${args[0]}/event/${args[1]}/note/${args[2]}`,
  method: "get",
  success: function(serverResponse) {
    $('#main-dashboard').html(serverResponse);
  }
});
$.ajax({
      url: "/sidebar",
      method: "get",
      success: function(serverResponse) {
        $('#static-side-menu').html(serverResponse);
        $('#slide-side-menu').html(serverResponse);

      }
    });
}
function addAlert(args) {
    $.ajax({
        url:  `/property/${args[0]}/event/${args[1]}/add_alert`,
        method: "get",
        success: function(serverResponse) {
            $('#main-dashboard').html(serverResponse);
        }
    });
    $.ajax({
      url: "/sidebar",
      method: "get",
      success: function(serverResponse) {
        $('#static-side-menu').html(serverResponse);
        $('#slide-side-menu').html(serverResponse);

      }
    });
}


function loadAlert(args){
$.ajax({
  url: `/property/${args[0]}/event/${args[1]}/alert/${args[2]}`,
  method: "get",
  success: function(serverResponse) {
    $('#main-dashboard').html(serverResponse);
  }
});
$.ajax({
      url: "/sidebar",
      method: "get",
      success: function(serverResponse) {
        $('#static-side-menu').html(serverResponse);
        $('#slide-side-menu').html(serverResponse);

      }
    });
}


var routes = [
    ['/properties', loadProperties],
    ['/property/(\\d+)/event/(\\d+)/addNote', addNote],
    ['/property/(\\d+)/event/(\\d+)/notes', loadNotes],
    ['/property/(\\d+)/event/(\\d+)/note/(\\d+)', loadNote],

    ['/property/(\\d+)/event/(\\d+)/addAlert', addAlert],
    ['/property/(\\d+)/event/(\\d+)/alert/(\\d+)', loadAlert],


    ['/property/(\\d+)/addEvent', addEvent],
    ['/property/(\\d+)/events', loadProperty],
    ['/add_property', addProperty],

];

var originalHash = (window.location.hash || '#').substr(1);

function loadRoute() {
    var newHash = (window.location.hash || '#').substr(1);

    var route = routes.find(r => new RegExp(`^${r[0]}$`).exec(newHash));
    if (route) {
        route[1](new RegExp(route[0]).exec(newHash).slice(1));
    } else {
         window.location.hash = '/properties';
    }

    originalHash = newHash;
}

$(window).bind('hashchange', loadRoute);
loadRoute();
