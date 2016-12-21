import procgame.game
from procgame.game import AdvancedMode

class ChaseLoopMode(procgame.game.AdvancedMode):

	def __init__(self, game):
		super(ChaseLoopMode, self).__init__(game=game, priority=20, mode_type=AdvancedMode.Manual)
		pass

	def mode_started(self):
		self.game.lamps.chaseValue.schedule(0xff00ff00)
		self.scoreIncrease = 1000000
		self.game.sound.play_music('dorado', -1)
		self.delay(name="hurry", delay=15, handler=self.hurry_up)
		self.delay(name="over", delay=20, handler=self.times_up)

	def evt_ball_ending(self, (shoot_again, last_ball)):
		self.game.modes.remove(self)
		self.cancel_delayed("hurry")
		self.cancel_delayed("over")

	def hurry_up(self):
		self.game.sound.play('junkrat_tick_tock')
		self.game.lamps.chaseValue.schedule(0xF0F0F0F0)

	def times_up(self):
		self.game.sound.play_music('overwatch_main', -1)
		self.game.modes.remove(self.game.chase_loop_mode)
		self.game.lamps.standupMidL.disable()
		self.game.lamps.standupMidC.disable()
		self.game.lamps.standupMidR.disable()
		self.game.setPlayerState('standupSwitchL',False)
		self.game.setPlayerState('standupSwitchC',False)
		self.game.setPlayerState('standupSwitchR',False)


	def mode_stopped(self):
		self.game.lamps.chaseValue.disable()

	def sw_chaseLoopHigh_active(self, sw):
		self.game.sound.play('tracer_whee')
		self.game.displayText("Scored %d" % self.scoreIncrease)
		self.game.score(self.scoreIncrease)
		self.scoreIncrease *= 2
		return procgame.game.SwitchStop

