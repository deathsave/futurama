from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestMoonModeSuccessNoExtras(FullMachineTestCase):

    def test_moon_mode_success_no_extras(self):
        self._start_game()
        self._verify_cryolab_mode()
        self._nibbler_skillshot()
        self._exit_cryolab_to_base()
        self._light_moon_delivery()
        self._start_moon_delivery()
        self._deliver_crate_and_wait()
        self._exit_moon_to_base()
        self._light_cannibalon_delivery()
        self._do_cannibalon_delivery()

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

    def _exit_cryolab_to_base(self):
        self.advance_time_and_run(30)
        self.assertModeNotRunning("cryolab_delivery")
        self.assertModeRunning("delivery_manager")
        self.assertModeRunning("crew_manager")
        self.assertModeRunning("slurm_caps")
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'base_slide')
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')
        self.assertNotEqual("ignore", self.machine.state_machines.mom_zapp_toggle_state.state)

    def _light_moon_delivery(self):
        self.hit_switch_and_run("s_dt_nibbler", 3)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(3)
        self.assertEqual("full", self.machine.state_machines.fuel_gauge_state.state)

    def _start_moon_delivery(self):
        self.hit_switch_and_run("s_VUK", 5)
        self.assertEqual("start", self.machine.state_machines.moon_delivery_state.state)
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'moon_delivery_intro_slide')
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'delivery_instructions_slide')
        self.assertEqual("ignore", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.post_event("flipper_cradle", 4)
        self.assertEqual("step1", self.machine.state_machines.moon_delivery_state.state)

    def _deliver_crate_and_wait(self):
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(5)
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'crate_delivered_slide')
        self.advance_time_and_run(10)
        self.assertPlayerVarEqual("success", "moon_delivery_status")
        self.assertEqual("step2", self.machine.state_machines.moon_delivery_state.state)
        self.advance_time_and_run(10)

    def _exit_moon_to_base(self):
        self.advance_time_and_run(3)
        self.assertModeNotRunning("moon_delivery")
        self.assertEqual("start", self.machine.state_machines.fuel_gauge_state.state)
        self.assertModeRunning("delivery_manager")
        self.assertModeRunning("crew_manager")
        self.assertModeRunning("slurm_caps")
        self.assertEqual(0, self.machine.ball_devices.bd_VUK.balls)
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'base_slide')
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')
        self.assertNotEqual("ignore", self.machine.state_machines.mom_zapp_toggle_state.state)

    def _light_cannibalon_delivery(self):
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
