function loadProperties(){
    $.ajax({
      url: "/properties",
      method: "get",
      success: function(serverResponse) {
        $('#body').html(serverResponse);
      }
    });

    // fetch('/properties', { credentials: 'same-origin' }).then(resp => resp.text()).then(html =>$('#body').html(html));
}

function loadProperty(args) {
    renderTemplate('/static/home_app/html/property.html').then(html =>{
        $('#container').html(html);
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
    ['/', loadProperties],
    ['/property/(\\d+)', loadProperty]
];

var originalHash = (window.location.hash || '#').substr(1);

function loadRoute() {
    var newHash = (window.location.hash || '#').substr(1);

    var route = routes.find(r => new RegExp(`^${r[0]}$`).exec(newHash));
    if (route) {
        route[1](new RegExp(route[0]).exec(newHash).slice(1));
    } else {
         window.location.hash = '/';
    }

    originalHash = newHash;
}

$(window).bind('hashchange', loadRoute);
loadRoute();
