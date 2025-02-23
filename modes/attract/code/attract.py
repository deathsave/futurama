from mpf.core.mode import Mode

class Attract(Mode):

    def mode_start(self, **kwargs):
        self.platforms.pololu.pololu_ticcmd_wrapper._ticcmd(self, "--halt-and-set-position, 0")