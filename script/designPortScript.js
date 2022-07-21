const backbut = document.querySelector('#back-container');
const logo = document.querySelector('#head-logo-img');
const portimg = document.querySelectorAll('.portimg');
const overlay = document.querySelector('body');
const webport = document.querySelector('#webport');
const python = document.querySelector('#pythonport');

function featureImg (imgEle)
{
	let div = document.createElement('div');
	let img = document.createElement('img');
	let p = document.createElement('p');

	overlay.prepend(div);
	div.setAttribute('id', 'focus-container');
	div.setAttribute('class','no-hili');
	div.prepend(img);

	img.setAttribute('id', 'focus-img');
	img.setAttribute('src', imgEle.src);

	div.prepend(p);
	p.setAttribute('id', 'focusExit');
	p.innerHTML = 'X';

	p.addEventListener('mouseup',event =>{
		div.remove();
	})
	if (imgEle.nextElementSibling !== null)
	{
		p = document.createElement('p');
		div.prepend(p);
		p.setAttribute('id','next-arrow-p');
		p.innerHTML = '>'
		p.addEventListener('mouseup',event =>{
			div.remove()
			featureImg(imgEle.nextElementSibling)
		})
	}

	if (imgEle.previousElementSibling.tagName !== "P")
	{
		p = document.createElement('p');
		div.prepend(p);
		p.setAttribute('id','prev-arrow-p');
		p.innerHTML = '<'
		p.addEventListener('mouseup',event =>{
			div.remove()
			featureImg(imgEle.previousElementSibling)
		})
	}
}




portimg.forEach((item) =>{
	item.addEventListener('mouseup',event =>{
		overDiv = featureImg(item);
	})
})


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

webport.addEventListener('mouseup',event =>{
	location.href = "webport.html"
})

pythonport.addEventListener('mouseup',event =>{
	location.href = "pythonport.html";
})