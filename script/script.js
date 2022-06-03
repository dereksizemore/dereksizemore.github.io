const fgBodyC2 = document.querySelector('#fg-body-c2');
const loadScript = document.createElement('script');
const about = document.querySelector('#about');
const webport = document.querySelector('#webport');
const designport = document.querySelector('#designport');
const python = document.querySelector('#pythonport');
const scroll = document.querySelector('#sub-title-scroll');
const h1 = document.querySelector('#text-head-main');
const resume = document.querySelector('#resume');
const drop1 = document.querySelector('#drop1');
let drop1toggle = true;
const drop2 = document.querySelector('#drop2');
let drop2toggle = true;
const drop3 = document.querySelector('#drop3');
let drop3toggle = true;
const drop4 = document.querySelector('#drop4');
let drop4toggle = true;

function dropdown(toggle,id,list)
{
	if (toggle === true)
	{
		const div = document.createElement('div');
		const ul = document.createElement('ul');


		div.setAttribute('class', 'dropdown-sub');
		div.classList.add("no-hili");
		ul.setAttribute('class', 'dropdown-text-li');

		ul.innerHTML = list;

		id.firstChild.nextElementSibling.firstChild.nextElementSibling.nextElementSibling.innerHTML = "&#8673;&nbsp;";
		id.appendChild(div);
		div.appendChild(ul);
		return false;
	}
	else
	{
		id.firstChild.nextElementSibling.firstChild.nextElementSibling.nextElementSibling.innerHTML = "&#8675;&nbsp;";
		document.querySelector('.dropdown-sub').remove();
		return true;
	}
}

function dropdownHoverOn(id){
	id.firstChild.nextElementSibling.firstChild.nextElementSibling.nextElementSibling.classList.remove("dropdown-text-arrow");
	id.firstChild.nextElementSibling.firstChild.nextElementSibling.nextElementSibling.classList.add("dropdown-text-arrow-hover");
}
function dropdownHoverOut(id){
	id.firstChild.nextElementSibling.firstChild.nextElementSibling.nextElementSibling.classList.remove("dropdown-text-arrow-hover");
	id.firstChild.nextElementSibling.firstChild.nextElementSibling.nextElementSibling.classList.add("dropdown-text-arrow");
}

about.addEventListener('mouseover',event =>{
	about.firstChild.nextElementSibling.classList.add('dark')
	about.firstChild.nextElementSibling.nextElementSibling.setAttribute('id','over');
})
about.addEventListener('mouseleave',event =>{
	about.firstChild.nextElementSibling.classList.remove('class', 'dark')
	about.firstChild.nextElementSibling.nextElementSibling.removeAttribute('id','over');
})

about.addEventListener('mouseup',event =>{
	location.href = "html/about.html"
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
	location.href = "html/webport.html"
})

pythonport.addEventListener('mouseup',event =>{
	location.href = "html/pythonport.html";
})

designport.addEventListener('mouseup',event =>{
	location.href = "html/designport.html";
})

resume.addEventListener('mouseup',event =>{
	alert("######################\nDOWNLOAD INSTRUCTIONS\n######################\n This link will take you to the most up to date version of my resume on docs.google.com.\n\n To download it in the format that is most convenient for you, simply click 'File' in the menu bar of the new window that opens and then navigate to 'download'.")
})

drop1.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li>HTML5</li><li>CSS</li><li>Javascript (ES6)</li><li>Python 3.7</li><li>Git</li><li>GitHub</li><li>Shopify</li><li>Wordpress</li>";
	drop1toggle = dropdown(drop1toggle,drop1,list);
})
drop1.addEventListener('mouseover',event =>{
	dropdownHoverOn(drop1);
})
drop1.addEventListener('mouseout',event =>{
	dropdownHoverOut(drop1);
})

drop2.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li>Adobe Illustrator</li><li>Adobe Photoshop</li><li>Apparel Design</li>"
	drop2toggle = dropdown(drop2toggle,drop2,list);
})
drop2.addEventListener('mouseover',event =>{
	dropdownHoverOn(drop2);
})
drop2.addEventListener('mouseout',event =>{
	dropdownHoverOut(drop2);
})

drop3.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li>Creative Writing</li><li>Customer Service</li><li>Google Search</li><li>Interpersonal & Written Communication</li><li>Product Presentation</li><li>Sales</li><li>Software Training</li><li>UI/UX Design</li>";
	drop3toggle = dropdown(drop3toggle,drop3,list);
})
drop3.addEventListener('mouseover',event =>{
	dropdownHoverOn(drop3);
})
drop3.addEventListener('mouseout',event =>{
	dropdownHoverOut(drop3);
})

drop4.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li>Adaptable</li><li>Attention To Detail</li><li>Determined</li><li>High Learning Agility</li><li>Persistent</li><li>Self-Motivated</li>"
	drop4toggle = dropdown(drop4toggle,drop4,list);
})
drop4.addEventListener('mouseover',event =>{
	dropdownHoverOn(drop4);
})
drop4.addEventListener('mouseout',event =>{
	dropdownHoverOut(drop4);
})

$("#sub-title-scroll").click(function() {
	$('html, body').animate({
		scrollTop: $("#text-head-main").offset().top
	},1350);
});