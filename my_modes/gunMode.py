import procgame.game
from procgame.game import AdvancedMode
#TODO
class gunMode(procgame.game.AdvancedMode):
  """
  left chase loop
  """

  def __init__(self, game):
     super(gunMode, self).__init__(game=game,
     priority=13, mode_type=AdvancedMode.Ball) # 11 is the highest so far
    # stuff that gets done EXACTLY once.
    # happens when the "parent" Game creates this mode
     pass
     def mode_started(self):
         self.counter = 0

         pass


  def gunMode(self):
      #TODO enable drop target and allow user to shooter
      #enable invincibilityMode
      #if gun hits give superjackpot of 50mil
      pass
  def sw_rampLeftMade_active(self):
      if(self.counter == 0):
         self.lamps.checkpointL.enable()
         self.counter = self.counter + 1
         return
      if(self.counter == 1):
         self.lamps.passcodeL.enable()
         self.counter = self.counter + 1
         return
      if(self.counter == 2):
         self.lamps.silentAlarmL.enable()
         self.counter = self.counter + 1
         return
      if(self.counter == 3):
         self.lamps.vaultKeyL.enable()
         self.counter = self.counter + 1
         return
      if(self.counter == 4):
         self.lamps.cpuLitL.enable()
         #TODO: activate gun
         self.counter = 0
         gunMode()
