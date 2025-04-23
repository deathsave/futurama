from mpf.platforms.pololu.pololu_ticcmd_wrapper import PololuTiccmdWrapper
from mpf.modes.attract.code.attract import Attract

class FuturamaAttract(Attract):

    def mode_start(self, **kwargs):
        tic = PololuTiccmdWrapper("00427235", self.machine)
        tic._ticcmd("--halt-and-set-position 0")
        super().mode_start(**kwargs)
