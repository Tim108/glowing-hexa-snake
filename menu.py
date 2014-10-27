#GUI for the main menu of glowing-hexa-snake
#Based on the sample of cocos2d @ http://cocos2d.org

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pyglet
from pyglet.gl import *

from cocos.director import *
from cocos.menu import *
from cocos.scene import *
from cocos.layer import *
from cocos.actions import *

class MainMenu(Menu):
    def __init__( self ):

        # call superclass with the title
        super( MainMenu, self ).__init__("Glowing-Hexa-Snake" )

        pyglet.font.add_directory('.')

        # you can override the font that will be used for the title and the items
        self.font_title['font_name'] = 'You Are Loved'
        self.font_title['font_size'] = 40
	self.font_title['color'] = (0,185,0,255)
        self.font_item['font_name'] = 'You Are Loved'
        self.font_item_selected['font_name'] = 'You Are Loved'
	self.font_item_selected['color'] = (0,185,0,255)	
        # you can also override the font size and the colors. see menu.py for
        # more info

        # example: menus can be vertical aligned and horizontal aligned
        self.menu_valign = TOP
        self.menu_halign = LEFT

        items = []

        items.append( MenuItem('New Game', self.on_new_game ) )
        items.append( MenuItem('Options', self.on_options ) )
        items.append( MenuItem('Scores', self.on_scores ) )
        items.append( MenuItem('Quit', self.on_quit ) )

	self.create_menu( items )	

    # Callbacks
    def on_new_game( self ):
        self.parent.switch_to( 3 )

    def on_scores( self ):
        self.parent.switch_to( 2 )

    def on_options( self ):
        self.parent.switch_to( 1 )

    def on_quit( self ):
        director.pop()


class OptionMenu(Menu):
    def __init__( self ):
        super( OptionMenu, self ).__init__("Glowing-Hexa-Snake" )

        self.font_title['font_name'] = 'You Are Loved'
        self.font_title['font_size'] = 40
	self.font_title['color'] = (0,185,0,255)
        self.font_item['font_name'] = 'You Are Loved'
        self.font_item_selected['font_name'] = 'You Are Loved'
	self.font_item_selected['color'] = (0,185,0,255)
        self.menu_valign = TOP
        self.menu_halign = LEFT

        items = []
        items.append( MenuItem('Fullscreen', self.on_fullscreen) )
        items.append( ToggleMenuItem('Show FPS: ', self.on_show_fps, True) )
        items.append( MenuItem('OK', self.on_quit) )

	self.create_menu(items)	
    # Callbacks
    def on_fullscreen( self ):
        director.window.set_fullscreen( not director.window.fullscreen )

    def on_quit( self ):
        self.parent.switch_to( 0 )

    def on_show_fps( self, value ):
        director.show_FPS = value

class ScoreMenu(Menu):
    def __init__( self ):
        super( ScoreMenu, self ).__init__("Glowing-Hexa-Snake" )

        self.font_title['font_name'] = 'You Are Loved'
        self.font_title['font_size'] = 40
	self.font_title['color'] = (0,185,0,255)
        self.font_item['font_name'] = 'You Are Loved'
        self.font_item_selected['font_name'] = 'You Are Loved'
	self.font_item_selected['color'] = (0,185,0,255)
        self.menu_valign = TOP
        self.menu_halign = LEFT

        self.create_menu( [MenuItem('Go Back', self.on_quit)] )

    def on_quit( self ):
        self.parent.switch_to( 0 )

class Ingame(Menu):
    def __init__( self ):
        super( Ingame, self ).__init__("Ingame zeg ik u!" )

        self.font_title['font_name'] = 'You Are Loved'
        self.font_title['font_size'] = 40
        self.font_title['color'] = (0,185,0,255)
        self.font_item['font_name'] = 'You Are Loved'
        self.font_item_selected['font_name'] = 'You Are Loved'
        self.font_item_selected['color'] = (0,185,0,255)
	self.font_item['font_size'] = 18
	self.font_item_selected['font_size'] = 18
        self.menu_valign = BOTTOM
        self.menu_halign = LEFT

	items = []
        items.append( MenuItem('Pause', self.on_pause) )
        items.append( MenuItem('Exit', self.on_quit) )
        self.create_menu(items)

    def on_quit( self ):
        self.parent.switch_to( 0 )

    def on_pause( self ):
	self.parent.switch_to( 0 )
	#do something?

def init():
    director.init( resizable=True, width=640, height=480)

def start():
    director.set_depth_test()

    menulayer = MultiplexLayer( MainMenu(), OptionMenu(), ScoreMenu(), Ingame() )
    
    scene =Scene( menulayer )

    return scene

def run(scene):
    director.run( scene )

if __name__ == "__main__":
    init()
    s = start()
    run(s)
