const textHeadMain = document.querySelector('#enter-button');
const fgBodyC2 = document.querySelector('#fg-body-c2');
const logo = document.querySelector("#head-logo-img");
const loadScript = document.createElement('script');

function openPage(){
	fgBodyC2.innerHTML = mainBody;
	document.querySelector('body').appendChild(loadScript)
	loadScript.setAttribute('src', 'mainScript.js');
	loadScript.setAttribute('type','text/javacsript');
}
textHeadMain.addEventListener('mouseup',event =>{
	location.href = "main.html";
})

logo.addEventListener('mouseup',event =>{
	location.href = "index.html";
})