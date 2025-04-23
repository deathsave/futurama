from mpf.modes.attract.code.attract import Attract

class FuturamaAttract(Attract):

    def mode_start(self, **kwargs):
        stepper = self.machine.steppers['zoidberg_stepper']
        stepper.move_to_position(0)
        super().mode_start(**kwargs)
