const backbut = document.querySelector('#back-container');
const logo = document.querySelector("#head-logo-img");

backbut.addEventListener('mouseup',event =>{
	location.href = "main.html"
})
logo.addEventListener('mouseup',event =>{
	location.href = "index.html";
})