const backbut = document.querySelector('#back-container');
const logo = document.querySelector('#head-logo-img');
const portimg = document.querySelectorAll('.portimg');
const overlay = document.querySelector('body')
const div = document.createElement('div');
const img = document.createElement('img');
const p = document.createElement('p');

function featureImg (imgEle)
{
	overlay.prepend(div);
	div.setAttribute('id', 'focus-container');
	div.prepend(img);
	img.setAttribute('id', 'focus-img');
	img.setAttribute('src', imgEle.src);
	div.prepend(p)
	p.setAttribute('id', 'focusExit')
	p.innerHTML = 'X'
	p.addEventListener('mouseup',event =>{
		div.remove()
	})
}	

portimg.forEach((item) =>{
	item.addEventListener('mouseup',event =>{
		featureImg(item)
	})
})


backbut.addEventListener('mouseup',event =>{
	location.href = "main.html"
})
logo.addEventListener('mouseup',event =>{
	location.href = "index.html";
})