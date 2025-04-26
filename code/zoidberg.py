from mpf.core.custom_code import CustomCode
from mpf.platforms.pololu.pololu_ticcmd_wrapper import PololuTiccmdWrapper

class Zoidberg(CustomCode):

    def on_load(self):
        print("Loading Zoidberg tic homing reset")
        self.machine.events.add_handler('reset_zoidberg_stepper', self.reset_tic)

    def reset_tic(self, **kwargs):
        if 'smart_virtual' in self.machine.hardware_platforms:
            print("Skipping Zoidberg tic homing reset")
        else:
            print("Attempting Zoidberg tic homing reset")
            tic = PololuTiccmdWrapper("00427235", self.machine)
            tic.halt_and_set_position(0)
