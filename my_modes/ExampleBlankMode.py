####
## Example of a blank mode

import procgame.game
from procgame.game import AdvancedMode

import pygame
from pygame.locals import *
from pygame.font import *

class ExBlankMode(procgame.game.AdvancedMode):
  """
  Example Mode
  """
  def __init__(self, game):
    super(ExBlankMode, self).__init__(game=game, priority=2, mode_type=AdvancedMode.Game) # 2 is higher than BGM
    # stuff that gets done EXACTLY once.
    # happens when the "parent" Game creates this mode
    pass
  
  def mode_started(self):
    print("My mode started")
    #self.game.displayText("hit the flashing target for bonus")
  
  def mode_stopped(self): 
    print("My mode ended")
    # do cleanup of the mode here. 

  # Example of how to handle a switch hit
  def sw_target1_active(self, sw):
    self.game.lamps.target1.enable()
    self.game.displayText("HIT")
    self.game.score(700)
    self.game.sound.play('sling')
    #return procgame.game.SwitchContinue
   # - or -
    return procgame.game.SwitchStop
  def sw_target2_active(self,sw):
    self.game.lamps.target2.enable()
    self.game.displayText("target 2")
    self.game.score(1400)
    self.game.sound.play('sling')
    return procgame.game.SwitchStop
  def sw_target3_active(self,sw):
    self.game.lamps.target2.enable()
    self.game.displayText("target 3")
    self.game.score(1400)
    self.game.sound.play('sling')
    return procgame.game.SwitchStop
  def sw_target4_active(self,sw):
    self.game.lamps.target2.enable()
    self.game.displayText("target 4")
    self.game.score(1400)
    self.game.sound.play('sling')
    return procgame.game.SwitchStop
  def sw_target5_active(self,sw):
    self.game.lamps.target2.enable()
    self.game.displayText("target 5")
    self.game.score(1400)
    self.game.sound.play('sling')
    return procgame.game.SwitchStop

  
   




