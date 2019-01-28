
function translate(){
	$.getJSON("lang_db.json", function(d){
		let html = $('body').html();
		for(let i=0; i<d.ru.length; i++){
			html = html.replace(d.ru[i], d.en[i]);
		}
		$('body').html(html);
	})
}