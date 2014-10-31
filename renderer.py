
import pygame
import time
import sys

class Renderer(object):
	black = 0, 0, 0
	white = 255, 255, 255
	states = ['menu', 'highscores', 'inGame', 'pause', 'gameOver']
	def __init__(self, guiState):
		pygame.init()
		if guiState == Renderer.states[0]:
			#In menu
			self.drawMenu()
		elif guiState == Renderer.states[1]:
			#In highscores
			print "highscore state"
			###self.drawHighscores()
		elif guiState == Renderer.states[2]:
			#In game, draw game/board/thingy
			self.drawInGame()
		elif guiState == Renderer.states[3]:
			#Game paused
			self.drawPauseOverlay()
		elif guiState == Renderer.states[4]:
			#Game over
			print "In GameOver mode"
			##self.drawGameOverOverlay
		else:
			print 'Should not be able to happen'

	def drawInGame(self):
		self.drawField()
		self.drawSnake(location)
		self.drawCandy(location)

	def drawSnake(self, location):
		snakeImage = pygame.image.load('res/snakebase.png')
		self.fieldSurface.blit(snakeImage, (location))
		self.fieldScreen.blit(self.fieldSurface, (0, 0))

	def drawCandy(self, location):
		candyImage = pygame.image.load('res/mouse.png')
		self.fieldSurface.blit(candyImage, (location))
		self.fieldScreen.blit(self.fieldSurface, (0, 0))

	def deleteSnake(self, location):
		blackImage = pygame.image.load('res/black.png')
		self.fieldSurface.blit(blackImage, (location))
		self.fieldScreen.blit(self.fieldSurface, (0, 0))

	def drawMenu(self):
        	size = width, height = 640, 480
        	screen = pygame.display.set_mode(size)

		#Make surface
		mySurface = pygame.Surface(size)
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

		screen.blit(mySurface, (0, 0))

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
							numClicked = numClicked + 1
							self.drawField()
#							print "Start game has been clicked"
						elif yPos >= 180 and yPos <= 240:
							numClicked = numClicked + 1
#							print "Highscores has been clicked"
						elif yPos >= 240 and yPos <= 300:
							numClicked = numClicked + 1
#							print "Exit game has been clicked"
							sys.exit()
							print str(totalClicks) + " , " + str(numClicked)
				if event.type == pygame.QUIT:
					sys.exit()
			pygame.display.flip()

	def drawField(self):
		#Make screen
		size = width, height = 640, 480
		self.fieldScreen = pygame.display.set_mode(size)
		#Make surface
		self.fieldSurface = pygame.Surface(size)
		self.fieldSurface.fill(Renderer.black)
		#Draw grid
		grey = 96, 96, 96
		for c in range(0, 16):
			pygame.draw.line(self.fieldSurface, grey, [c*30+15, 15], [c*30+15, 15*30+15])
			pygame.draw.line(self.fieldSurface, grey, [15, c*30+15], [15*30+15, c*30+15])
		self.fieldScreen.blit(self.fieldSurface, (0,0))
		#Draw buttons
		fieldButtons = ['res/Pause.png', 'res/Exit.png']
		for x in range (0, len(fieldButtons)):
			pathField = fieldButtons[x]
			imageField = pygame.image.load(pathField)
			self.fieldSurface.blit(imageField, (488, 15+x*65))
		self.fieldScreen.blit(self.fieldSurface, (0,0))
		#Draw "Score:"
		scoreFont = pygame.font.SysFont("Arial", 30)
		scoreText = scoreFont.render("Score: ", True, Renderer.white)
		self.fieldSurface.blit(scoreText, (510, 365))
		self.fieldScreen.blit(self.fieldSurface, (0, 0))
		
		
		self.drawCandy((45, 15))
		#self.drawSnake((15, 45))
#		while True:
#			for event in pygame.event.get():
#				if event.type == pygame.MOUSEBUTTONDOWN:
#					pos = pygame.mouse.get_pos()
#					xPos = pos[0]
#					yPos = pos[1]
#					if xPos >= 488 and xPos <= 618:
#						if yPos >= 15 and yPos <= 65:
#							self.drawPauseOverlay()
#						elif yPos >= 80 and yPos <= 130:
 #                                                       sys.exit()
#			pygame.display.flip()
	
	def drawPauseOverlay(self):		
		self.printScore('Pause')
                #Make overlay
                s = pygame.Surface((640,480))
                s.set_alpha(128)
                s.fill(Renderer.black)
                #fieldScreen.blit(s, (0,0))
                #Make text "Game paused" on overlay
                font = pygame.font.SysFont("Arial", 40)
                gamePausedLabel = font.render("Game paused", 1, Renderer.white)
                font = pygame.font.SysFont("Arial", 20)
                pressPLabel = font.render("Press [P] to continue", 1, Renderer.white)
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
					if count>1:
						count = 0
						self.drawInGame()
										

	def drawGameOverOverlay(self):
		printScore("Game Over")
		
	def printScore(self, score):
		#First make black overlay because maybe an old score has been printed already?
		
		#Print score beneath "Score:" label
		scoreFont = pygame.font.SysFont("Arial", 30)
		scoreNum = scoreFont.render(score, True, Renderer.white)
		self.fieldScreen.blit(scoreNum, (510, 400))		

if __name__ == "__main__":
	rendererx = Renderer(Renderer.states[2])
	renderer = rendererx.drawSnake((15,15))
