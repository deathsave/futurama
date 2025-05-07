from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestCryolabModePathAllShotsSuccess(MpfMachineTestCase):

    def test_cryolab_mode_path_all_shots_success(self):
        self._start_game()
        self._verify_cryolab_mode()
        self._ride_the_bike()
        self._lock_the_bike()
        self._deliver_pizza()
        self._fall_in_cryopod()
        self._long_exit_to_base_mode()

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
        self.assertEqual("panuccis",
            self.machine.state_machines.cryolab_delivery_state.state)

    def _ride_the_bike(self):
        self.hit_switch_and_run("s_left_ramp", 3)
        self.assertEqual("ride_bike",
            self.machine.state_machines.cryolab_delivery_state.state)

    def _lock_the_bike(self):
        self.hit_switch_and_run("s_right_loop", 3)
        self.assertEqual("lock_bike",
            self.machine.state_machines.cryolab_delivery_state.state)

    def _deliver_pizza(self):
        self.hit_switch_and_run("s_right_ramp", 3)
        self.assertEqual("i_c_weiner",
            self.machine.state_machines.cryolab_delivery_state.state)

    def _fall_in_cryopod(self):
        self.hit_switch_and_run("s_VUK", 3)
        self.assertEqual("fall_in_crypod",
            self.machine.state_machines.cryolab_delivery_state.state)

    def _long_exit_to_base_mode(self):
        self.advance_time_and_run(60)
        self.assertModeNotRunning("cryolab_delivery")
        self.assertModeRunning("delivery_manager")
        self.assertModeRunning("crew_manager")
        self.assertModeRunning("slurm_caps")
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'base_slide')
