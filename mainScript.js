/* Declatrations */
const codeport = document.querySelector('#codeport');
const designport = document.querySelector('#designport');
const about = document.querySelector('#about');
const back = document.querySelector('#back-container');
const lscodeport = document.createElement('script');
const logo = document.querySelector("#head-logo-img");

/* Nav Menu Event Listeners on main.html */

/* Code Portfolio Highlight */
codeport.addEventListener('mouseover',event =>{
	codeport.firstChild.nextElementSibling.classList.add('dark')
	codeport.firstChild.nextElementSibling.nextElementSibling.setAttribute('id','over');
})
codeport.addEventListener('mouseleave',event =>{
	codeport.firstChild.nextElementSibling.classList.remove('class', 'dark')
	codeport.firstChild.nextElementSibling.nextElementSibling.removeAttribute('id','over');
})

/* Design Portfolio Highlight */
designport.addEventListener('mouseover',event =>{
	designport.firstChild.nextElementSibling.classList.add('dark')
	designport.firstChild.nextElementSibling.nextElementSibling.setAttribute('id','over');
})
designport.addEventListener('mouseleave',event =>{
	designport.firstChild.nextElementSibling.classList.remove('class', 'dark')
	designport.firstChild.nextElementSibling.nextElementSibling.removeAttribute('id','over');
})

/* About Highlight */
about.addEventListener('mouseover',event =>{
	about.firstChild.nextElementSibling.classList.add('dark')
	about.firstChild.nextElementSibling.nextElementSibling.setAttribute('id','over');
})
about.addEventListener('mouseleave',event =>{
	about.firstChild.nextElementSibling.classList.remove('class', 'dark')
	about.firstChild.nextElementSibling.nextElementSibling.removeAttribute('id','over');
})

/* Nav to Code Portfolio */
codeport.addEventListener('mouseup',event =>{
	location.href = "code.html"
})
/* Nav to Design Portfolio */
designport.addEventListener('mouseup',event =>{
	location.href = "design.html";
})
/* Nav to About Portfolio */
about.addEventListener('mouseup',event =>{
	location.href = "about.html";
})

/* Return to Splash Screen */
logo.addEventListener('mouseup',event =>{
	location.href = "index.html";
})