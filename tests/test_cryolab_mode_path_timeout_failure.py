from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestCryolabModePathTimeoutFailure(FullMachineTestCase):

    def test_cryolab_mode_path_timeout_failure(self):
        self._start_game()
        self._verify_cryolab_mode()
        self._wait_and_exit_to_base_mode()

    def _start_game(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_shooter_lane")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(1)
        self.assertEqual(1, self.machine.playfield.balls)

    def _verify_cryolab_mode(self):
        self.assertModeRunning("cryolab_delivery")
        self.assertModeNotRunning("delivery_manager")
        self.assertModeNotRunning("crew_manager")
        self.assertModeNotRunning("slurm_caps")
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'cryolab_delivery_slide')

    def _wait_and_exit_to_base_mode(self):
        self.advance_time_and_run(40)
        self.assertModeNotRunning("cryolab_delivery")
        self.assertModeRunning("delivery_manager")
        self.assertModeRunning("crew_manager")
        self.assertModeRunning("slurm_caps")
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'base_slide')
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')
        self.assertNotEqual("ignore", self.machine.state_machines.mom_zapp_toggle_state.state)
