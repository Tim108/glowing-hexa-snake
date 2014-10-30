import pygame

class Renderer(object):
	def __init__(self):
		pygame.init()

        	size = width, height = 640, 480
        	black = 0, 0, 0

        	screen = pygame.display.set_mode(size)

		#Make surface
		mySurface = pygame.Surface((640,480))
		mySurface.fill(black)
		#Make color for rectangles
		myColor = pygame.Color(0, 188, 0)
		
		sizeXRect = 100
		sizeYRect = 50
		#Make rectangle
		xRect = 50
		yRect = 135
#		myRect = pygame.Rect(xRect, yRect, sizeXRect, sizeYRect)
		#draw 3 rectangles
#		pygame.draw.rect(mySurface, myColor, myRect, 1)
#		pygame.draw.rect(mySurface, myColor, myRect2, 1)
#		pygame.draw.rect(mySurface, myColor, myRect3, 1)
		#insert text on rectangles
		myFont = pygame.font.SysFont("Arial", 14)
#		startText = myFont.render("Start game", 255, (255, 255, 255))
		
		#Draw button and text on surface
		for i in [135, 195, 255]:
			myRect = pygame.Rect(xRect, i, sizeXRect, sizeYRect)
			pygame.draw.rect(mySurface, myColor, myRect, 1)
		j=0
		texts = ["Start game", "Highscores", "Exit game"]
		for x in range (0, len(texts)):
			j = texts[x]
			j = myFont.render(j, 255, (255, 255, 255))
			xText = int(0.5 * (100 - j.get_width()) + xRect)
			yText = int(0.5 * (50 - j.get_height()) + yRect + x*60)
			mySurface.blit(j, (xText, yText))
		
		screen.blit(mySurface, (0, 0))

        	while(True):
	            	for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			pygame.display.flip()

if __name__ == "__main__":
	renderer = Renderer()
