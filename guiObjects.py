class Button(pygame.sprite.Sprite):
	
	def __init__(self, left, top, width, height):
		pygame.sprite.Sprite.__init__(self)
		self.rect = pygame.Rect(left, top, width, height)
		
