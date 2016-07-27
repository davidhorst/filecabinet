function loadProperties(){
    $.ajax({
      url: "/properties",
      method: "get",
      success: function(serverResponse) {
        $('#main-dashboard').html(serverResponse);
      }
    });

    // fetch('/properties', { credentials: 'same-origin' }).then(resp => resp.text()).then(html =>$('#body').html(html));
}


function loadNotes(){
    $.ajax({
      url: "/properties",
      method: "get",
      success: function(serverResponse) {
        $('#main-dashboard').html(serverResponse);
      }
    });
}

function renderTemplate(partialUrl,jsonUrl) {
    return Promise.all([
        fetch(partialUrl).then(resp => resp.text()),
        fetch(jsonUrl).then(resp => resp.json())
    ]).then(args => {
        var template = Handlebars.compile(args[0]);
        var html = template(args[1]);
        return html;
    });
}


var routes = [
    ['/properties', loadProperties],
    ['/property/(\\d+)/event/(\\d+)/notes', loadNotes],
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
