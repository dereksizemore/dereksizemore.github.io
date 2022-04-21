/* Declarations */
const backbut = document.querySelector('#back-container');
const logo = document.querySelector('#head-logo-img');
const portimg = document.querySelectorAll('.portimg');
const overlay = document.querySelector('body')

/* Functions */

function featureImg (imgEle)
/* ?- featureImg Brings an overlay to the screen when a user      */
/*    clicks on an image inside a "imgport-container" with        */
/*    an Exit button, backward navigation, and forward navigation */
{
	/* Declarations */
	let div = document.createElement('div');
	let img = document.createElement('img');
	let p = document.createElement('p');

	/* Create a <div> with the id #focus-container and the class .no-hili */
	overlay.prepend(div);
	div.setAttribute('id', 'focus-container');
	div.setAttribute('class','no-hili');

	/* Prepend an <img> tag to #focus-container and give it the same */
	/* src as the clicked image and an id of #focus-img  */
	div.prepend(img);
	img.setAttribute('id', 'focus-img');
	img.setAttribute('src', imgEle.src);

	/* Prepend a <p> tag to #focus-container and give it the id #focusExit */
	div.prepend(p);
	p.setAttribute('id', 'focusExit');

	/* Add an X to the innerHTML */
	p.innerHTML = 'X';

	/* Add an event listener to remove the div when a user clicks the X */
	p.addEventListener('mouseup',event =>{
		div.remove();
	})
	/* If the nextElementSibling is another image, remove the current */
	/* #foucs-img and create a new one when a user clicks the '>'     */
	if (imgEle.nextElementSibling !== null)
	{
		/* Reset the focus to a new p element and prepend it to the  */
		/* <div> with an id of #next-arrow-p and innerHTML of '>'    */
		p = document.createElement('p');
		div.prepend(p);
		p.setAttribute('id','next-arrow-p');
		p.innerHTML = '>'

		/* When a user clicks '>' remove the current div */
		/* and create a new one with the next image      */
		p.addEventListener('mouseup',event =>{
			div.remove()
			featureImg(imgEle.nextElementSibling)
		})
	}

	/* If the previousElementSibling is another image, remove the current */
	/* #foucs-img and create a new one when a user clicks the '<'         */
	if (imgEle.previousElementSibling !== null)
	{
		/* Reset the focus to a new p element and prepend it to the  */
		/* <div> with an id of #next-arrow-p and innerHTML of '<'    */
		p = document.createElement('p');
		div.prepend(p);
		p.setAttribute('id','prev-arrow-p');
		p.innerHTML = '<'
		/* When a user clicks '<' remove the current div  */
		/* and create a new one with the next image       */
		p.addEventListener('mouseup',event =>{
			div.remove()
			featureImg(imgEle.previousElementSibling)
		})
	}
}


/* Add Overlay to page when user clicks an image */
portimg.forEach((item) =>{
	item.addEventListener('mouseup',event =>{
		featureImg(item);
	})
})

/* Return to main.html */
backbut.addEventListener('mouseup',event =>{
	location.href = "main.html"
})
/* Return to Splash Screen */
logo.addEventListener('mouseup',event =>{
	location.href = "index.html";
})