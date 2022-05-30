const backbut = document.querySelector('#back-container');
const logo = document.querySelector('#head-logo-img');
const webport = document.querySelector('#webport');
const designport = document.querySelector('#designport');
const python = document.querySelector('#pythonport');

backbut.addEventListener('mouseup',event =>{
	location.href = "../index.html"
})
logo.addEventListener('mouseup',event =>{
	location.href = "../index.html";
})

webport.addEventListener('mouseover',event =>{
	webport.firstChild.nextElementSibling.classList.add('dark')
	webport.firstChild.nextElementSibling.nextElementSibling.setAttribute('id','over');
})
webport.addEventListener('mouseleave',event =>{
	webport.firstChild.nextElementSibling.classList.remove('class', 'dark')
	webport.firstChild.nextElementSibling.nextElementSibling.removeAttribute('id','over');
})

pythonport.addEventListener('mouseover',event =>{
	pythonport.firstChild.nextElementSibling.classList.add('dark')
	pythonport.firstChild.nextElementSibling.nextElementSibling.setAttribute('id','over');

})
pythonport.addEventListener('mouseleave',event =>{
	pythonport.firstChild.nextElementSibling.classList.remove('class', 'dark')
	pythonport.firstChild.nextElementSibling.nextElementSibling.removeAttribute('id','over');
})

designport.addEventListener('mouseover',event =>{
	designport.firstChild.nextElementSibling.classList.add('dark')
	designport.firstChild.nextElementSibling.nextElementSibling.setAttribute('id','over');

})
designport.addEventListener('mouseleave',event =>{
	designport.firstChild.nextElementSibling.classList.remove('class', 'dark')
	designport.firstChild.nextElementSibling.nextElementSibling.removeAttribute('id','over');
})

webport.addEventListener('mouseup',event =>{
	location.href = "webport.html"
})

pythonport.addEventListener('mouseup',event =>{
	location.href = "pythonport.html";
})

designport.addEventListener('mouseup',event =>{
	location.href = "designport.html";
})