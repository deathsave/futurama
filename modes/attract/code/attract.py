from mpf.platforms.pololu.pololu_ticcmd_wrapper import PololuTiccmdWrapper
from mpf.modes.attract.code.attract import Attract

class FuturamaAttract(Attract):

    def mode_start(self, **kwargs):

        if self.core.platform_controller._check_and_get_platform != "smart_virtual":
            self._reset_tic()          
        super().mode_start(**kwargs)

    def _reset_tic(self):
        print("Attract Mode Tic Stepper Reset")
        tic = PololuTiccmdWrapper("00427235", self.machine)
        tic.halt_and_set_position(0)
