from mpf.core.mode import Mode

class Attract(Mode):

    def mode_start(self, **kwargs):
        if (self.core.platform_controller._check_and_get_platform != "smart_virtual"):
            self.platforms.pololu.pololu_ticcmd_wrapper._ticcmd(self, "--halt-and-set-position, 0")