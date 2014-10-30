import pygame
import time
import sys

class Renderer(object):
	def __init__(self):
		pygame.init()

        	size = width, height = 640, 480
		black = 0, 0, 0
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
			mySurface.blit(myImage, (255, 180+b*60))

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
					if xPos >= 270 and xPos <= 370:
						if yPos >= 180 and yPos <= 230:
							numClicked = numClicked + 1
							self.drawField()
#							print "Start game has been clicked"
						elif yPos >= 240 and yPos <= 290:
							numClicked = numClicked + 1
#							print "Highscores has been clicked"
						elif yPos >= 300 and yPos <= 350:
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
		black = 0, 0, 0
		white = 255, 255, 255
		self.fieldScreen = pygame.display.set_mode(size)
		#Make surface
		fieldSurface = pygame.Surface(size)
		fieldSurface.fill(black)
		#Draw grid
		grey = 96, 96, 96
		for c in range(0, 16):
			pygame.draw.line(fieldSurface, grey, [c*30+15, 15], [c*30+15, 15*30+15])
			pygame.draw.line(fieldSurface, grey, [15, c*30+15], [15*30+15, c*30+15])
		self.fieldScreen.blit(fieldSurface, (0,0))
		#Draw buttons
		fieldButtons = ['res/Pause.png', 'res/Reset.png', 'res/Exit.png']
		for x in range (0, len(fieldButtons)):
			pathField = fieldButtons[x]
			imageField = pygame.image.load(pathField)
			fieldSurface.blit(imageField, (488, 15+x*65))
		self.fieldScreen.blit(fieldSurface, (0,0))
		#Draw "Score:"
		scoreFont = pygame.font.SysFont("Arial", 30)
		scoreText = scoreFont.render("Score: ", True, white)
		self.fieldScreen.blit(scoreText, (510, 365))

		while True:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					pos = pygame.mouse.get_pos()
					xPos = pos[0]
					yPos = pos[1]
					if xPos >= 488 and xPos <= 618:
						if yPos >= 15 and yPos <= 65:
							self.printScore('Pause')
							#Make overlay
							s = pygame.Surface((640,480))
							s.set_alpha(128)
							s.fill(black)
							#fieldScreen.blit(s, (0,0))
							#Make text "Game paused" on overlay
							font = pygame.font.SysFont("Arial", 40)
							gamePausedLabel = font.render("Game paused", 1, white)
							
							font = pygame.font.SysFont("Arial", 20)
							pressPLabel = font.render("Press [P] to continue", 1, white)
							
							xLoc = (640 - gamePausedLabel.get_width())/2
							yLoc = (480 - (pressPLabel.get_height() + gamePausedLabel.get_height()))/2

							s.blit(gamePausedLabel, (xLoc, yLoc))
	
							x2Loc = (640 - pressPLabel.get_width())/2
							y2Loc = (480 + pressPLabel.get_height())/2

							s.blit(pressPLabel, (x2Loc, y2Loc))
							self.fieldScreen.blit(s, (0, 0))

						elif yPos >= 80 and yPos <= 130:
							s = pygame.Surface((640,480))
                                                        s.set_alpha(128)
                                                        s.fill(black)
                                                        #fieldScreen.blit(s, (0,0))
                                                        #Make text "Game paused" on overlay
                                                        font = pygame.font.SysFont("Arial", 40)
                                                        gamePausedLabel = font.render("Game reset", 1, white)

                                                        font = pygame.font.SysFont("Arial", 20)
                                                        pressPLabel = font.render("Press [R] to restart", 1, white)

                                                        xLoc = (640 - gamePausedLabel.get_width())/2
                                                        yLoc = (480 - (pressPLabel.get_height() + gamePausedLabel.get_height()))/2

                                                        s.blit(gamePausedLabel, (xLoc, yLoc))

                                                        x2Loc = (640 - pressPLabel.get_width())/2
                                                        y2Loc = (480 + pressPLabel.get_height())/2

                                                        s.blit(pressPLabel, (x2Loc, y2Loc))
                                                        self.fieldScreen.blit(s, (0, 0))

							self.printScore('Reset')
						elif yPos >= 145 and yPos <= 205:
							sys.exit()
			pygame.display.flip()
			
		
	def printScore(self, score):
		white = 255, 255, 255
		#First make black overlay because maybe an old score has been printed already?
		
		#Print score beneath "Score:" label
		scoreFont = pygame.font.SysFont("Arial", 30)
		scoreNum = scoreFont.render(score, True, white)
		self.fieldScreen.blit(scoreNum, (510, 400))		

if __name__ == "__main__":
	rendererx = Renderer().drawField()
	renderer = Renderer().printScore(150)
