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
		self.game.coils.knockDown.pulse()
		self.number = 1
		self.direction = 1
		self.game.sound.play_music('route_66')

		self.cancel_delayed("next_target")
		self.delay(name="hurry",delay=18,handler=self.hurry)
		self.delay(name="times_up", delay=25,handler = self.times_up)
		# self.delay(name = "hurry", delay = 10,handler = self.hurry)
  #       self.delay(name = "next_target",delay = 15,handler=self.timerCall)
		#drop target
	def mode_stopped(self):
		#self.game.coils.dropTarget.pulse()
		self.game.lamps.checkpointL.disable()
		self.game.lamps.passcodeL.disable()
		self.game.lamps.silentAlarmL.disable()
		self.game.lamps.vaultKeyL.disable()
		self.game.lamps.cpuLitL.disable()
		self.game.lamps.target1.disable()
		self.game.lamps.target2.disable()
		self.game.lamps.target3.disable()
		self.game.lamps.target4.disable()
		self.game.lamps.target5.disable()
		self.leftRampCounter = 0
		self.game.sound.fadeout_music()
		self.game.sound.play_music('overwatch_main', -1)

	def hurry(self):
		self.game.lamps.checkpointL.schedule(0xf0f0f0f0)
		self.game.lamps.passcodeL.schedule(0xf0f0f0f0)
		self.game.lamps.silentAlarmL.schedule(0xf0f0f0f0)
		self.game.lamps.vaultKeyL.schedule(0xf0f0f0f0)
		self.game.lamps.cpuLitL.schedule(0xf0f0f0f0)
	def times_up(self):
		if(self.game.shooter_mode in self.game.modes):
			self.game.modes.remove(self)

	def next_target(self):
		self.game.lamps["target%d" % self.number].disable()
		self.number = self.number + self.direction
		if(self.number == 5):
			self.direction = -1
		elif(self.number == 1):
			self.direction = 1
		#self.game.displayText("Hit target %d" % self.number)
		# self.game.lamps.target3.schedule(0xf0f0f0)
		self.game.lamps["target%d" % self.number].enable()
		self.delay(name="next_target", delay=0.5, handler=self.next_target)


	def checktarget(self, target_num):
		if(self.number == target_num):

			self.game.score(5000000)
			self.game.sound.play('fish_in_barrell')
		else:
			self.game.sound.play('mei_miss')
		self.game.modes.remove(self)
		return procgame.game.SwitchStop

	# Example of how to handle a switch hit
	def sw_target3_active(self, sw):
		return self.checktarget(3)

	def sw_target1_active(self, sw):
		return self.checktarget(1)

	def sw_target2_active(self, sw):
		return self.checktarget(2)

	def sw_target4_active(self, sw):
		return self.checktarget(4)

	def sw_target5_active(self, sw):
		return self.checktarget(5)
	def sw_ballPopper_active(self,sw):
		self.game.sound.play('high_noon')
		self.delay(name="next_target", delay=1.0, handler=self.next_target)