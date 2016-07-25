function loadHome() {
    renderTemplate('/static/main/user-login.html','/static/home_app/json/event14.json').then(html => {
        $('#template_content').html(html);
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

function loadProperty(args) {
    renderTemplate('/static/home_app/html/property.html','/api/property/' + args[0]).then(html =>{
        $('#template_content').html(html);
    });
}


var routes = [
    ['/', loadHome],
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


loadRoute()