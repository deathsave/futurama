from mpf.core.mode import Mode
from mpf.platforms.pololu import pololu_tic
from mpf.platforms.pololu import pololu_ticcmd_wrapper

class Attract(Mode):

    def mode_start(self, **kwargs):
        del kwargs
        self._serial_number = "00427235"
        pololu_tic.PololuTiccmdWrapper._run_subprocess_ticcmd(self, "--halt-and-set position 0")


#previously tried:
#self.platforms.pololu.pololu_ticcmd_wrapper._ticcmd(self, "--halt-and-set-position 0")
