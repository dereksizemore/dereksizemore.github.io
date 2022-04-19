##-------- Make Some Functions and Declare any needed variables---------
gamerun = True
board = ['        ']
boardstate = False
newgame = " "
entry = True
var_a6 = 0
bar = '            ||          ||'
barline = '  ----------||----------||---------'
banner = " \\/\\/\\ TIC /\\/\\/\\ TAC /\\/\\/\\ TOE /\\/\\/ "
xturnban = " ---------- PLAYER X'S TURN ---------- "
oturnban = " ---------- PLAYER O'S TURN ---------- "
xwinban = " --------- PLAYER X WINS!!!! --------- "
owinban = " --------- PLAYER O WINS!!!! --------- "
drawban = " ------------ IT's A DRAW ------------ "



def turnx() :
	return input("\n Player X's Turn : Please input a corresponding number to put your X on the board. \n")
	pass
def turnxentry() :
	for var_a in board :
		if thismovex[0] == var_a :
			board[board.index(var_a) + 1] = ' \\\\  // '
			board[board.index(var_a) - 1] = ' //  \\\\'
			board[board.index(var_a)] = '  }}{{  '
	pass
def turno() :
	return list(input("\n Player O's Turn : Please input a corresponding number to put your O on the board. \n"))
	pass
def turnoentry() :
	for var_b in board :
		if thismoveo[0] == var_b :
			board[board.index(var_b) + 1] = '  ****  '
			board[board.index(var_b) - 1] = '  ****  '
			board[board.index(var_b)] = ' **  ** '
	pass	
def gameboard() :
	if len(board) <= 1 :
		var_a6 = 0
		for var_aaaaa in range(0,27) :
			if var_aaaaa == 1 :
				board.append('1')
			elif var_aaaaa == 0:
				pass
			elif ((var_aaaaa - 1)% 3) == 0 :
				var_a6 += 1
				board.append(int((var_aaaaa - (var_a6 - 1)) / 2))
			else :
				board.append('        ')
	var_a8 = 0
	for var_a7 in board :
		board[var_a8] = str(board[var_a8])
		var_a8 += 1
	print('\n #####################################')
	print(banner)
	print(' #####################################\n')
	print('\n   {0:^8} || {1:^8} || {2:^8}'.format(board[20],board[23],board[26]))
	print('   {0:^8} || {1:^8} || {2:^8}'.format(board[19],board[22],board[25]))
	print('   {0:^8} || {1:^8} || {2:^8}'.format(board[18],board[21],board[24]))
	print(barline)
	print(barline)
	print('   {0:^8} || {1:^8} || {2:^8}'.format(board[11],board[14],board[17]))
	print('   {0:^8} || {1:^8} || {2:^8}'.format(board[10],board[13],board[16]))
	print('   {0:^8} || {1:^8} || {2:^8}'.format(board[9],board[12],board[15]))
	print(barline)
	print(barline)
	print('   {0:^8} || {1:^8} || {2:^8}'.format(board[2],board[5],board[8]))
	print('   {0:^8} || {1:^8} || {2:^8}'.format(board[1],board[4],board[7]))
	print('   {0:^8} || {1:^8} || {2:^8}'.format(board[0],board[3],board[6]))
	print('\n #####################################')
	print(banner)
	print(' #####################################\n')
	pass
def xwins() :
	chickendx()
	gameboard()
	pass
def owins() :
	chickendo()
	gameboard()
	pass
def draw() :
	gameboard()
	pass
def chickendx() :
	if (board[1] == board[4] and board[4] == board[7]) :
		board[2] = '*\\\\  //*'
		board[1] = '* }}{{ *'
		board[0] = '*//  \\\\*'
		board[5] = '*\\\\  //*'
		board[4] = '* }}{{ *'
		board[3] = '*//  \\\\*'
		board[8] = '*\\\\  //*'
		board[7] = '* }}{{ *'
		board[6] = '*//  \\\\*'
	elif (board[10] == board[13] and board[13] == board[16]) :
		board[11] = '*\\\\  //*'
		board[10] = '* }}{{ *'
		board[9] = '*//  \\\\*'
		board[14] = '*\\\\  //*'
		board[13] = '* }}{{ *'
		board[12] = '*//  \\\\*'
		board[17] = '*\\\\  //*'
		board[16] = '* }}{{ *'
		board[15] = '*//  \\\\*'
	elif (board[19] == board[22] and board[22] == board[25]) :
		board[20] = '*\\\\  //*'
		board[19] = '* }}{{ *'
		board[18] = '*//  \\\\*'
		board[23] = '*\\\\  //*'
		board[22] = '* }}{{ *'
		board[21] = '*//  \\\\*'
		board[26] = '*\\\\  //*'
		board[25] = '* }}{{ *'
		board[24] = '*//  \\\\*'
	elif (board[1] == board[13] and board[13] == board[25]) :
		board[2] = '*\\\\  //*'
		board[1] = '* }}{{ *'
		board[0] = '*//  \\\\*'
		board[14] = '*\\\\  //*'
		board[13] = '* }}{{ *'
		board[12] = '*//  \\\\*'
		board[26] = '*\\\\  //*'
		board[25] = '* }}{{ *'
		board[24] = '*//  \\\\*'
	elif (board[7] == board[13] and board[13] == board[19]) :
		board[8] = '*\\\\  //*'
		board[7] = '* }}{{ *'
		board[6] = '*//  \\\\*'
		board[14] = '*\\\\  //*'
		board[13] = '* }}{{ *'
		board[12] = '*//  \\\\*'
		board[20] = '*\\\\  //*'
		board[19] = '* }}{{ *'
		board[18] = '*//  \\\\*'
	elif (board[1] == board[10] and board[10] == board[19]) :
		board[2] = '*\\\\  //*'
		board[1] = '* }}{{ *'
		board[0] = '*//  \\\\*'
		board[11] = '*\\\\  //*'
		board[10] = '* }}{{ *'
		board[9] = '*//  \\\\*'
		board[20] = '*\\\\  //*'
		board[19] = '* }}{{ *'
		board[18] = '*//  \\\\*'		
	elif (board[4] == board[13] and board[13] == board[22]) :
		board[5] = '*\\\\  //*'
		board[4] = '* }}{{ *'
		board[3] = '*//  \\\\*'
		board[14] = '*\\\\  //*'
		board[13] = '* }}{{ *'
		board[12] = '*//  \\\\*'
		board[23] = '*\\\\  //*'
		board[22] = '* }}{{ *'
		board[21] = '*//  \\\\*'
	elif (board[7] == board[16] and board[16] == board[25]) :
		board[8] = '*\\\\  //*'
		board[7] = '* }}{{ *'
		board[6] = '*//  \\\\*'
		board[17] = '*\\\\  //*'
		board[16] = '* }}{{ *'
		board[15] = '*//  \\\\*'
		board[26] = '*\\\\  //*'
		board[25] = '* }}{{ *'
		board[24] = '*//  \\\\*'
	pass
def chickendo() :
	if (board[1] == board[4] and board[4] == board[7]) :
		board[2] = '- **** -'
		board[1] = '-**  **-'
		board[0] = '- **** -'
		board[5] = '- **** -'
		board[4] = '-**  **-'
		board[3] = '- **** -'
		board[8] = '- **** -'
		board[7] = '-**  **-'
		board[6] = '- **** -'
	elif (board[10] == board[13] and board[13] == board[16]) :
		board[11] = '- **** -'
		board[10] = '-**  **-'
		board[9] = '- **** -'
		board[14] = '- **** -'
		board[13] = '-**  **-'
		board[12] = '- **** -'
		board[17] = '- **** -'
		board[16] = '-**  **-'
		board[15] = '- **** -'
	elif (board[19] == board[22] and board[22] == board[25]) :
		board[20] = '- **** -'
		board[19] = ' **  ** '
		board[18] = '- **** -'
		board[23] = '- **** -'
		board[22] = '-**  **-'
		board[21] = '- **** -'
		board[26] = '- **** -'
		board[25] = '-**  **-'
		board[24] = '- **** -'
	elif (board[1] == board[13] and board[13] == board[25]) :
		board[2] = '- **** -'
		board[1] = '-**  **-'
		board[0] = '- **** -'
		board[14] = '- **** -'
		board[13] = '-**  **-'
		board[12] = '- **** -'
		board[26] = '- **** -'
		board[25] = '-**  **-'
		board[24] = '- **** -'
	elif (board[7] == board[13] and board[13] == board[19]) :
		board[8] = '- **** -'
		board[7] = '-**  **-'
		board[6] = '- **** -'
		board[14] = '- **** -'
		board[13] = '-**  **-'
		board[12] = '- **** -'
		board[20] = '- **** -'
		board[19] = '-**  **-'
		board[18] = '- **** -'
	elif (board[1] == board[10] and board[10] == board[19]) :
		board[2] = '- **** -'
		board[1] = '-**  **-'
		board[0] = '- **** -'
		board[11] = '- **** -'
		board[10] = '-**  **-'
		board[9] = '- **** -'
		board[20] = '- **** -'
		board[19] = '-**  **-'
		board[18] = '- **** -'		
	elif (board[4] == board[13] and board[13] == board[22]) :
		board[5] = '- **** -'
		board[4] = '-**  **-'
		board[3] = '- **** -'
		board[14] = '- **** -'
		board[13] = '-**  **-'
		board[12] = '- **** -'
		board[23] = '- **** -'
		board[22] = '-**  **-'
		board[21] = '- **** -'
	elif (board[7] == board[16] and board[16] == board[25]) :
		board[8] = '- **** -'
		board[7] = '-**  **-'
		board[6] = '- **** -'
		board[17] = '- **** -'
		board[16] = '-**  **-'
		board[15] = '- **** -'
		board[26] = '- **** -'
		board[25] = '-**  **-'
		board[24] = '- **** -'
	pass
def wincheck() :
	if (str(board[1]) == str(board[4]) and str(board[4]) == str(board[7])) or (str(board[10]) == str(board[13]) and str(board[13]) == str(board[16])) or (str(board[19]) == str(board[22]) and str(board[22]) == str(board[25])) or (str(board[1]) == str(board[13]) and str(board[13]) == str(board[25])) or (str(board[7]) == str(board[13]) and str(board[13]) == str(board[19])) or (str(board[1]) == str(board[10]) and str(board[10]) == str(board[19])) or (str(board[4]) == str(board[13]) and str(board[13]) == str(board[22])) or (str(board[7]) == str(board[16]) and str(board[16]) == str(board[25])) :
		return True
	else :
		return False
	pass
def drawcheck() :
	for var_c in board :
		if (board[1] != '1') and (board[4] != '2') and (board[7] != '3') and (board[10] != '4') and (board[13] != '5') and (board[16] != '6') and (board[19] != '7') and (board[22] != '8') and (board[25] != '9') :
			return True
		else :
			return False
	pass
##----------------Initiate Game ----------------
print("[(You can close the program anytime by typing \"Quit\" or \"Exit\")]")
print('\n #####################################')
print(banner)
print(' #####################################\n')
print(bar)
print(bar)
print(bar)
print(barline)
print(barline)
print(bar)
print('')
print('       Welcome to Tic Tac Toe!!!')
print('')
print(bar)
print(barline)
print(barline)
print(bar)
print(bar)
print(bar)
print('\n #####################################')
print(banner)
print(' #####################################\n')
while gamerun == True :
## ---======-- Ask to Play ----
	print("\n     Would you like to play a game of Tic Tac Toe? You'll need 2 players!")
## ------------- Recieve Input and make it a list of characters ----
	startgame = list(input('          (Y)es or (N)o \n'))
	print("\n\n\n  [(You can close the program anytime by typing \"Quit\" or \"Exit\")]")
## --------------- Y INPUT - START GAME ----------------------
	if len(startgame) >= 1 :
		if startgame[0].lower() == 'y' or newgame[0].lower() == 'y' :
			xturn = True
			oturn = False
			exit = False
			boardstate = False
## ------- GAME ENGINE------
			while boardstate == False :
				while xturn == True :
					banner = xturnban
## ---------- Draw Game Board ------------
					gameboard()	
##----------- Player X Turn ----------
					thismovex = turnx()
##----------- Check for correct input or win----------	
					for var_aa in board :
						if len(thismovex) >= 1 :
							if len(thismovex) >= 4 :
								if thismovex[0].lower() == 'q' and thismovex[1].lower() == 'u' and thismovex[2].lower() == 'i' and thismovex[3].lower() == 't' :
									boardstate = True
									gamerun = False
									xturn = False
									oturn = False
									break
								elif thismovex[0].lower() == 'e' and thismovex[1].lower() == 'x' and thismovex[2].lower() == 'i' and thismovex[3].lower() == 't' :
									boardstate = True
									gamerun = False
									xturn = False
									oturn = False
									break
								else :
									if var_aa == thismovex[0] :
										turnxentry()
										xturn = False
										oturn = True
							else :		
								if var_aa == thismovex[0] :
									turnxentry()
									xturn = False
									oturn = True
					if boardstate == True :
						break
##---------- If X has won or drawn, output message and ask to replay ---------
					boardstate = wincheck()
					if boardstate == True :
						banner = xwinban
						xwins()
						oturn = False
						exit = True
						break
					else :
						boardstate = drawcheck()
						if boardstate == True :
							banner = drawban
							draw()
							exit = True
							oturn = False
							xturn = False
							break
				while oturn == True :
					banner = oturnban
##---------- Draw Game Board -----------
					gameboard()
##---------- Player O Turn -----------
					thismoveo = turno()
##---------- Check for input or win -----------
					for var_cc in board :
						if len(thismoveo) >= 1 :
							if len(thismoveo) >= 4 :
								if thismoveo[0].lower() == 'q' and thismoveo[1].lower() == 'u' and thismoveo[2].lower() == 'i' and thismoveo[3].lower() == 't' :
									boardstate = True
									gamerun = False
									oturn = False
									xturn = False
									break
								elif thismoveo[0].lower() == 'e' and thismoveo[1].lower() == 'x' and thismoveo[2].lower() == 'i' and thismoveo[3].lower() == 't' :
									boardstate = True
									gamerun = False
									oturn = False
									xturn = False
									break
								else :
									if var_cc == thismoveo[0] :
										turnoentry()
										oturn = False
										xturn = True
							else :		
								if var_cc == thismoveo[0] :
									turnoentry()
									oturn = False
									xturn = True
					if boardstate == True :
						break
##---------- If O has won or drawn, output message and ask to replay ---------
					boardstate = wincheck()
					if boardstate == True :
						banner = owinban
						owins()
						xturn = False
						exit = True
						break
					else :
						boardstate = drawcheck()
						if boardstate == True :
							banner = drawban
							draw()
							exit = True
							oturn = False
							xturn = False
							break
				if exit == True :
					boardstate = True
					board = ['        ']
## --------------- N INPUT - ABORT GAME -----------------------
		elif startgame[0].lower() == 'n' or newgame[0].lower() == 'n' :
			gamerun = False
		elif ((startgame[0].lower() == 'q') and (startgame[1].lower() == 'u') and (startgame[2].lower() == 'i') and (startgame[3].lower() == 't')) :
			gamerun = False
		elif ((startgame[0].lower() == 'e') and (startgame[1].lower() == 'x') and (startgame[2].lower() == 'i') and (startgame[3].lower() == 't')) :
			gamerun = False
## --------------- Other INPUT - RESTART PROMPT -----------------
		else :
			print('Opps, you pressed the wrong key')