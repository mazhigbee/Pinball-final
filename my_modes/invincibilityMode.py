import procgame.game
from procgame.game import AdvancedMode

class invincibilityMode(procgame.game.AdvancedMode):
  """
  left chase loop
  """
  def __init__(self, game):
    super(invincibilityMode, self).__init__(game=game,
      priority=11, mode_type=AdvancedMode.Manual) # 11 is the highest so far
    # stuff that gets done EXACTLY once.
    # happens when the "parent" Game creates this mode
    pass

def mode_started(self):
    self.lamps.
    pass
