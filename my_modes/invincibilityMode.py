import procgame.game
from procgame.game import AdvancedMode
#TODO fix this
class invincibilityMode(procgame.game.AdvancedMode):

    def __init__(self, game):
        super(invincibilityMode, self).__init__(game=game,
        priority=11, mode_type=AdvancedMode.Manual) # 11 is the highest so far
        # stuff that gets done EXACTLY once.
        # happens when the "parent" Game creates this mode



        #TODO ballsaver4
        #self.game.enable._ball_saver() SkeletonGame and seconds 




    def mode_started(self):
        self.delay(name = "next_target",delay = 1,handler=self.timerCall)
        pass
    def being(self):
        self.game.displayText("This is a test")
    def timerCall(self):

        self.game.lamps.standupRightT.disable()
        self.game.lamps.standupRightM.disable()
        self.game.lamps.standupRightB.disable()
        self.game.displayText("invincibilityMode over")
