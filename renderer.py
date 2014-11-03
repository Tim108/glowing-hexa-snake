import math

import pygame
import time
import sys
import threading

class Renderer(threading.Thread):
	size = 640, 480
	black = 0, 0, 0
	white = 255, 255, 255
	states = ['menu', 'highscores', 'inGame', 'pause', 'gameOver', 'drawSnake', 'drawCandy', 'deleteSnake']
	o = 0
	candy = -1
	snake = []
	state = 0

	def __init__(self, output):
		print "renderer init"
		threading.Thread.__init__(self)
		pygame.init()
                size = width, height = 640, 480
		self.o = output		
		self.changeState(self.states[0], 0)

	def changeState(self, guiState, num):
		if guiState == Renderer.states[0]:
                        #In menu
                        self.drawMenu()
			print "changed state to menu"
                elif guiState == Renderer.states[1]:
                        #In highscores
                        print "highscore state"
                        ###self.drawHighscores()
                elif guiState == Renderer.states[2]:
                        #In game, draw game/board/thingy
                        self.drawStartGame()
                elif guiState == Renderer.states[3]:
                        #Game paused
                        self.drawPauseOverlay()
                elif guiState == Renderer.states[4]:
                        #Game over
                        #print "In GameOver mode"
                        self.drawGameOverOverlay(num)
                elif guiState == Renderer.states[5]:
                        self.drawSnake(num)
                elif guiState == Renderer.states[6]:
                        self.drawCandy(num)
                elif guiState == Renderer.states[7]:
                        self.deleteSnake(num)
                else:
                        print 'Should not be able to happen'
                pygame.display.flip()


	def toXY(self, i):
        	x = (i % 15)*30  + 15
        	y = (math.floor(i/15))*30  + 15
        	return (x,y)


	def drawStartGame(self):
		self.drawField()
		self.drawSnakeArray()
		self.printScore(str(0))
		self.o.bStart()
		#self.drawSnake(location)

	#Draw snake WITHOUT new location, just the snake array that is known by the class
	def drawSnakeArray(self):
		self.drawField()
		snakeImage = pygame.image.load('res/snakebase.png')
		snakeHeadImage = pygame.image.load('res/snakehead.png')
		for i in self.snake:
			if i == self.snake[0]:
				self.fieldSurface.blit(snakeHeadImage, self.toXY(i))
			else:
				self.fieldSurface.blit(snakeImage, self.toXY(i))
		self.fieldScreen.blit(self.fieldSurface, (0, 0))
		pygame.display.flip()

	#Draw snake WITH new location
	def drawSnake(self, location):
		self.drawField()
		self.drawCandyArray()
		self.snake.insert(0, location)
		snakeImage = pygame.image.load('res/snakebase.png')
		snakeHeadImage = pygame.image.load('res/snakehead.png')
		for i in self.snake:
			if i == location:
				self.fieldSurface.blit(snakeHeadImage, self.toXY(i))
			else:
				self.fieldSurface.blit(snakeImage, self.toXY(i))
		self.fieldScreen.blit(self.fieldSurface, (0, 0))
		pygame.display.flip()

	def drawCandyArray(self):
		self.drawField()
		self.drawSnakeArray()
		candyImage = pygame.image.load('res/mouse.png')
		self.fieldSurface.blit(candyImage, self.toXY(self.candy))
		self.fieldScreen.blit(self.fieldSurface, (0, 0))
		pygame.display.flip()

	def drawCandy(self, location):
		self.candy = location
		self.drawField()
		self.drawSnakeArray()
		candyImage = pygame.image.load('res/mouse.png')
		self.fieldSurface.blit(candyImage, self.toXY(location))
		self.fieldScreen.blit(self.fieldSurface, (0, 0))
		pygame.display.flip()

	def deleteSnake(self, location):
		if location in self.snake:
			self.snake.remove(location)
#		self.drawSnake(location)
#		time.sleep(2)
#		print "done sleeping"
#		blackImage = pygame.image.load('res/black.png')
#		print "image loaded"
#		self.fieldSurface.blit(blackImage, location)
#		self.fieldScreen.blit(self.fieldSurface, (0, 0))
#		print "done blitting"
		self.drawField()
		self.drawSnakeArray()		

		pygame.display.flip()
		#self.checkButtons()

	def drawMenu(self):
		print "Drawing menu"
		self.screen = pygame.display.set_mode(self.size)
		#Make surface
		mySurface = pygame.Surface(self.size)
		#mySurface.fill(black)
		
		#Make background picture (load and put on surface)
		myBackground = pygame.image.load('res/background.png')
		mySurface.blit(myBackground, (0,0))

		#Implementation of button images
		buttons = ['res/Start.png', 'res/Highscores.png', 'res/Exit.png']
		for b in range (0, len(buttons)):
			path = buttons[b]
			myImage = pygame.image.load(path)
			mySurface.blit(myImage, (155, 130+b*60))

		self.screen.blit(mySurface, (0, 0))

	def run(self):
		print "banaantjes"
		totalClicks = 0
		numClicked = 0

        	while(True):
	            	for event in pygame.event.get():
				#print "Blablabla"
				if event.type == pygame.MOUSEBUTTONDOWN:
					totalClicks = totalClicks + 1
					#print "Mouse gets (de)pressed"
					pos = pygame.mouse.get_pos()
					xPos = pos[0]
					yPos = pos[1]
					#Check where the mouse has clicked
					if xPos >= 155 and xPos <= 255:
						if yPos >= 130 and yPos <= 180:
							self.drawStartGame()
							#sys.exit()
#							print "Start game has been clicked"
						elif yPos >= 180 and yPos <= 240:
							print "Highscores has been clicked"
						elif yPos >= 240 and yPos <= 300:
#							print "Exit game has been clicked"
							sys.exit()
							print str(totalClicks) + " , " + str(numClicked)

				if event.type == pygame.USEREVENT:
					n = event.action
					l = event.location
					if n == 4:
						self.printScore(l)
					elif n == 2:
						self.drawCandy(l)
					elif n == 6:
						self.drawSnake(l)
					elif n == 1:
						self.deleteSnake(l)
					elif n == 7:
						self.drawGameOverOverlay(l)

				if event.type == pygame.QUIT:
					sys.exit()
					
		print "Uit while"
	

	def drawField(self):
		#Make screen
		self.fieldScreen = pygame.display.set_mode(self.size)
		#Make surface
		self.fieldSurface = pygame.Surface(self.size)
		self.fieldSurface.fill(Renderer.black)
		#Draw grid
		grey = 96, 96, 96
		for c in range(0, 16):
			pygame.draw.line(self.fieldSurface, grey, [c*30+15, 15], [c*30+15, 15*30+15])
			pygame.draw.line(self.fieldSurface, grey, [15, c*30+15], [15*30+15, c*30+15])
		self.fieldScreen.blit(self.fieldSurface, (0,0))
		#Draw buttons
#		fieldButtons = ['res/Pause.png', 'res/Exit.png']
#		for x in range (0, len(fieldButtons)):
#			pathField = fieldButtons[x]
#			imageField = pygame.image.load(pathField)
#			self.fieldSurface.blit(imageField, (488, 15+x*65))
#		self.fieldScreen.blit(self.fieldSurface, (0,0))
		#Draw "Score:"
		scoreFont = pygame.font.SysFont("Arial", 30)
		scoreText = scoreFont.render("Score: ", True, Renderer.white)
		self.fieldSurface.blit(scoreText, (510, 365))
		self.fieldScreen.blit(self.fieldSurface, (0, 0))

		pygame.display.flip()		
		#Find correct way to check whether buttons are pressed!!!
	# 	self.checkButtons()
		#self.checkButtons()
#		self.drawCandy((45, 15))
		#self.drawSnake((15, 45))
	
	#def checkButtons(self):
	#	while True:
	#		for event in pygame.event.get():
	#			if event.type == pygame.MOUSEBUTTONDOWN:
	#				pos = pygame.mouse.get_pos()
	#				xPos = pos[0]
	#				yPos = pos[1]
	#				if xPos >= 488 and xPos <= 618:
	#					if yPos >= 15 and yPos <= 65:
	#						self.drawPauseOverlay()
	#					elif yPos >= 80 and yPos <= 130:
         #                                               sys.exit()
	#	pygame.display.flip()

	def drawPauseOverlay(self):		
                #Make overlay
                s = pygame.Surface(self.size)
                s.set_alpha(128)
                s.fill(Renderer.black)
                #fieldScreen.blit(s, (0,0))
                #Make text "Game paused" on overlay
                font = pygame.font.SysFont("Arial", 40)
                gamePausedLabel = font.render("Game paused", 1, Renderer.white)
                font = pygame.font.SysFont("Arial", 20)
                pressPLabel = font.render("Click to continue", 1, Renderer.white)
                xLoc = (640 - gamePausedLabel.get_width())/2
                yLoc = (480 - (pressPLabel.get_height() + gamePausedLabel.get_height()))/2
                s.blit(gamePausedLabel, (xLoc, yLoc))
                x2Loc = (640 - pressPLabel.get_width())/2
                y2Loc = (480 + pressPLabel.get_height())/2
#		self.printScore('Pause')
		#Make overlay
		#fieldScreen.blit(s, (0,0))
		#Make text "Game paused" on overlay
		s.blit(pressPLabel, (x2Loc, y2Loc))
		self.fieldScreen.blit(s, (0, 0))
#	printScore('Pause')
		#Make overlay
		#fieldScreen.blit(s, (0,0))
		#Make text "Game paused" on overlay
		count = 0
		while True:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					count += 1
					if count>0:
						count = 0
						self.drawInGame()

			pygame.display.flip()
										

	def drawGameOverOverlay(self, score):
		s = pygame.Surface(self.size)
		s.set_alpha(128)
		s.fill(Renderer.black)
		#Make text "Game Over" on overlay + score
		font = pygame.font.SysFont("Arial", 40)
		gameOverLabel = font.render("Game Over", 1, Renderer.white)
		font = pygame.font.SysFont("Arial", 20)
		scoreLabel = font.render("Score:" + str(score), 1, Renderer.white)
 
		xLoc = (640 - gameOverLabel.get_width())/2
		yLoc = (480 - (scoreLabel.get_height() + gameOverLabel.get_height()))/2
		s.blit(gameOverLabel,(xLoc, yLoc))
		
		x2Loc = (640 - scoreLabel.get_width())/2
		y2Loc = (480 + scoreLabel.get_height())/2
		s.blit(scoreLabel, (x2Loc, y2Loc))
		self.fieldScreen.blit(s, (0, 0))
		
		count = 0
		overlayActive = True
                while overlayActive:
                        for event in pygame.event.get():
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                        count += 1
                                        if count>0:
                                                count = 0
						overlayActive = False

                        pygame.display.flip()
                self.drawMenu()


	def printScore(self, score):
		#Print score beneath "Score:" label
		self.drawField()
		self.drawSnakeArray()
		if self.candy != -1:
			self.drawCandyArray()
		scoreFont = pygame.font.SysFont("Arial", 30)
		scoreNum = scoreFont.render(str(score), True, Renderer.white)
		self.fieldScreen.blit(scoreNum, (510, 400))		
		pygame.display.flip()

if __name__ == "__main__":
	renderer = Renderer()
