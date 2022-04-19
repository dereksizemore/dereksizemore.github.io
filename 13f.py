from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import requests
import time
from bs4 import BeautifulSoup

goon = True
linklist = ['']
linklist2 = ['']
sharelist = ['']
sharelist2 = ['','Company:', 'Symbol','Shares','Control']

def company():
	cname = list(input("Company Name:"))
	cdate = list(input("\n Type in a specific year or add (+) to go get all years up to that year. \n \n   (Example: An input of '2008' will return all reports for the year 2008. An input of '+2008' will return all reports from the most recent to the first report of 2008) \n\nFormat (YYYY) or (+YYYY): "))
	compname = ''
	output = ['']
	compname = compname.join(addplus(cname))
	url = "https://sec.report/Document/Header/?company=" + compname + "&formType=13F-HR#results"
	output.append(str(''.join(killplus(cname))))
	output.pop(0)
	output.append(url)
	output.append(cdate)
	output.append(cname)
	return output

def addplus(iput):
	b = 0
	for a in iput:
		if a == ' ':
			iput[b] = '+'
		b += 1
	return iput

def killplus(iput):
	b = 0
	for a in iput:
		if a == '+':
			iput[b] = ''
		b += 1
	return iput	

def convertreports(iput):
	b = 0
	for a in iput:
		blist = str(iput[b])
		clist = list(blist)
		if clist[4] == '2' and clist[5] == '0':
			tstring1 = ''.join(clist[4:-5])
			linklist.append(tstring1)
		elif len(clist) > 14 and clist[14] == 'D':
			tstring2 = ''.join(clist[13:44])
			linklist.append(tstring2)
		b += 1

def extractreports(iput):
	#--iput is outlist[2] - the user input date--#
	iputdate = list(iput)
	if iputdate[0] == '+':
		cdate = int(iputdate[3] + iputdate[4])
		for i in range(len(linklist)):
			if len(linklist) > 3:
				crepdate = list(linklist[2])
				repdate = int(crepdate[2] + crepdate[3])
				#-- | cdate | last 2 digits of user input date |--#--|repdate | the last 2 digits of the current item in the SEC linklist --#
				if cdate <= repdate:
					linklist2.append(linklist[1])
					linklist2.append(linklist[2])
					linklist.pop(1)
					linklist.pop(1)
	else:
		#--iput is outlist[2] - the user input date--#
		cdate = int(iputdate[2] + iputdate[3])
		for i in range(len(linklist)):
			if len(linklist) > 3:
				crepdate = list(linklist[2])
				repdate = int(crepdate[2] + crepdate[3])
				#-- | cdate | last 2 digits of user input date |--#--|repdate | the last 2 digits of the current item in the SEC linklist --#	
				if cdate == repdate:
					linklist2.append(linklist[1])
					linklist2.append(linklist[2])
					linklist.pop(1)
					linklist.pop(1)
				else:
					linklist.pop(1)
					linklist.pop(1)
	return int(((len(linklist2) - 1) / 2))

def getreports():
	tempt = 1
	websearch = True
	while websearch == True:
		driver = webdriver.Firefox()
		driver.get(outlist[1])
		xfer = driver.page_source

		soup = BeautifulSoup(xfer, 'html.parser')

		#-- Get form links and store them in a list --#
		tabledef = soup.find_all('td')
		if outlist[0].lower() == 'blackrockinc':
			for i in range(131):
				tabledef.pop(0)
		elif outlist[0].lower() =='fidelitynational':
			for i in range(21):
				tabledef.pop(0)
		driver.close()
		convertreports(tabledef)
		if len(linklist) > 1:
			websearch = False
			print('Report list populated...')
			return True
		else:
			print('Your request TIMED OUT or the company does not exist. Search attempt ' + str(tempt) + ' of 5')
			print(outlist[1])
			tempt += 1
			if tempt > 5:
				sv1 = ''.join(outlist[3])
				print("\n\n################# \nNo data gathered.\n#################\n\nYour request has TIMED OUT too many times or there isn't an instance of " + sv1 + " in the SEC database. \n\n Re-run this script with a different company name or copy: " + outlist[1] + "into a browser to confirm a TIMEOUT.")
				websearch = False
				return False

def searchreports():
	url = 'https://sec.report' + linklist2[1]
	driver = webdriver.Firefox()
	driver.get(url)
	xfer = driver.page_source
	soup = BeautifulSoup(xfer, 'html.parser')
	for small in soup("small"):
		small.decompose()
	tabledef = soup.find_all('td')
	driver.close()
	for a in range(len(tabledef)):
		if str(tabledef[a]) == '<td class="FormTextR">COLUMN 7</td>':
			tdef = str(tabledef[a])
			convertshare = tabledef[a + 21:]
			return convertshare
	convertshare = tabledef[12:-25]
	print('Converting list...')
	return convertshare

def sharetable(iput):
	if str(iput[0]) == '<td class="FormTextR">SOLE</td>':
		iput.pop(0)
		iput.pop(0)
		iput.pop(0)
		for a in range(0,len(iput),12):
			if a < (len(iput) - 4):
				sharelist.append(iput[a])
				sharelist.append(iput[a + 4])
				sharelist.append(iput[a + 7])
		return None
	for a in range(0,len(iput),6):
		if a < (len(iput) - 4):
			sharelist.append(iput[a])
			sharelist.append(iput[a + 1])
			sharelist.append(iput[a + 3])
			sharelist.append(iput[a + 4])

def grabsymbol(iput):
	for i in range(6,len(iput),4):
			url ="https://quotes.fidelity.com/mmnet/SymLookup.phtml?reqforlookup=REQUESTFORLOOKUP&productid=mmnet&isLoggedIn=mmnet&rows=50&for=stock&by=cusip&criteria=" + str(sharelist2[i]) + "&submit=Search"
			xfer = requests.get(url)
			soup = BeautifulSoup(xfer.content, 'html.parser')
			tables = soup.find_all('a')
			nosym = list(tables[6])
			iput[i] = str(nosym)
	return iput

def pulltags():
	for a in range(1,(len(sharelist)),1):
		clist = list(sharelist[a])
		clist2 = str(clist)
		clist3 = list(clist2)
		clist4 = ''.join(clist3[2:-2])
		sharelist2.append(clist4)	

def writfil(cname):
	company = cname + '-' + linklist2[2]
	txt = open(company, 'w')
	txt.write(cname + ' | ' + linklist2[2] + '\n')
	for i in range(1,len(sharelist2),1):
		if (i % 4) == 0:
			tstring = str(sharelist2[i])
			txt.write(tstring)
			txt.write('\n')
		else:
			txt.write(str(sharelist2[i]))
			txt.write(' | ')
	txt.close()
	linklist2.pop(1)
	linklist2.pop(1)



#-#-#-#-#-#-#______START LOGIC______#-#-#-#-#-#

#-- ASK FOR COMPANY NAME --#
outlist = company()

#-- Search SEC site for doc-table or quit after 5 timeouts --#
goon = getreports()

#-- determine needed reports --#
if goon == True:
	reportcount = extractreports(outlist[2])
	if reportcount == 0:
		print('No Reports Found')
#-- Get share data from forms--#
while reportcount > 0:
	shares = searchreports()
#-- Manipulate Data --#
	sharetable(shares)
	pulltags()
	sharelist2 = grabsymbol(sharelist2)

#---Write to text file---#
	print('Writing to file...')
	writfil(outlist[0])
	print('DONE')
#-- Reset Variables for next file --#
	sharelist = ['']
	sharelist2 = ['','Company:','Symbol','Shares','Control']
	reportcount -= 1