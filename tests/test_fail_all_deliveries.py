from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestFailAllDeliveries(FullMachineTestCase):

    def test_fail_all_deliveries(self):
        self._start_game()
        self._verify_cryolab_mode()
        self._exit_cryolab_to_base()
        self._light_moon_delivery()
        self._start_moon_delivery()
        self._exit_moon_to_base()
        self._light_cannibalon_delivery()
        self._do_cannibalon_delivery()
        self._light_robot_homeworld_delivery()
        self._start_robot_homeworld_delivery()
        self._exit_robot_homeworld_to_base()
        self._light_roswell_delivery()
        self._start_roswell_delivery()
        self._end_roswell_delivery()

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

    def _exit_cryolab_to_base(self):
        self.hit_and_release_switch("s_t_fry")
        self.advance_time_and_run(50)
        self.assertModeNotRunning("cryolab_delivery")
        self.assertPlayerVarEqual("failed", "cryolab_delivery_status")
        self.assertModeRunning("delivery_manager")
        self.assertModeRunning("crew_manager")
        self.assertModeRunning("slurm_caps")

    def _light_moon_delivery(self):
        self.hit_switch_and_run("s_dt_nibbler", 3)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(3)

    def _start_moon_delivery(self):
        self.hit_switch_and_run("s_VUK", 5)
        self.assertEqual("start", self.machine.state_machines.moon_delivery_state.state)
        self.post_event("flipper_cradle", 4)
        self.assertEqual("step1", self.machine.state_machines.moon_delivery_state.state)

    def _exit_moon_to_base(self):
        self.advance_time_and_run(30)
        self.assertModeNotRunning("moon_delivery")
        self.assertPlayerVarEqual("failed", "moon_delivery_status")
        self.assertModeRunning("delivery_manager")
        self.assertModeRunning("crew_manager")
        self.assertModeRunning("slurm_caps")
        self.assertEqual(0, self.machine.ball_devices.bd_VUK.balls)

    def _light_cannibalon_delivery(self):
        self.assertEqual("start", self.machine.state_machines.fuel_gauge_state.state)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.assertEqual("full", self.machine.state_machines.fuel_gauge_state.state)
        self.assertEqual("cannibalon_delivery_enable", self.machine.state_machines.cannibalon_delivery_handler.state)

    def _do_cannibalon_delivery(self):
        self.hit_switch_and_run("s_VUK", 5)
        self.assertEqual("cannibalon_delivery_active", self.machine.state_machines.cannibalon_delivery_handler.state)
        self.advance_time_and_run(17)
        self.assertEqual("cannibalon_delivery_done", self.machine.state_machines.cannibalon_delivery_handler.state)

    def _light_robot_homeworld_delivery(self):
        self.assertEqual("start", self.machine.state_machines.fuel_gauge_state.state)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.assertEqual("full", self.machine.state_machines.fuel_gauge_state.state)
        self.assertEqual("robot_homeworld_delivery_enable", self.machine.state_machines.robot_homeworld_delivery_handler.state)

    def _start_robot_homeworld_delivery(self):
        self.hit_switch_and_run("s_VUK", 35)
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'reusable_delivery_slide')
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'RH_delivery_instructions_slide')
        self.assertEqual("robot_homeworld_delivery_active", self.machine.state_machines.robot_homeworld_delivery_handler.state)

    def _exit_robot_homeworld_to_base(self):
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(25)
        self.hit_switch_and_run("s_trough1", 20)
        self.assertModeNotRunning("robot_homeworld_delivery")
        self.assertPlayerVarEqual("failed", "robot_homeworld_delivery_status")
        self.hit_and_release_switch("s_shooter_lane")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(1)
        self.assertEqual(1, self.machine.playfield.balls)
        self.advance_time_and_run(3)
        self.assertModeRunning("delivery_manager")
        self.assertModeRunning("crew_manager")
        self.assertModeRunning("slurm_caps")
        self.assertEqual(0, self.machine.ball_devices.bd_VUK.balls)
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'base_slide')
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')
        self.assertNotEqual("ignore", self.machine.state_machines.mom_zapp_toggle_state.state)

    def _light_roswell_delivery(self):
        self.assertEqual("start", self.machine.state_machines.fuel_gauge_state.state)
        self.assertEqual("roswell_delivery_next", self.machine.state_machines.roswell_delivery_handler.state)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.assertEqual("full", self.machine.state_machines.fuel_gauge_state.state)
        self.assertEqual("roswell_delivery_enable", self.machine.state_machines.roswell_delivery_handler.state)

    def _start_roswell_delivery(self):
        self.hit_switch_and_run("s_VUK", 20)
        self.assertEqual("roswell_delivery_active", self.machine.state_machines.roswell_delivery_handler.state)
        self.assertModeRunning("roswell_delivery")
        self.assertPlayerVarEqual("no", "did_nasty_in_the_pasty")

    def _end_roswell_delivery(self):
        self.advance_time_and_run(25)
        self.hit_switch_and_run("s_trough1", 20)
        self.hit_and_release_switch("s_shooter_lane")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(1)
        self.assertModeNotRunning("roswell_delivery")
        self.assertPlayerVarEqual("failed", "roswell_delivery_status")
        self.assertPlayerVarEqual("no", "did_nasty_in_the_pasty")
        self.assertEqual(1, self.machine.playfield.balls)
        self.advance_time_and_run(3)
        self.assertModeRunning("delivery_manager")
        self.assertModeRunning("crew_manager")
        self.assertModeRunning("slurm_caps")
        self.assertEqual(0, self.machine.ball_devices.bd_VUK.balls)
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'base_slide')
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')
        self.assertEqual("start", self.machine.state_machines.fuel_gauge_state.state)
