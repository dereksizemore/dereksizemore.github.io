import os


def sortdata(inlist):
	outlist = []
	for i in range(2,len(inlist),6):
		outlist.append(inlist[i - 2])
		outlist.append(inlist[i])
		outlist.append(inlist[i + 1])
		outlist.append(inlist[i + 3])
	return outlist

def writedata(inlist):
	outfile = open('faillist.txt','a')
	for i in inlist:
		outfile.write(i + " ")
	outfile.write('\n')
	outfile.close()

def grabftddata(ftds):
	string = ""
	ftds.split()
	outlist = []
	for i in ftds:
		if i == "|":
			outlist.append(string)
			string = ""
		elif i == '\n':
			outlist.append(string)
			string = ""
		else:
			string = string + i
	return outlist
def grabtickerdata(inlist):
	string = ""
	inlist.split()
	outlist = []
	for i in inlist:
		if i == ",":
			outlist.append(string)
			string = ""
		else:
			string = string + i
	return outlist
###################################
######------ START LOGIC -----#####
###################################
# -- Change Directory to D:/PYTON/Stock/FTD/ -- #
os.chdir(r'D:/PYTON/Stock/FTD/')

# -- Get Tickers to pull from ftd data from pre defined text file -- #
tickerdata = open('tickers.txt','r')
tickersdata = tickerdata.read()
tickerdata.close()

# -- Get ftddata from downloaded file -- #
ftdata = open('ftddata.txt','r')
ftds = ftdata.read()
ftdata.close()

# --  format data -- #
data = grabftddata(ftds)
sortedData = sortdata(data)
tickers = grabtickerdata(tickersdata)

# -- Write data -- #
for a in tickers:
	for i in range(1,len(sortedData),4):
		if sortedData[i] == a:
			writedata([sortedData[i],sortedData[i - 1],sortedData[i + 1],sortedData[i + 2]])
	addspace = open('faillist.txt','a')
	addspace.write('\n')
	addspace.close()

for i in range(3, len(sortedData),4):
	if i > 3:
		if sortedData[i] != '.':
			if float(sortedData[i])*float(sortedData[i-1]) > 30000000:
				writedata([sortedData[i - 2],sortedData[i - 3],sortedData[i - 1],sortedData[i]])
addspace = open('faillist.txt','a')
addspace.write('\n')
addspace.close()