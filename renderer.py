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
			time.sleep(1)
			pygame.display.flip()

	def drawField(self):
		#Make screen
		size = width, height = 640, 480
		black = 0, 0, 0
		white = 255, 255, 255
		fieldScreen = pygame.display.set_mode(size)
		#Make surface
		fieldSurface = pygame.Surface(size)
		fieldSurface.fill(black)
		#Draw grid
		grey = 96, 96, 96
		for c in range(0, 16):
			pygame.draw.line(fieldSurface, grey, [c*30+15, 15], [c*30+15, 15*30+15])
			pygame.draw.line(fieldSurface, grey, [15, c*30+15], [15*30+15, c*30+15])
		fieldScreen.blit(fieldSurface, (0,0))
		#Draw buttons
		fieldButtons = ['res/Pause.png', 'res/Reset.png', 'res/Exit.png']
		for x in range (0, len(fieldButtons)):
			pathField = fieldButtons[x]
			imageField = pygame.image.load(pathField)
			fieldSurface.blit(imageField, (488, 15+x*65))
		fieldScreen.blit(fieldSurface, (0,0))
		#Draw "Score:"
		scoreFont = pygame.font.SysFont("Arial", 30)
		scoreText = scoreFont.render("Score: ", True, white)
		fieldScreen.blit(scoreText, (510, 365))
		#Draw snake
		
		

if __name__ == "__main__":
	renderer = Renderer()
