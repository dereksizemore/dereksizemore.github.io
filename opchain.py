from bs4 import BeautifulSoup
import urllib.request
import pygsheets
import pandas as pd
import calendar
from datetime import date
import time
import statistics

# -- link creditials -- #
gc = pygsheets.authorize(service_file='D:/PYTON/Stock/opchain/cred.json')
# -------- setup panda dataframe ----- #
df = pd.DataFrame()

# -- DECLARATIONS -- #
alpha = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
clist = ['']
plist = ['']
prlist = ['']
highlolist = ['']

# -- FUNCTIONS -- #
def grabdata(ticker):
	outlist = ['']
	urla = 'https://query1.finance.yahoo.com/v7/finance/download/'
	urlb = '&interval=1d&events=history&includeAdjustedClose=true'

	today = date.today()
	todayx = today.strftime("%Y-%m-%d")
	unidate = calendar.timegm(time.strptime(todayx + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))

	urldate = '?period1=' + str(unidate - (31536000 * 5)) + '&period2=' + str(unidate)

	source = urllib.request.urlopen(urla + ticker + urldate + urlb).read()
	soup = BeautifulSoup(source, 'html.parser')
	prelist = ','.join(str(soup).split('\n'))
	outlist = prelist.split(',')
	for i in range(7):
		outlist.pop(0)
	outlist.reverse()
	return outlist

def fivdavg(pdata):
	outlist = ['']
	fivdavg = 0.0
	for i in range (2,5 * 7,7):
		outlist.append(float(pdata[i]))
	outlist.pop(0)
	out = statistics.mean(outlist)
	return out

def npricelist(n5):
	n30 = (float(n5) - float(highlolist[2]))/(float(highlolist[1])-float(highlolist[2]))
	n6m = (float(n5) - float(highlolist[4]))/(float(highlolist[3])-float(highlolist[4]))
	n1y = (float(n5) - float(highlolist[6]))/(float(highlolist[5])-float(highlolist[6]))
	wks.update_value('o2', n30)
	wks.update_value('o3', n6m)
	wks.update_value('o4', n1y)	

def get52wavg(data):
	outlist = ['']
	ftwavg = 0.0
	for i in range(2,365 * 7,7):
		outlist.append(data[i])
	outlist.pop(0)
	for i in outlist:
		ftwavg += float(i)
	highlolist.append(max(outlist))
	highlolist.append(min(outlist))
	return ftwavg/365

def getsixavg(data):
	outlist = ['']
	sixmavg = 0.0
	for i in range (2,int((365/2)) * 7, 7):
		outlist.append(data[i])
	outlist.pop(0)
	for i in outlist:
		sixmavg += float(i)
	highlolist.append(max(outlist))
	highlolist.append(min(outlist))
	return sixmavg/(365/2)

def get30davg(data):
	outlist = ['']
	thdavg = 0.0
	for i in range (2,30 * 7,7):
		outlist.append(data[i])
	outlist.pop(0)
	for i in outlist:
		thdavg += float(i)
	highlolist.append(max(outlist))
	highlolist.append(min(outlist))
	return thdavg/30

def get2yvol(data):
	outlist = ['']
	for i in range (7,(365*2) * 7,7):
		outlist.append(data[i])
	outlist.pop(0)
	return outlist

def fillhead():
	wks.update_value('b1', ticker)
	wks.update_value('c1', prlist[1])
	wks.update_value('b4', expy)
	wks.update_value('e2', str("%.2f" % thdavg))
	wks.update_value('e3', str("%.2f" % sixmavg))
	wks.update_value('e4', str("%.2f" % ftwavg))
	wks.update_value('g2', str("%.2f" % float(highlolist[1])))
	wks.update_value('i2', str("%.2f" % float(highlolist[2])))
	wks.update_value('g3', str("%.2f" % float(highlolist[3])))
	wks.update_value('i3', str("%.2f" % float(highlolist[4])))
	wks.update_value('g4', str("%.2f" % float(highlolist[5])))
	wks.update_value('i4', str("%.2f" % float(highlolist[6])))

def volume(voldata):
	vol1yli = ['']
	vol6mli = ['']
	vol90li = ['']
	vol30li = ['']
	for i in range(len(vollist)):
		vol1yli.append(int(vollist[i]))
		if i <= 30:
			vol30li.append(int(vollist[i]))
		if i <= 90 :
			vol90li.append(int(vollist[i]))
		if i <= (365/2):
			vol6mli.append(int(vollist[i]))
	vol5li = [int(vollist[0]),int(vollist[1]),int(vollist[2]),int(vollist[3]),int(vollist[4])]
	vol30li.pop(0)
	vol90li.pop(0)
	vol6mli.pop(0)
	vol1yli.pop(0)

	vavg5 = int(statistics.mean(vol5li))
	vavg30 = int(statistics.mean(vol30li))
	vavg90 = int(statistics.mean(vol90li))
	vavg6m = int(statistics.mean(vol6mli))
	vavg1y = int(statistics.mean(vol1yli))

	nv5 = (int(vavg5) - min(vol5li))/(max(vol5li)-min(vol5li))
	nv30 = (int(vavg5) - min(vol30li))/(max(vol30li)-min(vol30li))
	nv90 = (int(vavg5) - min(vol90li))/(max(vol90li)-min(vol90li))
	nv6m = (int(vavg5) - min(vol6mli))/(max(vol6mli)-min(vol6mli))
	nv1y = (int(vavg5) - min(vol1yli))/(max(vol1yli)-min(vol1yli))
	wks.update_value('q2', nv5)
	wks.update_value('q3', nv30)
	wks.update_value('q4', nv90)
	wks.update_value('s2', nv6m)
	wks.update_value('s3', nv1y)
	wks.update_value('k2', vavg5)
	wks.update_value('k3', vavg30)
	wks.update_value('k4', vavg90)
	wks.update_value('m2', vavg6m)
	wks.update_value('m3', vavg1y)

def buildchain():	
	# -- Convert date from epoch for URL -- #
	unidate = calendar.timegm(time.strptime(expy + ' 00:00:00', '%Y-%m-%d %H:%M:%S'))

	# -- Crawl Yahoo Finance with Beautiful Soup -- #
	source = urllib.request.urlopen('http://finance.yahoo.com/quote/' + ticker + '/options?date=' + str(unidate) + '&p=' + ticker).read()
	# -- Make Soup -- #
	soup = BeautifulSoup(source, 'html.parser')

	# -- Organize Soup -- #
	calls = soup.find('table', attrs={"class": "calls W(100%) Pos(r) Bd(0) Pt(0) list-options"})
	puts = soup.find('table', attrs={"class": "puts W(100%) Pos(r) list-options"})
	price = soup.find('span', attrs={"class" : "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})

	# -- Get price data from HTML soup -- #
	for string in price.stripped_strings:
		prlist.append(string)
	
	# -- Get call table from HTML soup -- #
	for string in calls.stripped_strings:
		clist.append(string.replace(',','').replace('-','0'))

	# -- Get Put data from HTML soup -- #
	for string in puts.stripped_strings:
		plist.append(string.replace(',','').replace('-','0'))
	# -- Clear header row from tables -- #
	for i in range(12):
		plist.pop(0)
		clist.pop(0)

	fillhead()
	volume(vollist)
	npricelist(fivdavg(priceinfo))

	x = 6
	a = 2
	# -- Strike Price -- #
	for i in range(2,len(clist),11):
		if int(clist[i + 7]) > 0:
			wks.update_value(alpha[a] + str(x), clist[i])
			x += 16
	x = 7
	# -- Last sold price -- #
	for i in range(3,len(clist),11):
		if int(clist[i + 6]) > 0:
			wks.update_value(alpha[a] + str(x), clist[i])
			x += 16
	x = 8
	# -- Volume -- #
	for i in range(8,len(clist),11):
		if int(clist[1 + i]) > 0:
			wks.update_value(alpha[a] + str(x), clist[i])
			x += 16
	# -- Open interest -- #
	x = 9
	for i in range(9,len(clist),11):
		if int(clist[i]) > 0:
			wks.update_value(alpha[a] + str(x), clist[i])
			x += 16

	# -- extract put data from list to sheet -- #
	x = 15
	a = 4
	b = 1
	c = 1
	d = 1
	e = 1
	for j in range (1, len(clist),11):
		for i in range (2,len(plist),11):
			if int(plist[7 + i]) > 0:
				if a > 26:
					a = 1
					wks.update_value(alpha[a] + alpha[b] + str(x), plist[i])
					b += 1
				elif e > 1:
					wks.update_value(alpha[d] + alpha[e] + str(x), plist[i])
				elif d > 26:
					d = 1
					wks.update_value(alpha[d] + alpha[e] + str(x), plist[i])
					e += 1
				elif d > 1:
					wks.update_value(alpha[c] + alpha[d] + str(x), plist[i])
					d += 1
				elif c > 26:
					c = 1
					wks.update_value(alpha[c] + alpha[d] + str(x), plist[i])
					d += 1
				elif c > 1:
					wks.update_value(alpha[b] + alpha[c] + str(x), plist[i])
					c += 1	
				elif b > 26:
					b = 1
					wks.update_value(alpha[b] + alpha[c] + str(x), plist[i])
					c += 1
				elif b > 1:
					wks.update_value(alpha[a] + alpha[b] + str(x), plist[i])
					b += 1
				else:
					wks.update_value(alpha[a] + str(x), plist[i])
					a += 1 
		x += 16
		a = 4
		b = 1
		c = 1
		d = 1
		e = 1	
	x = 16
	a = 4
	b = 1
	c = 1
	d = 1
	e = 1
	for j in range (1, len(clist),11):
		for i in range (3,len(plist),11):
			if int(plist[6 + i]) > 0:
				if a > 26:
					a = 1
					wks.update_value(alpha[a] + alpha[b] + str(x), plist[i])
					b += 1
				elif e > 1:
					wks.update_value(alpha[d] + alpha[e] + str(x), plist[i])
				elif d > 26:
					d = 1
					wks.update_value(alpha[d] + alpha[e] + str(x), plist[i])
					e += 1
				elif d > 1:
					wks.update_value(alpha[c] + alpha[d] + str(x), plist[i])
					d += 1
				elif c > 26:
					c = 1
					wks.update_value(alpha[c] + alpha[d] + str(x), plist[i])
					d += 1
				elif c > 1:
					wks.update_value(alpha[b] + alpha[c] + str(x), plist[i])
					c += 1	
				elif b > 26:
					b = 1
					wks.update_value(alpha[b] + alpha[c] + str(x), plist[i])
					c += 1
				elif b > 1:
					wks.update_value(alpha[a] + alpha[b] + str(x), plist[i])
					b += 1
				else:
					wks.update_value(alpha[a] + str(x), plist[i])
					a += 1 
		x += 16
		a = 4
		b = 1
		c = 1
		d = 1
		e = 1	
	x = 17
	a = 4
	b = 1
	c = 1
	d = 1
	e = 1
	for j in range (1, len(clist),11):
		for i in range (8,len(plist),11):
			if int(plist[1 + i]) > 0:
				if a > 26:
					a = 1
					wks.update_value(alpha[a] + alpha[b] + str(x), plist[i])
					b += 1
				elif e > 1:
					wks.update_value(alpha[d] + alpha[e] + str(x), plist[i])
				elif d > 26:
					d = 1
					wks.update_value(alpha[d] + alpha[e] + str(x), plist[i])
					e += 1
				elif d > 1:
					wks.update_value(alpha[c] + alpha[d] + str(x), plist[i])
					d += 1
				elif c > 26:
					c = 1
					wks.update_value(alpha[c] + alpha[d] + str(x), plist[i])
					d += 1
				elif c > 1:
					wks.update_value(alpha[b] + alpha[c] + str(x), plist[i])
					c += 1	
				elif b > 26:
					b = 1
					wks.update_value(alpha[b] + alpha[c] + str(x), plist[i])
					c += 1
				elif b > 1:
					wks.update_value(alpha[a] + alpha[b] + str(x), plist[i])
					b += 1
				else:
					wks.update_value(alpha[a] + str(x), plist[i])
					a += 1 
		x += 16
		a = 4
		b = 1
		c = 1
		d = 1
		e = 1	
	x = 18
	a = 4
	b = 1
	c = 1
	d = 1
	e = 1
	for j in range (1, len(clist),11):
		for i in range (9,len(plist),11):
			if int(plist[i]) > 0:
				if a > 26:
					a = 1
					wks.update_value(alpha[a] + alpha[b] + str(x), plist[i])
					b += 1
				elif e > 1:
					wks.update_value(alpha[d] + alpha[e] + str(x), plist[i])
				elif d > 26:
					d = 1
					wks.update_value(alpha[d] + alpha[e] + str(x), plist[i])
					e += 1
				elif d > 1:
					wks.update_value(alpha[c] + alpha[d] + str(x), plist[i])
					d += 1
				elif c > 26:
					c = 1
					wks.update_value(alpha[c] + alpha[d] + str(x), plist[i])
					d += 1
				elif c > 1:
					wks.update_value(alpha[b] + alpha[c] + str(x), plist[i])
					c += 1	
				elif b > 26:
					b = 1
					wks.update_value(alpha[b] + alpha[c] + str(x), plist[i])
					c += 1
				elif b > 1:
					wks.update_value(alpha[a] + alpha[b] + str(x), plist[i])
					b += 1
				else:
					wks.update_value(alpha[a] + str(x), plist[i])
					a += 1 
		x += 16
		a = 4
		b = 1
		c = 1
		d = 1
		e = 1


#################################
#####----- START LOGIC -----#####
#################################

# -- Get Ticker and Option Expiration date from user -- #
ticker = input('TICKER: \n')
expy = input('EXPIRATION DATE: YYYY-MM-DD\n')

# -- Open Google Sheet --#
# -- Must includ space in options because of file name -- #
sh = gc.open('Options ')

# -- create worksheet operator -- #
wks = sh[0]

# -- Grab more data and do math -- #
priceinfo = grabdata(ticker)

thdavg = get30davg(priceinfo)
sixmavg = getsixavg(priceinfo)
ftwavg = get52wavg(priceinfo)
vollist = get2yvol(priceinfo)

buildchain()


# -- extract call data from list into sheet -- #

	
