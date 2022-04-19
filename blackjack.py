# ------------- DECLARATIONS ------------------
import random
deck = 	[('',0),('',0)]
banner = ' B-L-A-C-K-J-A-C-K'
playgame = ['']
card = ['']
oloop = True
playerloop = True
dealerloop = False
gameloop = True
bidloop = True
paloop = True
split1loop = True
splayerloop = True
sdealerloop = True
s1dloop = True
s2dloop = True
s3dloop = True
nevertrue = False
joiner = ' | '

class Player():
	def __init__ (self,name,chips,deckindex,hand,dhand,totlist):
		self.name = name
		self.chips = chips
		self.deckindex = deckindex
		self.hand = hand
		self.dhand = dhand
		self.totlist = totlist
	def cardvals(self,upbig):
		upsmall = [0]
		var_a9 = 0	
		for var_a8 in upbig:
			upsmall.append(upbig[var_a9][1])
			var_a9 +=1
		return upsmall[1:]
		pass		
	def cards(self,ctot):
		var_b2 = 0
		upsmall = ['']
		for var_b1 in ctot:
			upsmall.append(ctot[var_b2][0])
			var_b2 +=1
		return upsmall[1:]
		pass
class Dealer():
	def __init__ (self,deckindex,hand,dhand,totlist,curbid,doubool,splitcount,splithand,sdh1,sth1,sdh2,sth2,sdh3,sth3):
		self.deckindex = deckindex
		self.hand = hand
		self.dhand = dhand
		self.totlist = totlist
		self.curbid = curbid
		self.doubool = doubool
		self.splitcount = splitcount
		self.splithand = splithand
		self.sdh1 = sdh1
		self.sth1 = sth1
		self.sdh2 = sdh2
		self.sth2 = sth2
		self.sdh3 = sdh3
		self.sth3 = sth3
	def wincheck(self):
		if sum(Player1.totlist) > 21 and len(Player1.totlist) == 2:
			Player1.totlist.pop(Player1.totlist.index(11))
			Player1.totlist.append(1)
		if sum(Player1.totlist) == 21 and len(Player1.hand) == 2:
			Table.drawtable()
			print('|A|K| - |A|Q| - P-L-A-Y-E-R - B-L-A-C-K-J-A-C-K - |A|J| - |A|10|')
			Player1.chips = Player1.chips + TheDealer.curbid + (TheDealer.curbid/2)

			return False
		elif list(Player1.dhand)[0][0] == list(Player1.dhand)[1][0] and Player1.chips >= TheDealer.curbid and len(Player1.totlist) == 2:
			wcsloop = True
			Table.drawtable()
			while wcsloop == True:
				spoption = list(input('Would you like to split? (Y)es or (N)o\n'))
				if len(spoption) > 0 and spoption[0].lower() == 'y':
					if TheDealer.splitcount == 1:
						TheDealer.hand.append(deck[50])
						TheDealer.dhand.append(deck[50][0])
						TheDealer.totlist.append(deck[50][1])
					TheDealer.splitcount += 1
					TheDealer.split()
					wcsloop = False
					return True					
				elif len(spoption) > 0 and spoption[0].lower() == 'n':
					wcsloop = False
					return True
				else:
					wcsloop = True
				pass
		elif sum(Player1.totlist) > 21:
			Table.drawtable()
			print("YOU BUST! - THE DEALER WINS!")
			Player1.chips = Player1.chips - TheDealer.curbid
			return False
		else:
			Table.drawtable()
			return True
	def hitstay(self):
		if sum(Player1.totlist) == 21:
			Table.drawtable()
			print("You're at 21! Good Job!")
			return False		
		if Player1.deckindex == 2 and (Player1.chips - TheDealer.curbid) >= TheDealer.curbid:
			poption = list(input('Would you like another card or to double down? Type (H)it or (S)tay or (D)ouble\n'))
			if len(poption) > 0 and poption[0].lower() == 'h': 
				Player1.hand.append(deck[Player1.deckindex])
				Player1.dhand.append(deck[Player1.deckindex][0])
				Player1.totlist.append(deck[Player1.deckindex][1])
				Player1.deckindex += 1
				if sum(Player1.totlist) > 21 and 11 in Player1.totlist:	
					Player1.totlist.pop(Player1.totlist.index(11))
					Player1.totlist.append(1)
					return True				
				return True
			elif len(poption) > 0 and poption[0].lower() == 's':
				TheDealer.hand.append(deck[50])
				TheDealer.dhand.append(deck[50][0])
				TheDealer.totlist.append(deck[50][1])
				return False
			elif len(poption) > 0 and poption[0].lower() == 'd':
				TheDealer.curbid = TheDealer.curbid*2
				print('DOUBLE DOWN!!! The wager has been doubled to ${}'.format(TheDealer.curbid))
				Player1.hand.append(deck[Player1.deckindex])
				Player1.dhand.append(deck[Player1.deckindex][0])
				Player1.totlist.append(deck[Player1.deckindex][1])
				TheDealer.doubool = True		
				if sum(Player1.totlist) > 21 and 11 in Player1.totlist:	
					Player1.totlist.pop(Player1.totlist.index(11))
					Player1.totlist.append(1)
					return True	
				return True
			elif len(poption) > 0 and ((poption[0].lower() == 'q') and (poption[1].lower() == 'u') and (poption[2].lower() == 'i') and (poption[3].lower() == 't')):
				return False
			elif len(poption) > 0 and ((poption[0].lower() == 'e') and (poption[1].lower() == 'x') and (poption[2].lower() == 'i') and (poption[3].lower() == 't')):
				return False
			else:
				return True
		else:
			poption = list(input('Would you like another card? Type (H)it or (S)tay\n'))
			if len(poption) > 0 and poption[0].lower() == 'h': 
				Player1.hand.append(deck[Player1.deckindex])
				Player1.dhand.append(deck[Player1.deckindex][0])
				Player1.totlist.append(deck[Player1.deckindex][1])			
				Player1.deckindex += 1
				if sum(Player1.totlist) > 21 and 11 in Player1.totlist:	
					Player1.totlist.pop(Player1.totlist.index(11))
					Player1.totlist.append(1)
					return True						
				return True
			elif len(poption) > 0 and poption[0].lower() == 's':
				return False
				pass
			elif len(poption) > 0 and ((poption[0].lower() == 'q') and (poption[1].lower() == 'u') and (poption[2].lower() == 'i') and (poption[3].lower() == 't')):
				return False
			elif len(poption) > 0 and ((poption[0].lower() == 'e') and (poption[1].lower() == 'x') and (poption[2].lower() == 'i') and (poption[3].lower() == 't')):
				return False
			else:
				return True
				pass
		pass
	def split(self):
		if TheDealer.splitcount == 4:
			Player1.deckindex == 38
			TheDealer.sdh3 = Player1.dhand
			TheDealer.sth3 = Player1.totlist
			Player1.hand = [deck[1],deck[3]]
			Player1.dhand = Player1.cards(Player1.hand)
			Player1.totlist = Player1.cardvals(Player1.hand)
		elif TheDealer.splitcount == 3:
			Player1.deckindex == 28
			TheDealer.sdh2 = Player1.dhand
			TheDealer.sth2 = Player1.totlist
			Player1.hand = [deck[0],deck[6]]
			Player1.dhand = Player1.cards(Player1.hand)
			Player1.totlist = Player1.cardvals(Player1.hand)
		elif TheDealer.splitcount == 2:
			Player1.deckindex == 18
			TheDealer.sdh1 = Player1.dhand
			TheDealer.sth1 = Player1.totlist
			Player1.hand = [deck[0],deck[4]]
			Player1.dhand = Player1.cards(Player1.hand)
			Player1.totlist = Player1.cardvals(Player1.hand)
		else:
			Player1.deckindex = 8
			Player1.hand = [deck[1],deck[4]]
			TheDealer.sdh1 = Player1.cards(Player1.hand)
			TheDealer.sth1 = Player1.cardvals(Player1.hand)
			Player1.hand = [deck[0],deck[3]]
			Player1.dhand = Player1.cards(Player1.hand)
			Player1.totlist = Player1.cardvals(Player1.hand)			 
		pass
	def s3dealerai(self):	
		Table.drawtable()
		if TheDealer.splitcount == 1:
			if sum(TheDealer.totlist) == 21 and TheDealer.deckindex == 49:
				Table.drawtable()
				print('The Dealer got a B-L-A-C-K-J-A-C-K.')
				Player1.chips = Player1.chips - TheDealer.curbid
				return False
			if sum(TheDealer.totlist) < TheDealer.sth3:
				TheDealer.hand.append(deck[TheDealer.deckindex])
				TheDealer.dhand.append(deck[TheDealer.deckindex][0])
				TheDealer.totlist.append(deck[TheDealer.deckindex][1])
				TheDealer.deckindex = TheDealer.deckindex - 1
				return True
			elif sum(TheDealer.totlist) == TheDealer.sth3 and 11 in TheDealer.totlist:
				TheDealer.totlist.pop(TheDealer.totlist.index(11))
				return True
			elif sum(TheDealer.totlist) > 21 and 11 in TheDealer.totlist:
				TheDealer.totlist.pop(TheDealer.totlist.index(11))
				TheDealer.totlist.append(1)
				return True
			elif sum(TheDealer.totlist) == TheDealer.sth3 and sum(TheDealer.totlist) >= 17:
				print("It's a Draw! I have given back your {:.2f}.".format(TheDealer.curbid))
				return False
			elif sum(TheDealer.totlist) == TheDealer.sth3 and sum(TheDealer.totlist) < 17:
				TheDealer.hand.append(deck[TheDealer.deckindex])
				TheDealer.dhand.append(deck[TheDealer.deckindex][0])
				TheDealer.totlist.append(deck[TheDealer.deckindex][1])
				TheDealer.deckindex = TheDealer.deckindex - 1
				return True
			elif sum(TheDealer.totlist) > 21:
				print('The Dealer Busts!!! {0} wins! You have beeen credited with {1:.2f}.'.format(Player1.name,TheDealer.curbid))
				Player1.chips = Player1.chips + TheDealer.curbid
				return False
			else:
				print('You Lose. I have taken your ${:.2f}.'.format(TheDealer.curbid))
				Player1.chips = Player1.chips - TheDealer.curbid
				return False		
	def s2dealerai(self):	
		Table.drawtable()
		if TheDealer.splitcount == 1:
			if sum(TheDealer.totlist) == 21 and TheDealer.deckindex == 49:
				Table.drawtable()
				print('The Dealer got a B-L-A-C-K-J-A-C-K.')
				Player1.chips = Player1.chips - TheDealer.curbid
				return False
			if sum(TheDealer.totlist) < TheDealer.sth2:
				TheDealer.hand.append(deck[TheDealer.deckindex])
				TheDealer.dhand.append(deck[TheDealer.deckindex][0])
				TheDealer.totlist.append(deck[TheDealer.deckindex][1])
				TheDealer.deckindex = TheDealer.deckindex - 1
				return True
			elif sum(TheDealer.totlist) == TheDealer.sth2 and 11 in TheDealer.totlist:
				TheDealer.totlist.pop(TheDealer.totlist.index(11))
				return True
			elif sum(TheDealer.totlist) > 21 and 11 in TheDealer.totlist:
				TheDealer.totlist.pop(TheDealer.totlist.index(11))
				TheDealer.totlist.append(1)
				return True
			elif sum(TheDealer.totlist) == TheDealer.sth2 and sum(TheDealer.totlist) >= 17:
				print("It's a Draw! I have given back your {:.2f}.".format(TheDealer.curbid))
				return False
			elif sum(TheDealer.totlist) == TheDealer.sth2 and sum(TheDealer.totlist) < 17:
				TheDealer.hand.append(deck[TheDealer.deckindex])
				TheDealer.dhand.append(deck[TheDealer.deckindex][0])
				TheDealer.totlist.append(deck[TheDealer.deckindex][1])
				TheDealer.deckindex = TheDealer.deckindex - 1
				return True
			elif sum(TheDealer.totlist) > 21:
				print('The Dealer Busts!!! {0} wins! You have beeen credited with {1:.2f}.'.format(Player1.name,TheDealer.curbid))
				Player1.chips = Player1.chips + TheDealer.curbid
				return False
			else:
				print('You Lose. I have taken your ${:.2f}.'.format(TheDealer.curbid))
				Player1.chips = Player1.chips - TheDealer.curbid
				return False
	def s1dealerai(self):	
		Table.drawtable()
		if TheDealer.splitcount == 1:
			if sum(TheDealer.totlist) == 21 and TheDealer.deckindex == 49:
				Table.drawtable()
				print('The Dealer got a B-L-A-C-K-J-A-C-K.')
				Player1.chips = Player1.chips - TheDealer.curbid
				return False
			if sum(TheDealer.totlist) < sum(TheDealer.sth1):
				TheDealer.hand.append(deck[TheDealer.deckindex])
				TheDealer.dhand.append(deck[TheDealer.deckindex][0])
				TheDealer.totlist.append(deck[TheDealer.deckindex][1])
				TheDealer.deckindex = TheDealer.deckindex - 1
				return True
			elif sum(TheDealer.totlist) == sum(TheDealer.sth1) and 11 in TheDealer.totlist:
				TheDealer.totlist.pop(TheDealer.totlist.index(11))
				return True
			elif sum(TheDealer.totlist) > 21 and 11 in TheDealer.totlist:
				TheDealer.totlist.pop(TheDealer.totlist.index(11))
				TheDealer.totlist.append(1)
				return True
			elif sum(TheDealer.totlist) == sum(TheDealer.sth1) and sum(TheDealer.totlist) >= 17:
				print("It's a Draw! I have given back your {:.2f}.".format(TheDealer.curbid))
				return False
			elif sum(TheDealer.totlist) == sum(TheDealer.sth1) and sum(TheDealer.totlist) < 17:
				TheDealer.hand.append(deck[TheDealer.deckindex])
				TheDealer.dhand.append(deck[TheDealer.deckindex][0])
				TheDealer.totlist.append(deck[TheDealer.deckindex][1])
				TheDealer.deckindex = TheDealer.deckindex - 1
				return True
			elif sum(TheDealer.totlist) > 21:
				print('The Dealer Busts!!! {0} wins! You have beeen credited with {1:.2f}.'.format(Player1.name,TheDealer.curbid))
				Player1.chips = Player1.chips + TheDealer.curbid
				return False
			else:
				print('You Lose. I have taken your ${:.2f}.'.format(TheDealer.curbid))
				Player1.chips = Player1.chips - TheDealer.curbid
				return False
	def dealerai(self):
		if sum(TheDealer.totlist) == 21 and TheDealer.deckindex == 49:
			Table.drawtable()
			print('The Dealer got a B-L-A-C-K-J-A-C-K.')
			Player1.chips = Player1.chips - TheDealer.curbid
			dealerloop = False
		if sum(TheDealer.totlist) < sum(Player1.totlist):
			TheDealer.hand.append(deck[TheDealer.deckindex])
			TheDealer.dhand.append(deck[TheDealer.deckindex][0])
			TheDealer.totlist.append(deck[TheDealer.deckindex][1])
			TheDealer.deckindex = TheDealer.deckindex - 1
			return True
		elif sum(TheDealer.totlist) == sum(Player1.totlist) and 11 in TheDealer.totlist:
			TheDealer.totlist.pop(TheDealer.totlist.index(11))
			TheDealer.totlist.append(1)
			return True
		elif sum(TheDealer.totlist) > 21 and 11 in TheDealer.totlist:
			TheDealer.totlist.pop(TheDealer.totlist.index(11))
			TheDealer.totlist.append(1)
			return True
		elif sum(TheDealer.totlist) == sum(Player1.totlist) and sum(TheDealer.totlist) >= 17:
			print("It's a Draw! I have given back your {:.2f}.".format(TheDealer.curbid))
			return False
		elif sum(TheDealer.totlist) == sum(Player1.totlist) and sum(TheDealer.totlist) < 17:
			TheDealer.hand.append(deck[TheDealer.deckindex])
			TheDealer.dhand.append(deck[TheDealer.deckindex][0])
			TheDealer.totlist.append(deck[TheDealer.deckindex][1])
			TheDealer.deckindex = TheDealer.deckindex - 1
			return True
		elif sum(TheDealer.totlist) > 21:
			print('The Dealer Busts!!! {0} wins! You have beeen credited with {1:.2f}.'.format(Player1.name,TheDealer.curbid))
			Player1.chips = Player1.chips + TheDealer.curbid
			return False
		else:
			print('You Lose. I have taken your ${:.2f}.'.format(TheDealer.curbid))
			Player1.chips = Player1.chips - TheDealer.curbid
			return False
		pass
class Table():
	def __init__ (self,surface):
		self.surface = surface
	def drawtable():	
		if TheDealer.splitcount == 0:
			print('\n\n -----------------')
			print(banner)
			print(' -----------------')
			print(' ---- {0:^7}----'.format('Dealer'))
			print('\n | {0:<7} |\n'.format(joiner.join(TheDealer.dhand)))
			print(' ---- {0:^7}----'.format('Dealer'))
			print('\n Total: {}'.format(sum(TheDealer.totlist)))
			print('\n                 -----------')
			print('   $$**$$**$$ - | ${:8.2f} | $$**$$**$$'.format(TheDealer.curbid))
			print('                 -----------\n')
			print(' ---- {0:^7}----'.format(Player1.name))
			print('\n | {} |\n'.format(joiner.join(Player1.dhand)))
			print(' ---- {0:^7}----'.format(Player1.name))
			print('\n Total: {}'.format(sum(Player1.totlist)))
			print('\n -----------------')
			print(banner)
			print(' ----------------- \n')
		elif TheDealer.splitcount == 1:
			print('\n\n -----------------')
			print(banner)
			print(' -----------------')
			print(' ---- {0:^7}----'.format('Dealer'))
			if playerloop == True:
				print('\n | {0:<7} |\n'.format(TheDealer.dhand[0]))
			else:
				print('\n | {0:<7} |\n'.format(joiner.join(TheDealer.dhand)))
			print(' ---- {0:^7}----'.format('Dealer'))
			if playerloop == True:
				print('\n Total: {}'.format(TheDealer.totlist[0]))
			else:
				print('\n Total: {}'.format(sum(TheDealer.totlist)))
			print('\n                 -----------')
			print('   $$**$$**$$ - | ${:8.2f} | $$**$$**$$'.format(TheDealer.curbid))
			print('                 -----------\n')
			print(' ---- {0:^7}----'.format(Player1.name))
			if TheDealer.splithand == 0:
				print('\n | {0} | --SPLIT-- | {1} |\n'.format(joiner.join(Player1.dhand),TheDealer.sdh1[0]))
				print(' ---- {0:^7}----'.format(Player1.name))
				print('\n Total: {0}| --SPLIT-- | {1}'.format(sum(Player1.totlist),TheDealer.sth1[1]))
			else:
				print('\n | {0} | --SPLIT-- | {1} |\n'.format(joiner.join(Player1.dhand),joiner.join(TheDealer.sdh1)))
				print(' ---- {0:^7}----'.format(Player1.name))
				print('\n Total: {0}| --SPLIT-- | {1}'.format(sum(Player1.totlist),TheDealer.sth1))
			print('\n -----------------')
			print(banner)
			print(' ----------------- \n')
		elif TheDealer.splitcount == 2:
			print('\n\n -----------------')
			print(banner)
			print(' -----------------')
			print(' ---- {0:^7}----'.format('Dealer'))
			if playerloop == True:
				print('\n | {0:<7} |\n'.format(TheDealer.dhand[0]))
			else:
				print('\n | {0:<7} |\n'.format(joiner.join(TheDealer.dhand)))
			print(' ---- {0:^7}----'.format('Dealer'))
			if playerloop == True:
				print('\n Total: {}'.format(TheDealer.totlist[0]))
			else:
				print('\n Total: {}'.format(sum(TheDealer.totlist)))
			print('\n                 -----------')
			print('   $$**$$**$$ - | ${:8.2f} | $$**$$**$$'.format(TheDealer.curbid))
			print('                 -----------\n')
			print(' ---- {0:^7}----'.format(Player1.name))
			if TheDealer.splithand == 1:
				print('\n | {0} | --SPLIT-- | {1} | --SPLIT-- | {2} |\n'.format(joiner.join(Player1.dhand),TheDealer.sdh1[0],TheDealer.sdh2[0]))
				print(' ---- {0:^7}----'.format(Player1.name))
				print('\n Total: {0} | --SPLIT-- | {1} | --SPLIT-- | {2} |'.format(sum(Player1.totlist),TheDealer.sth1[0],TheDealer.sth2[0]))
			else:
				print('\n | {0} | --SPLIT-- | {1} | --SPLIT-- | {2} |\n'.format(joiner.join(Player1.dhand),joiner.join(TheDealer.sdh1),joiner.join(TheDealer.sdh2)))
				print(' ---- {0:^7}----'.format(Player1.name))
				print('\n Total: {0} | --SPLIT-- | {1} | --SPLIT-- | {2} |'.format(sum(Player1.totlist),TheDealer.sth1,TheDealer.sth2))
			print('\n -----------------')
			print(banner)
			print(' ----------------- \n')
		elif TheDealer.splitcount == 3:
			print('\n\n -----------------')
			print(banner)
			print(' -----------------')
			print(' ---- {0:^7}----'.format('Dealer'))
			if playerloop == True:
				print('\n | {0:<7} |\n'.format(TheDealer.dhand[0]))
			else:
				print('\n | {0:<7} |\n'.format(joiner.join(TheDealer.dhand)))
			print(' ---- {0:^7}----'.format('Dealer'))
			if playerloop == True:
				print('\n Total: {}'.format(TheDealer.totlist[0]))
			else:
				print('\n Total: {}'.format(sum(TheDealer.totlist)))
			print('\n                 -----------')
			print('   $$**$$**$$ - | ${:8.2f} | $$**$$**$$'.format(TheDealer.curbid))
			print('                 -----------\n')
			print(' ---- {0:^7}----'.format(Player1.name))
			print('\n | {0} | --SPLIT-- | {1} | --SPLIT-- | {2} | --SPLIT-- | {3} |\n'.format(joiner.join(Player1.dhand),joiner.join(TheDealer.sdh1),joiner.join(TheDealer.sdh2),joiner.join(TheDealer.sdh3)))
			print(' ---- {0:^7}----'.format(Player1.name))
			print('\n Total: {0} | --SPLIT-- | {1} | --SPLIT-- | {2} | --SPLIT-- | {3} |'.format(sum(Player1.totlist),TheDealer.sth1,TheDealer.sth2,TheDealer.sth3))
			print('\n -----------------')
			print(banner)
			print(' ----------------- \n')
class Bigdeck():
	def __init__ (self,lildeck):
		self.lildeck = lildeck
	def builddeck():
		if len(card) <= 1:
			var_a1 = 0
			for var_a2 in range(0,52):
				if var_a1 > 47:
					card.append('2')
				elif var_a1 > 43:
					card.append('3')
				elif var_a1 > 39:
					card.append('4')
				elif var_a1 > 35:
					card.append('5')
				elif var_a1 > 31:
					card.append('6')
				elif var_a1 > 27:
					card.append('7')
				elif var_a1 > 23:
					card.append('8')
				elif var_a1 > 19:
					card.append('9')
				elif var_a1 > 15:
					card.append('10')
				elif var_a1 > 11:
					card.append('J')
				elif var_a1 > 7:
					card.append('Q')
				elif var_a1 > 3:
					card.append('K')
				else:
					card.append('A')
				var_a1 += 1
			var_a3 = 0
			for var_a4 in card :
				if var_a3 % 4 == 0 :
					card[var_a3] = card[var_a3] + ' - D'
				elif var_a3 % 3 == 0 :
					card[var_a3] = card[var_a3] + ' - H'
				elif var_a3 % 2 == 0 :
					card[var_a3] = card[var_a3] + ' - S'
				else :
					card[var_a3] = card[var_a3] + ' - C'
				var_a3 += 1
			card.pop(0)

			var_a7 = 0
			for var_a6 in card:
				if var_a7  > 47:
					deck.insert(var_a7,(card[var_a7], 2))
				elif var_a7  > 43:
					deck.insert(var_a7,(card[var_a7], 3))
				elif var_a7  > 39:
					deck.insert(var_a7,(card[var_a7], 4))
				elif var_a7  > 35:
					deck.insert(var_a7,(card[var_a7], 5))
				elif var_a7  > 31:
					deck.insert(var_a7,(card[var_a7], 6))
				elif var_a7  > 27:
					deck.insert(var_a7,(card[var_a7], 7))
				elif var_a7  > 23:
					deck.insert(var_a7,(card[var_a7], 8))
				elif var_a7  > 19:
					deck.insert(var_a7,(card[var_a7], 9))
				elif var_a7  > 3:
					deck.insert(var_a7,(card[var_a7], 10))
				else:
					deck.insert(var_a7,(card[var_a7], 11))
				var_a7 += 1
			deck.pop(52)
			deck.pop(52)
		pass	
	def shuffle():
		random.shuffle(deck)
		pass
# ------------ INITIATE GAME --------------------
Bigdeck.builddeck()
print('\n\n -------------------------------------------')
print('  W-E-L-C-O-M-E    T-O    B-L-A-C-K-J-A-C-K ')
print(' -------------------------------------------\n\n')

while oloop == True:
	playgame = list(input('Would you like to play Blackjack? (Y)es or (N)o?\n'))
	if len(playgame) > 0 and playgame[0].lower() == 'y':
		pname = input("We're going to get you started with a small loan of $1,000.00 in chips. Who's name should we put it in? \n\n")
		if len(pname) > 0 and (pname[0].lower() == 'q') and (pname[1].lower() == 'u') and (pname[2].lower() == 'i') and (pname[3].lower() == 't'):
			break
		elif len(pname) > 0 and ((pname[0].lower() == 'e') and (pname[1].lower() == 'x') and (pname[2].lower() == 'i') and (pname[3].lower() == 't')):
			break
#-----------------------------------GAMEPLAY------------------------------
		else:	
#------------------------Create Player and Dealer---------------------
			Player1 = Player(pname,1000,2,[deck[0],deck[1]],[''],[0])
			Player1.totlist = Player1.cardvals(Player1.hand)
			Player1.dhand = Player1.cards(Player1.hand)
			TheDealer = Dealer(49,[deck[51]],[''],[0],0,False,0,0,[''],0,[''],0,[''],0)
			TheDealer.totlist = Player1.cardvals(TheDealer.hand)
			TheDealer.dhand = Player1.cards(TheDealer.hand)
#----------------------- Create Game Loop----------------------------------------			
			while gameloop == True:
#-----------------------------Ask for Wager-----------------------
				while bidloop == True:
					TheDealer.curbid = input('How much would you like to wager? Your balance is ${:.2f} chips. \n'.format(Player1.chips))
					try:
						TheDealer.curbid = float(TheDealer.curbid)
					except:
						print('You did not enter a number.')
						break
#-------------------------------------Deal Cards----------------------------
					if TheDealer.curbid > 0 and TheDealer.curbid <= Player1.chips:
#-----------------------------------------Play Blackjack-------------------------
						while playerloop == True:
							playerloop = TheDealer.wincheck()
							if playerloop == False:
								break
#--------------------------------------SPLIT----------------------------------------------
#########################################################################################################
#######------------------Needs game logic for all 3 spilt conditions---------############################
#########################################################################################################
							if TheDealer.splitcount >= 1:
								while split1loop == True:
									split1loop = TheDealer.wincheck()
									if split1loop == False:
										dealerloop = True
										playerloop = False
										TheDealer.splithand += 1
										break
									if TheDealer.splitcount == 1 and TheDealer.splithand < 1:
										playerloop = True
										split1loop = True
										TheDealer.splithand += 1
										TheDealer.sdh1 = Player1.dhand
										TheDealer.sth1 = sum(Player1.totlist)
										Player1.hand = [deck[1],deck[3]]
										Player1.dhand = Player1.cards(Player1.hand)
										Player1.totlist = Player1.cardvals(Player1.hand)
										break
									elif TheDealer.splitcount == 1 and TheDealer.splithand == 1:
										playerloop = False
										dealerloop = True
										break
									elif TheDealer.splitcount == 2 and TheDealer.splithand == 0:
										playerloop = True
										split1loop = True
										TheDealer.splithand += 1
										TheDealer.sdh2 = TheDealer.sdh1
										TheDealer.sth2 = TheDealer.sth1
										TheDealer.sdh1 = Player1.dhand
										TheDealer.sth1 = Player1.totlist
										Player1.hand = [deck[0],deck[4]]
										Player1.dhand = Player1.cards(Player1.hand)
										Player1.totlist = Player1.cardvals(Player1.hand)
										break
									elif TheDealer.splitcount == 2 and TheDealer.splithand == 1:
										TheDealer.sdh2 = Player1.dhand
										TheDealer.sth2 = Player1.totlist
										TheDealer.sth1 = TheDealer.sth2
										TheDealer.sdh1 = TheDealer.sdh2
										Player1.hand = [deck[0],deck[6]]
										Player1.dhand = Player1.cards(Player1.hand)
										Player1.totlist = Player1.cardvals(Player1.hand)
										Playerloop = True
										split1loop = True
									elif TheDealer.splitcount == 2 and TheDealer.splithand == 2:
										playerloop = False
										dealerloop = True
										break
									else:
										break
									split1loop = TheDealer.wincheck()
									if split1loop == False:
										break	
									split1loop = TheDealer.hitstay()
									if split1loop == False:
										dealerloop = True											
									if TheDealer.doubool == True:
										TheDealer.doubool = False										
										TheDealer.wincheck()
										split1loop = False
										if sum(Player1.totlist) > 21:
											dealerloop = False
										else:
											dealerloop = True
											TheDealer.splithand += 1	
										break
							if playerloop == False:
								dealerloop = True
								break		
#--------------------------Check for Dealer Blackjack--------------------------							
							if sum(TheDealer.totlist) == 21 and TheDealer.deckindex == 49:
								print('The Dealer got a B-L-A-C-K-J-A-C-K.')
								Player1.chips = Player1.chips - TheDealer.curbid
								dealerloop = False
								break								
							if TheDealer.splitcount < 1:
								playerloop = TheDealer.hitstay()
								if playerloop == False:
									dealerloop = True
									break
								if TheDealer.doubool == True:
									TheDealer.doubool = False
									TheDealer.wincheck()
									playerloop = False
									if sum(Player1.totlist) > 21:
										dealerloop = False
									else:
										dealerloop = True
									break	
	#-------------------------------------Dealer AI-------------------------------------
						if TheDealer.splitcount == 3:
							while s3dloop == True:
							 	s3dloop = TheDealer.s3dealerai()
						if TheDealer.splitcount >= 2:
							while s2dloop == True:
							 	s2dloop = TheDealer.s2dealerai()						
						if TheDealer.splitcount >= 1:
							while s1dloop == True:
							 	s1dloop = TheDealer.s1dealerai()
						while dealerloop == True:
							dealerloop = TheDealer.dealerai()
						if Player1.chips == 0:
							print("We see that you've gone through your first line of credit. Here's another $1000.00 to keep you going. \n\n $1000.00 has been credited to your account.")
							Player1.chips = 1000
						print('\n\n{0}, you have ${1:.2f} left in chips.'.format(Player1.name,Player1.chips))
#------------------------------REPLAY?????--------------------------------------						
						while paloop == True:
							playagain = list(input('Would you like to play again? (Y)es or (N)o?\n'))
							if len(playagain) > 0 and playagain[0].lower() == 'y':
								playerloop = True
								dealerloop = False
								Bigdeck.shuffle()
								Bigdeck.shuffle()
								Bigdeck.shuffle()
								Player1.hand = [deck[0],deck[1]]
								Player1.deckindex = 2
								Player1.totlist = Player1.cardvals(Player1.hand)
								Player1.dhand = Player1.cards(Player1.hand)						
								TheDealer.hand = [deck[51]]
								TheDealer.deckindex = 49
								TheDealer.totlist = Player1.cardvals(TheDealer.hand)
								TheDealer.dhand = Player1.cards(TheDealer.hand)
								TheDealer.splitcount = 0
								TheDealer.splithand = 0
								break
							elif len(playagain) > 0 and playagain[0].lower() == 'n':
								gameloop = False
								oloop = False
								bidloop = False
								break
							elif len(playagain) > 0 and ((playagain[0].lower() == 'q') and (playagain[1].lower() == 'u') and (playagain[2].lower() == 'i') and (playagain[3].lower() == 't')):
								gameloop = False
								oloop = False
								bidloop = False
								break
							elif len(playagain) > 0 and ((playagain[0].lower() == 'e') and (playagain[1].lower() == 'x') and (playagain[2].lower() == 'i') and (playagain[3].lower() == 't')):
								gameloop = False
								oloop = False
								bidloop = False
								break
							else:
								pass
					elif TheDealer.curbid > Player1.chips:
						print('You do not have enough chips to make this wager. Please try again.')
					else:
						pass
#---------------Response = no quit or exit-------------
	elif playgame[0].lower() == 'n':
		break
	elif ((playgame[0].lower() == 'q') and (playgame[1].lower() == 'u') and (playgame[2].lower() == 'i') and (playgame[3].lower() == 't')):
		break
	elif ((playgame[0].lower() == 'e') and (playgame[1].lower() == 'x') and (playgame[2].lower() == 'i') and (playgame[3].lower() == 't')):
		break
#---------unrecognized input----------------
	else:
		print('Sorry, that is not a valid input. Try again.\n')




		###########################################################################
#--------------Need to figure out how and where to impliment this---------#
###########################################################################
while nevertrue == True:
	break
	if TheDealer.splitcount == 1:
		TheDealer.sdh1 = Player1.dhand
		TheDealer.sth1 = Player1.totlist
		Player1.hand = [deck[1],deck[3]]
		Player1.dhand = Player1.cards(Player1.hand)
		Player1.totlist = Player1.cardvals(Player1.hand)
		playerloop = True
	elif TheDealer.splitcount == 2:
		TheDealer.sdh2 = TheDealer.sdh1
		TheDealer.sdh1 = Player1.cards(Player1.hand)
		Player1.hand = [deck[0],deck[4]]
		Player1.dhand = Player1.cards(Player1.hand)
		Player1.totlist = Player1.cardvals(Player1.hand)
		split1loop = True
		playerloop = True
	elif TheDealer.splitcount == 3:
		TheDealer.sdh3 = TheDealer.sdh3
		TheDealer.sdh2 = TheDealer.sdh1
		TheDealer.sdh1 = Player1.cards(Player1.hand)
		Player1.hand = [deck[0],deck[6]]
		Player1.dhand = Player1.cards(Player1.hand)
		Player1.totlist = Player1.cardvals(Player1.hand)
		split1loop = True
		playerloop = True	