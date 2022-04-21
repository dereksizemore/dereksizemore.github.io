/* DECLARATIONS */
const textHeadMain = document.querySelector('#enter-button');
const fgBodyC2 = document.querySelector('#fg-body-c2');
const logo = document.querySelector("#head-logo-img");
const loadScript = document.createElement('script');

/* Event Listerens */

/* Enter Main Page */
textHeadMain.addEventListener('mouseup',event =>{
	location.href = "main.html";
})