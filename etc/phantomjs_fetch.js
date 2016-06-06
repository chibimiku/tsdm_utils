fetch a js after javascript eval.

var address = httpwww.tsdm.net;
var timeout = 5000;

var page = require('webpage').create();
page.open(address, function (status) {
    if (status !== 'success') {
        console.log('Unable to load the address!');
        phantom.exit();
    } else {
        window.setTimeout(function () {
            page.render(output);
			var code = page.evaluate(function() {
				return document.documentElement.outerHTML;
			});
			console.log(code);
            phantom.exit();
        }, timeout);  Change timeout as required to allow sufficient time 
    }
});