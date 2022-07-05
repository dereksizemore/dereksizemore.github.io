const backbut = document.querySelector('#back-container');
const logo = document.querySelector('#head-logo-img');
const portimg = document.querySelectorAll('.portimg');
const overlay = document.querySelector('body');
const webport = document.querySelector('#webport');
const designport = document.querySelector('#designport');
const pyproject1 = document.querySelector('#pyproject1');
let pyproject1toggle = true;
const pyproject2 = document.querySelector('#pyproject2');
let pyproject2toggle = true;
const pyproject3 = document.querySelector('#pyproject3');
let pyproject3toggle = true;
const pyproject4 = document.querySelector('#pyproject4');
let pyproject4toggle = true;
const pyproject5 = document.querySelector('#pyproject5');
let pyproject5toggle = true;
const pyproject6 = document.querySelector('#pyproject6');
let pyproject6toggle = true;
const pyproject7 = document.querySelector('#pyproject7');
let pyproject7toggle = true;
const pylearn1 = document.querySelector('#pylearn1');
let pylearn1toggle = true;
const pylearn2 = document.querySelector('#pylearn2');
let pylearn2toggle = true;
const pylearn3 = document.querySelector('#pylearn3');
let pylearn3toggle = true;
const pylearn4 = document.querySelector('#pylearn4');
let pylearn4toggle = true;
const pylearn5 = document.querySelector('#pylearn5');
let pylearn5toggle = true;
const pylearn6 = document.querySelector('#pylearn6');
let pylearn6toggle = true;
const pylearn7 = document.querySelector('#pylearn7');
let pylearn7toggle = true;
const fbpy1 = document.querySelector("#fbpy1");
const fbpy2 = document.querySelector('#fbpy2');
const fbpy3 = document.querySelector('#fbpy3');
const fbpy4 = document.querySelector('#fbpy4');
const oldweb1 = document.querySelector('#oldweb1');
const oldweb2 = document.querySelector('#oldweb2');
const oldweb3 = document.querySelector('#oldweb3');
const oldweb4 = document.querySelector('#oldweb4');

function changeIframe(ele,filesrc)
{
	ele.parentNode.parentNode.nextElementSibling.firstChild.nextElementSibling.src = filesrc;
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

fbpy1.parentNode.addEventListener('mouseup',event =>{
	changeIframe(fbpy1,'ccstreampy.html');
	changeIframeActive(fbpy1);
})
fbpy2.parentNode.addEventListener('mouseup',event =>{
	changeIframe(fbpy2,'fibo-1.0py.html');
	changeIframeActive(fbpy2);
})
fbpy3.parentNode.addEventListener('mouseup',event =>{
	changeIframe(fbpy3,'finnstreampy.html');
	changeIframeActive(fbpy3);
})
fbpy4.parentNode.addEventListener('mouseup',event =>{
	changeIframe(fbpy4,'toolspy.html');
	changeIframeActive(fbpy4);
})

pyproject1.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<p>I started this project to reverse engineer a stock indicator that I regularly use. In it's current state it will take input from a file containing historical price data for a security or cryptocurrency and output 5 numbers: a 100 data point weighted moving average with 2 higher numbers and 2 lower numbers determined by user defined math functions and Fibonacci numbers.</p>";
	pyproject1toggle = dropdown(pyproject1toggle,pyproject1,list);
})
pyproject1.addEventListener('mouseover',event =>{
	dropdownHoverOn(pyproject1);
})
pyproject1.addEventListener('mouseout',event =>{
	dropdownHoverOut(pyproject1);
})

pyproject2.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<p>This project crawls finance.yahoo.com with BeautifulSoup and Requests and extracts option chain data. It takes the data and does math to some of it, connects to the Google Sheets API, and populates a spreadsheet with the data from the math and option chain.</p>";
	pyproject2toggle = dropdown(pyproject2toggle,pyproject2,list);
})
pyproject2.addEventListener('mouseover',event =>{
	dropdownHoverOn(pyproject2);
})
pyproject2.addEventListener('mouseout',event =>{
	dropdownHoverOut(pyproject2);
})

pyproject3.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<p>This project takes an input (stock symbols) from the user and then crawls locally stored text files of bi-monthly failed to deliver security data by the SEC. It then creates a file and extracts the data from the SEC release into a readable and organized file.</p>";
	pyproject3toggle = dropdown(pyproject3toggle,pyproject3,list);
})
pyproject3.addEventListener('mouseover',event =>{
	dropdownHoverOn(pyproject3);
})
pyproject3.addEventListener('mouseout',event =>{
	dropdownHoverOut(pyproject3);
})

pyproject4.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<p>This project takes data from quarterly 13-f releases and extracts 4 columns of data from one of the tables inside. It writes that data to a text file to be handled later.</p>";
	pyproject4toggle = dropdown(pyproject4toggle,pyproject4,list);
})
pyproject4.addEventListener('mouseover',event =>{
	dropdownHoverOn(pyproject4);
})
pyproject4.addEventListener('mouseout',event =>{
	dropdownHoverOut(pyproject4);
})

pyproject5.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "</p>This project walks a file directory in the OS to find all of the text files from each player and their stats and puts them in a list. The list is converted into a pandas dataframe which sorts and organizes the players and data. It then outputs a CSV with the combined data.</p>";
	pyproject5toggle = dropdown(pyproject5toggle,pyproject5,list);
})
pyproject5.addEventListener('mouseover',event =>{
	dropdownHoverOn(pyproject5);
})
pyproject5.addEventListener('mouseout',event =>{
	dropdownHoverOut(pyproject5);
})

pyproject6.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<p>This project is the second python script I wrote. I was given the option of following a code along or starting from scratch. I went in blind and finished the project with added input sanitizers. I learend a valuable lesson about version management when I tried to add true splitting up to 4 times and I broke the dealer AI. This project needs re-worked before it is working again.</p>";
	pyproject6toggle = dropdown(pyproject6toggle,pyproject6,list);
})
pyproject6.addEventListener('mouseover',event =>{
	dropdownHoverOn(pyproject6);
})
pyproject6.addEventListener('mouseout',event =>{
	dropdownHoverOut(pyproject6);
})

pyproject7.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<p>This project was a code along with the bootcamp I used to learn python. It was my first real script.";
	pyproject7toggle = dropdown(pyproject7toggle,pyproject7,list);
})
pyproject7.addEventListener('mouseover',event =>{
	dropdownHoverOn(pyproject7);
})
pyproject7.addEventListener('mouseout',event =>{
	dropdownHoverOut(pyproject7);
})

pylearn1.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li># Async Functions</li><li># JSON</li><li># Separating Functions</li><li># Sockets</li>";
	pylearn1toggle = dropdown(pylearn1toggle,pylearn1,list);
})
pylearn1.addEventListener('mouseover',event =>{
	dropdownHoverOn(pylearn1);
})
pylearn1.addEventListener('mouseout',event =>{
	dropdownHoverOut(pylearn1);
})

pylearn2.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li># Data Management</li><li># G-Suite API</li>";
	pylearn2toggle = dropdown(pylearn2toggle,pylearn2,list);
})
pylearn2.addEventListener('mouseover',event =>{
	dropdownHoverOn(pylearn2);
})
pylearn2.addEventListener('mouseout',event =>{
	dropdownHoverOut(pylearn2);
})

pylearn3.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li># Data Organization</li>";
	pylearn3toggle = dropdown(pylearn3toggle,pylearn3,list);
})
pylearn3.addEventListener('mouseover',event =>{
	dropdownHoverOn(pylearn3);
})
pylearn3.addEventListener('mouseout',event =>{
	dropdownHoverOut(pylearn3);
})

pylearn4.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li># BeautifulSoup Package</li><li># SEC Edgar System</li><li># Selenium Package</li>";
	pylearn4toggle = dropdown(pylearn4toggle,pylearn4,list);
})
pylearn4.addEventListener('mouseover',event =>{
	dropdownHoverOn(pylearn4);
})
pylearn4.addEventListener('mouseout',event =>{
	dropdownHoverOut(pylearn4);
})

pylearn5.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li># Dataframes</li><li># numpy Package</li><li># os Package</li><li># pandas Package</li>";
	pylearn5toggle = dropdown(pylearn5toggle,pylearn5,list);
})
pylearn5.addEventListener('mouseover',event =>{
	dropdownHoverOn(pylearn5);
})
pylearn5.addEventListener('mouseout',event =>{
	dropdownHoverOut(pylearn5);
})

pylearn6.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li># Game State</li><li># Nested Loops</li><li># Objects</li><li># Version Management</li>";
	pylearn6toggle = dropdown(pylearn6toggle,pylearn6,list);
})
pylearn6.addEventListener('mouseover',event =>{
	dropdownHoverOn(pylearn6);
})
pylearn6.addEventListener('mouseout',event =>{
	dropdownHoverOut(pylearn6);
})

pylearn7.firstChild.nextElementSibling.addEventListener('mouseup',event =>{
	const list = "<li># Python 3.7</li>";
	pylearn7toggle = dropdown(pylearn7toggle,pylearn7,list);
})
pylearn7.addEventListener('mouseover',event =>{
	dropdownHoverOn(pylearn7);
})
pylearn7.addEventListener('mouseout',event =>{
	dropdownHoverOut(pylearn7);
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

designport.addEventListener('mouseup',event =>{
	location.href = "designport.html";
})