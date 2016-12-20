import procgame.game
from procgame.game import AdvancedMode
#TODO fix this
class invincibilityMode(procgame.game.AdvancedMode):

    def __init__(self, game):
        super(invincibilityMode, self).__init__(game=game,
        priority=11, mode_type=AdvancedMode.Manual) # 11 is the highest so far
        # stuff that gets done EXACTLY once.
        # happens when the "parent" Game creates this mode



        #TODO ballsaver
        #self.game.enable_ball_saver() SkeletonGame and seconds




    def mode_started(self):
        self.game.sound.play('invin_sfx')
        self.game.displayText("Invincibility Mode Active!")
        self.game.sound.play_music('invin_active')
        self.delay(name = "hurry", delay = 10,handler = self.hurry)
        self.delay(name = "next_target",delay = 15,handler=self.timerCall)
        self.game.enable_ball_saver(15,5,True,True)
        pass
    def hurry(self):
        self.game.lamps.standupRightT.schedule(0xf00f00f0)
        self.game.lamps.standupRightM.schedule(0x0f00f00f)
        self.game.lamps.standupRightB.schedule(0x00f00f00)

    def timerCall(self):
    	self.game.setPlayerState('standupRT', False)
        self.game.setPlayerState('standupRM', False)
        self.game.setPlayerState('standupRB', False)
        self.game.lamps.standupRightT.disable()
        self.game.lamps.standupRightM.disable()
        self.game.lamps.standupRightB.disable()
        self.game.sound.play_music('overwatch-main')
        self.game.displayText("invincibilityMode over")
        self.game.disable_ball_saver()
        self.game.modes.remove(self.game.invincibility_mode)
