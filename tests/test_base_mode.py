from mpf.tests.MpfGameTestCase import MpfGameTestCase

class TestBaseMode(MpfGameTestCase):

    def test_base_mode(self):
        self.assertModeRunning("attract")
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        # TODO: this fails due to the game crashing
        #       on the stepper config
        self.assertModeRunning("game")
