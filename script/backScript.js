const backbut = document.querySelector('#back-container');
const logo = document.querySelector('#head-logo-img');
const portimg = document.querySelectorAll('.portimg');
const overlay = document.querySelector('body');




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

	if (imgEle.previousElementSibling !== null)
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

