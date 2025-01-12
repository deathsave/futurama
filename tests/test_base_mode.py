from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestBaseMode(MpfMachineTestCase):

    def test_base_mode(self):
        self._start_game()

        # Test base mode integration here...

    def _start_game(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_shooter_lane")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(1)
        self.assertEqual(1, self.machine.playfield.balls)
