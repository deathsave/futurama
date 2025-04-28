from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestMomZappShotsAfterCryolab(MpfMachineTestCase):

    def test_cryolab_mode_path_nibbler_skillshot(self):
        self._start_game()
        self._verify_cryolab_mode()
        self._nibbler_skillshot()
        self._exit_to_base_mode()
        self._activate_mom_scene1()

    def _start_game(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_shooter_lane")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(1)
        self.assertEqual(1, self.machine.playfield.balls)

    def _verify_cryolab_mode(self):
        self.advance_time_and_run(3)
        self.assertModeRunning("cryolab_delivery")
        self.assertModeNotRunning("delivery_manager")
        self.assertModeNotRunning("crew_manager")
        self.assertModeNotRunning("slurm_caps")
        self.assertEqual("panuccis", self.machine.state_machines.cryolab_delivery_state.state)

    def _nibbler_skillshot(self):
        self.hit_switch_and_run("s_VUK", 3)
        self.assertPlayerVarEqual("success", "cryolab_delivery_status")

    def _exit_to_base_mode(self):
        self.advance_time_and_run(30)
        self.assertModeNotRunning("cryolab_delivery")
        self.assertModeRunning("delivery_manager")
        self.assertModeRunning("crew_manager")
        self.assertModeRunning("slurm_caps")

    def _activate_mom_scene1(self):
        self.assertEqual("zapp", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.advance_time_and_run(30)
        self.assertPlayerVarEqual(1, "mom_multiplier")
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_left_inlane")
        self.assertEqual("mom", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(2)
        self.assertPlayerVarEqual(2, "mom_multiplier")
