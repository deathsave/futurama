from mpf.core.custom_code import CustomCode
from mpf.platforms.pololu.pololu_ticcmd_wrapper import PololuTiccmdWrapper

class Zoidberg(CustomCode):

    def on_load(self):
        self._reset_tic()

    def _reset_tic(self):
        if 'smart_virtual' in self.machine.hardware_platforms:
            print("Skipping Zoidberg tic homing reset")
        else:
            tic = PololuTiccmdWrapper("00427235", self.machine)
            tic.halt_and_set_position(0)
            print("Zoidberg tic homing reset done")
