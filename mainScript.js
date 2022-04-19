const codeport = document.querySelector('#codeport');
const designport = document.querySelector('#designport');
const about = document.querySelector('#about');
const back = document.querySelector('#back-container');
const lscodeport = document.createElement('script');
const logo = document.querySelector("#head-logo-img");

codeport.addEventListener('mouseover',event =>{
	codeport.firstChild.nextElementSibling.classList.add('dark')
	codeport.firstChild.nextElementSibling.nextElementSibling.setAttribute('id','over');
})
codeport.addEventListener('mouseleave',event =>{
	codeport.firstChild.nextElementSibling.classList.remove('class', 'dark')
	codeport.firstChild.nextElementSibling.nextElementSibling.removeAttribute('id','over');
})

designport.addEventListener('mouseover',event =>{
	designport.firstChild.nextElementSibling.classList.add('dark')
	designport.firstChild.nextElementSibling.nextElementSibling.setAttribute('id','over');

})
designport.addEventListener('mouseleave',event =>{
	designport.firstChild.nextElementSibling.classList.remove('class', 'dark')
	designport.firstChild.nextElementSibling.nextElementSibling.removeAttribute('id','over');
})

about.addEventListener('mouseover',event =>{
	about.firstChild.nextElementSibling.classList.add('dark')
	about.firstChild.nextElementSibling.nextElementSibling.setAttribute('id','over');

})
about.addEventListener('mouseleave',event =>{
	about.firstChild.nextElementSibling.classList.remove('class', 'dark')
	about.firstChild.nextElementSibling.nextElementSibling.removeAttribute('id','over');
})

codeport.addEventListener('mouseup',event =>{
	location.href = "code.html"
})

designport.addEventListener('mouseup',event =>{
	location.href = "design.html";
})

about.addEventListener('mouseup',event =>{
	location.href = "about.html";
})

logo.addEventListener('mouseup',event =>{
	location.href = "index.html";
})