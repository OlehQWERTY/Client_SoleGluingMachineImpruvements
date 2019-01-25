// simple raplasing names according to lang_db dictionary (can be stored in DB)
// load this after all script cause it raplase names and some functions wouldn't work

console.log("I am with you");
function translate(strJson){
	// window.onload = function () {  // after page is loading
			// $.getJSON("lang_db.json", function(d){
			$.getJSON(strJson, function(d){  // read json obj with translation
				let html = $('body').html();
				for(let i=0; i<d.en.length; i++){  // replase text english to ukranian one
					html = html.replace(d.en[i], d.ua[i]);
				}
				$('body').html(html);
			})

  // }
}

// var str = "Mr Blue has a blue house and a blue car";
// var res = str.replace(/blue|house|car/gi, function (x) {
//   return x.toUpperCase();
// });