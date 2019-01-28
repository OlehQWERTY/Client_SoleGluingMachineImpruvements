// return cookie with name, if exist, or undefined
function getCookie(name) {
	var matches = document.cookie.match(new RegExp(
		"(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
	));
	return matches ? decodeURIComponent(matches[1]) : undefined;
}

// document.cookie = "userName=Vasya";

function setCookie(name, value) {
	if(name == "language"){
		location.reload();  // reload page
	}
	var date = new Date(0);
	document.cookie = name + '=' + value + "; path=/;";
	// document.cookie = "userName=Vasya";
	// console.log(name + '=' + value + "; path=/; expires=" + date.toUTCString());
}

function delCookie(name) {
	var date = new Date(0);
	document.cookie = name + "=; path=/; expires=" + date.toUTCString();
}

// var date = new Date(new Date().getTime() + 60 * 60 * 24 * 1000);	// one day life 
// document.cookie = "name=value; path=/; expires=" + date.toUTCString();