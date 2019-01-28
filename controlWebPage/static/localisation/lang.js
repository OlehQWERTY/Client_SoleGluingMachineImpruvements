// simple raplasing names according to lang_db dictionary (can be stored in DB)
// load this after all script cause it raplase names and some functions wouldn't work

console.log("I am with you");

function replaceAll(str, find, replace) {
	return str.replace(new RegExp(find, 'g'), replace);
}

function translate(strJson){
	// window.onload = function () {  // after page is loading
			// $.getJSON("lang_db.json", function(d){
			$.getJSON(strJson, function(d){  // read json obj with translation
				let html = $('body').html();

				for(let i=0; i<d.en.length; i++){  // replase text english to ukranian one
					// var re = new RegExp("{[(" + d.ua[i] + ")]}", 'g'); // reg expression all (DO NOT WORK: WHY???)
					var ammount = html.split("{[(" + d.en[i] + ")]}").length;  // ammount of similar strings 
					console.log(ammount, d.en[i]);
					for(var n=0;n<=ammount;n++){  // teaplase all similar
						html = html.replace("{[(" + d.en[i] + ")]}", d.ua[i]);  // replase string with translated string
						// console.log(n);
					}
				}
				$('body').html(html);
			})

  // }
}