import procgame.game
from procgame.game import AdvancedMode
#TODOPO
class shooterMode(procgame.game.AdvancedMode):
	"""
	shooter
	"""

	def __init__(self, game):
		super(shooterMode, self).__init__(game=game,
		priority=13, mode_type=AdvancedMode.Manual) # 11 is the highest so far
		# stuff that gets done EXACTLY once.
		# happens when the "parent" Game creates this mode
		pass

	def mode_started(self):
		self.game.lamps.checkpointL.schedule(0x00f00ff)
		self.game.lamps.passcodeL.schedule(0xf0f0f0f0)
		self.game.lamps.silentAlarmL.schedule(0xf00f0f)
		self.game.lamps.vaultKeyL.schedule(0x0ff0ff0)
		self.game.lamps.cpuLitL.schedule(0x0f00f0f0)
		self.game.displayText("LOAD THE GUN")
		# self.delay(name = "hurry", delay = 10,handler = self.hurry)
  #       self.delay(name = "next_target",delay = 15,handler=self.timerCall)
		#drop target

	def times_up(self):
		self.leftRampCounter = 0
