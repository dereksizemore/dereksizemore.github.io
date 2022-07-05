const backbut = document.querySelector('#back-container');
const logo = document.querySelector('#head-logo-img');
const portimg = document.querySelectorAll('.portimg');
const overlay = document.querySelector('body');
const oldweb1 = document.querySelector('#oldweb1');
const oldweb2 = document.querySelector('#oldweb2');
const oldweb3 = document.querySelector('#oldweb3');
const oldweb4 = document.querySelector('#oldweb4');
const toolbox1 = document.querySelector("#toolbox1");
const toolbox2 = document.querySelector("#toolbox2");
const toolbox3 = document.querySelector("#toolbox3");
const toolbox4 = document.querySelector("#toolbox4");
const toolbox5 = document.querySelector("#toolbox5");
const toolbox6 = document.querySelector("#toolbox6");
const toolbox7 = document.querySelector("#toolbox7");
const designport = document.querySelector('#designport');
const python = document.querySelector('#pythonport');
let webproject1 = document.querySelector('#webproject1');
let webproject1toggle = true;
const webproject2 = document.querySelector('#webproject2');
let webproject2toggle = true;
const webproject3 = document.querySelector('#webproject3');
let webproject3toggle = true;
const webproject4 = document.querySelector('#webproject4');
let webproject4toggle = true;
const webproject5 = document.querySelector('#webproject5');
let webproject5toggle = true;
const webproject6 = document.querySelector('#webproject6');
let webproject6toggle = true;
let weblearn1 = document.querySelector('#weblearn1');
let weblearn1toggle = true;
const weblearn2 = document.querySelector('#weblearn2');
let weblearn2toggle = true;
const weblearn3 = document.querySelector('#weblearn3');
let weblearn3toggle = true;
const weblearn4 = document.querySelector('#weblearn4');
let weblearn4toggle = true;
const weblearn5 = document.querySelector('#weblearn5');
let weblearn5toggle = true;
const weblearn6 = document.querySelector('#weblearn6');
let weblearn6toggle = true;


function changeIframe(ele,filesrc)
{
	ele.parentNode.parentNode.nextElementSibling.firstChild.nextElementSibling.src = filesrc;
}
function changeIframe2(ele,filesrc)
{
	ele.parentNode.parentNode.nextElementSibling.src = filesrc;
}

function changeIframeActive(ele)
{
	for (let i = 0; i < ele.parentNode.parentNode.children.length; i++)
	{
		if (ele.parentNode.parentNode.children[i].className === "iframe-nav-active")
		{
			ele.parentNode.parentNode.children[i].className = "iframe-nav";
		}
		ele.parentNode.className = "iframe-nav-active";

	}
}

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

backbut.addEventListener('mouseup',event =>{
	location.href = "../index.html"
})
logo.addEventListener('mouseup',event =>{
	location.href = "../index.html";
})

oldweb1.parentNode.addEventListener('mouseup',event =>{
	changeIframe(oldweb1,'../img/temple.jpg');
	changeIframeActive(oldweb1);
})
oldweb2.parentNode.addEventListener('mouseup',event =>{
	changeIframe(oldweb2,'../img/cpwhitetails.jpg');
	changeIframeActive(oldweb2);
})
oldweb3.parentNode.addEventListener('mouseup',event =>{
	changeIframe(oldweb3,'../img/dwp.jpg');
	changeIframeActive(oldweb3);
})
oldweb4.parentNode.addEventListener('mouseup',event =>{
	changeIframe(oldweb4,'../img/summerpalace.jpg');
	changeIframeActive(oldweb4);
})

toolbox1.parentNode.addEventListener('mouseup',event => {
	changeIframe2(toolbox1,'../img/toolbox1.jpg');
	changeIframeActive(toolbox1);
})
toolbox2.parentNode.addEventListener('mouseup',event => {
	changeIframe2(toolbox2,'../img/toolbox2.jpg');
	changeIframeActive(toolbox2);
})
toolbox3.parentNode.addEventListener('mouseup',event => {
	changeIframe2(toolbox3,'../img/toolbox3.jpg');
	changeIframeActive(toolbox3);
})
toolbox4.parentNode.addEventListener('mouseup',event => {
	changeIframe2(toolbox4,'../img/toolbox4.jpg');
	changeIframeActive(toolbox4);
})
toolbox5.parentNode.addEventListener('mouseup',event => {
	changeIframe2(toolbox5,'../img/toolbox5.jpg');
	changeIframeActive(toolbox5);
})
toolbox6.parentNode.addEventListener('mouseup',event => {
	changeIframe2(toolbox6,'../img/toolbox6.jpg');
	changeIframeActive(toolbox6);
})
toolbox7.parentNode.addEventListener('mouseup',event => {
	changeIframe2(toolbox7,'../img/toolbox7.jpg');
	changeIframeActive(toolbox7);
})
webproject6.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<p>I started working on Pua's Toolbox after a discussion I had with my wife and our business partner. The state of Oklahoma, along with OMMA, mandated an inventory tracking software called Metrc. For the most part, Metrc does it's job admirably and is easy to understand, but it isn't perfect. The biggest hole is invoicing. There simply isn't an invoicing option inside the software and the third party options, from talking to people using them, are overpriced and under featured. My extension changes that! With 3 clicks in my toolbox, it will pull dynamic, state-ful order and product data from the DOM and provide a user-friendly screen to add itemized pricing. One final click will have a well formatted and printer friendly invoice.</p>";
	webproject6toggle = dropdown(webproject6toggle,webproject6,list);
})
webproject6.addEventListener('mouseover',event =>{
	dropdownHoverOn(webproject6);
})
webproject6.addEventListener('mouseout',event =>{
	dropdownHoverOut(webproject6);
})

webproject1.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<p>This is a code-along React project I completed to learn React, State, and State-Management.</p>";
	webproject1toggle = dropdown(webproject1toggle,webproject1,list);
})
webproject1.addEventListener('mouseover',event =>{
	dropdownHoverOn(webproject1);
})
webproject1.addEventListener('mouseout',event =>{
	dropdownHoverOut(webproject1);
})

webproject2.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<p>This is the shop I set-up to experiment and learn more about shopify.</p>";
	webproject2toggle = dropdown(webproject2toggle,webproject2,list);
})
webproject2.addEventListener('mouseover',event =>{
	dropdownHoverOn(webproject2);
})
webproject2.addEventListener('mouseout',event =>{
	dropdownHoverOut(webproject2);
})

webproject3.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<p>This is a website I created for a cannabis clone and genetic preservation company. I started with blank text files and an old design I made using wordpress. I had no prior experience with Javascript before starting this project. I designed and created all logo and brand imaging for this website while working intimately with the ownership team.";
	webproject3toggle = dropdown(webproject3toggle,webproject3,list);
})
webproject3.addEventListener('mouseover',event =>{
	dropdownHoverOn(webproject3);
})
webproject3.addEventListener('mouseout',event =>{
	dropdownHoverOut(webproject3);
})

webproject4.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<p>This is a collection of websites I made after high school. Beijing Temple and Summer Palace were both made in my first year of college to help two fellow students with projects they were working on. Circle P Whitetails is the first website I ever sold. Derek's Web Page was the website I used to advertise myself and my website business.</p>";
	webproject4toggle = dropdown(webproject4toggle,webproject4,list);
})
webproject4.addEventListener('mouseover',event =>{
	dropdownHoverOn(webproject4);
})
webproject4.addEventListener('mouseout',event =>{
	dropdownHoverOut(webproject4);
})

webproject5.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<p>This is the last version of the first HTML website I made. It was a blog, lifestyle webpage, and community that was going to take over the interenet... or so I thought.</p>";
	webproject5toggle = dropdown(webproject5toggle,webproject5,list);
})
webproject5.addEventListener('mouseover',event =>{
	dropdownHoverOn(webproject5);
})
webproject5.addEventListener('mouseout',event =>{
	dropdownHoverOut(webproject5);
})

weblearn6.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li>#Chrome API</li><li>#Runtime Messages</li><li>#Unit Testing</li><li>#Mutation Observers</li>";
	weblearn6toggle = dropdown(weblearn6toggle,weblearn6,list);
})
weblearn6.addEventListener('mouseover',event =>{
	dropdownHoverOn(weblearn6);
})
weblearn6.addEventListener('mouseout',event =>{
	dropdownHoverOut(weblearn6);
})

weblearn1.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li>#JSX</li><li>#node.js</li><li>#React</li><li>#State</li><li>#State-Management</li>";
	weblearn1toggle = dropdown(weblearn1toggle,weblearn1,list);
})
weblearn1.addEventListener('mouseover',event =>{
	dropdownHoverOn(weblearn1);
})
weblearn1.addEventListener('mouseout',event =>{
	dropdownHoverOut(weblearn1);
})

weblearn2.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li>#.liquid File Extension</li><li>#Liquid Logic</li><li>#Liquid Templating</li><li>#Shopify Pagebuilder</li><li>#Shopify</li><li>#Shopify Product Creation</li>";
	weblearn2toggle = dropdown(weblearn2toggle,weblearn2,list);
})
weblearn2.addEventListener('mouseover',event =>{
	dropdownHoverOn(weblearn2);
})
weblearn2.addEventListener('mouseout',event =>{
	dropdownHoverOut(weblearn2);
})

weblearn3.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li>#DOM Control</li><li>#Javascript</li><li>#jQuery</li><li>#node.js</li><li>#State Management</li><li>#Working With An Owner Group</li>";
	weblearn3toggle = dropdown(weblearn3toggle,weblearn3,list);
})
weblearn3.addEventListener('mouseover',event =>{
	dropdownHoverOn(weblearn3);
})
weblearn3.addEventListener('mouseout',event =>{
	dropdownHoverOut(weblearn3);
})

weblearn4.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li>#Display Optimization</li><li>#Templating</li><li>#Web Design Principles</li>";
	weblearn4toggle = dropdown(weblearn4toggle,weblearn4,list);
})
weblearn4.addEventListener('mouseover',event =>{
	dropdownHoverOn(weblearn4);
})
weblearn4.addEventListener('mouseout',event =>{
	dropdownHoverOut(weblearn4);
})

weblearn5.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li>#HTML</li><li>#Inline Styling</li>";
	weblearn5toggle = dropdown(weblearn5toggle,weblearn5,list);
})
weblearn5.addEventListener('mouseover',event =>{
	dropdownHoverOn(weblearn5);
})
weblearn5.addEventListener('mouseout',event =>{
	dropdownHoverOut(weblearn5);
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

pythonport.addEventListener('mouseup',event =>{
	location.href = "pythonport.html";
})

designport.addEventListener('mouseup',event =>{
	location.href = "designport.html";
})