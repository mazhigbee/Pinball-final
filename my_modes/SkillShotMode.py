import procgame.game
from procgame.game import AdvancedMode

class SkillshotMode(procgame.game.AdvancedMode):
  """
  Skill shot Mode
  """
  def __init__(self, game):
    super(SkillshotMode, self).__init__(game=game,
      priority=10, mode_type=AdvancedMode.Ball) # 10 is the highest so far
    # stuff that gets done EXACTLY once.
    # happens when the "parent" Game creates this mode
    pass

  """
  called when the mode is activated (added to the queue)
  """
  def mode_started(self):
    self.number = 1
    self.direction = 1
    self.cancel_delayed("next_target")
    self.delay(name="next_target", delay=1.0, handler=self.next_target)

  """
  a function that changes number by direction,
  keeping the number between 1 and 5; also displays
  the number on the screen
  """
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
    self.delay(name="next_target", delay=0.2, handler=self.next_target)

  def mode_stopped(self):
    self.game.lamps.target1.disable()
    self.game.lamps.target2.disable()
    self.game.lamps.target3.disable()
    self.game.lamps.target4.disable()
    self.game.lamps.target5.disable()
    self.game.sound.fadeout_music()
    self.game.sound.play_music('overwatch_main', -1)

  def evt_ball_starting(self):
    self.game.sound.stop_music()
    self.game.sound.play_music('skillshot')
    self.game.displayText("Hit the flashing target!")


  def sw_gripTrigger_active(self, sw):
    if(self.game.switches.shooter.is_active()):
      self.game.sound.play('skillshot_fire')
      self.game.coils.plunger.pulse()

  def checktarget(self, target_num):
    if(self.number == target_num):
      self.game.displayText("HOOKED")
      self.game.score(1000000)
      self.game.sound.play('hanzo_stronger')
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
