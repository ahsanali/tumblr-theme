var casper = require('casper').create();

casper.start('http://www.tumblr.com/login', function() {
    this.fill('form#signup_form', {
        'user[email]':    'sn.ahsanali@gmail.com',
        'user[password]':    'batista2',
    }, true);
});


function insertScript() {
	INJECTION_SCRIPT = '<script> console.log("from code");</script>'

	var editor = ace.edit("editor");
	var text = editor.getSession().getValue();
	var reg = /\<\!\-\-Begin\ OneButton\-\-\>(.+?)\<\!\-\-End\ OneButton\-\-\>/i;
	var matches = text.match(reg);
	if (matches && matches.length == 2){
		text = text.replace(matches[1],INJECTION_SCRIPT);
		editor.getSession().setValue(text);
	}
	else{
		text = text.replace('</body>',"<!--Begin OneButton-->"+INJECTION_SCRIPT+"<!--End OneButton--></body>")
		editor.getSession().setValue(text);
	}
	return editor.getSession().getValue();
    

}

function getButton(){
	return document.getElementById("edit_html_button").textContent;
}

function getUpdateButton(){
	return document.querySelector("#edit_html_panel .buttons_right .button.green").textContent;
}
function getSubmitButton(){
	return document.querySelector("#edit_html_panel .buttons_right .button.blue").style.display;
}
casper.waitFor(function check() {
    return this.getCurrentUrl() ==  "https://www.tumblr.com/dashboard";
}, function then() {

	casper.open("https://www.tumblr.com/customize/").then(function(){
		this.echo(this.getCurrentUrl())
		this.echo("getting button text")
		this.echo( this.evaluate(getButton));
		this.click('div#edit_html_button');
		this.wait(2000, function() {

        	text = this.evaluate(insertScript);
        	this.echo(text);
        	this.echo( this.evaluate(getUpdateButton));
        	this.click("#edit_html_panel .buttons_right .button.green");

        	this.waitUntilVisible("#edit_html_panel .buttons_right .button.blue", function(){
        		this.echo( this.evaluate(getSubmitButton));
        		this.click("#edit_html_panel .buttons_right .button.blue");
        		this.echo("saving")
        		this.waitWhileVisible("#edit_html_panel .buttons_right .button.blue");
        		this.echo("saved")
        	})
	    });
	})

},function timeout() { // step to execute if check has failed
    this.echo("cannot login").exit();
});


casper.run(function() {
   this.exit();
});

