import procgame.game
from procgame.game import AdvancedMode
#TODOPO
class gunMode(procgame.game.AdvancedMode):
  """
  gunMode
  """

  def __init__(self, game):
     super(gunMode, self).__init__(game=game,
     priority=13, mode_type=AdvancedMode.Ball) # 11 is the highest so far
    # stuff that gets done EXACTLY once.
    # happens when the "parent" Game creates this mode
     pass
  def mode_started(self):
     self.number = 0

  def runMode(self):
      self.game.lamps.checkpointL.schedule(0x00f00ff)
      self.game.lamps.passcodeL.schedule(0xf0f0f0f0)
      self.game.lamps.silentAlarmL.schedule(0xf00f0f)
      self.game.lamps.vaultKeyL.schedule(0x0ff0ff0)
      self.game.lamps.cpuLitL.schedule(0x0f00f0f0)


  def sw_rampLeftMade_active(self,sw):
      if(self.number == 0):
         self.game.lamps.checkpointL.enable()
         self.number = self.number + 1
         return
      if(self.number == 1):
         self.game.lamps.passcodeL.enable()
         self.number = self.number + 1
         return
      if(self.number == 2):
         self.game.lamps.silentAlarmL.enable()
         self.number = self.number + 1
         return
      if(self.number == 3):
         self.game.lamps.vaultKeyL.enable()
         self.number = self.number + 1
         return
      if(self.number == 4):
         self.game.lamps.cpuLitL.enable()
         #TODO: activate gun
         self.number = 0
         runMode();
