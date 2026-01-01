from mpf.tests.MpfMachineTestCase import MpfMachineTestCase
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestCrewLevelUp(FullMachineTestCase):

    def test_crew_level_up(self):
        self._start_game()
        self._verify_cryolab_mode()
        self._ride_the_bike()
        self._lock_the_bike()
        self._deliver_pizza()
        self._fall_in_cryopod()
        self._long_exit_to_base_mode()
        self._bender_to_level2()
        self._fry_to_level2()
        self._leela_to_level2()
        self._suicide_booth_activation()
        self._amy_to_level2()
        self._runout_timer_on_PFx()
        self._zoidberg_to_level2()
        self._trigger_zoidberg_ball_save()
        self._hermes_to_level2()
        self._nibbler_to_level2()
        self._professor_to_level2()



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
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'cryolab_delivery_slide')
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
        self.assertPlayerVarEqual("success", "cryolab_delivery_status")

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
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')
        self.assertNotEqual("ignore", self.machine.state_machines.mom_zapp_toggle_state.state)

    def _bender_to_level2(self):
        self.assertPlayerVarEqual(1, "bender_level")
        self.assertPlayerVarEqual(1, "bender_multiplier")
        self.assertPlayerVarEqual(1, "crew_multiplier")
        self.assertModeNotRunning("suicide_booth")
        self.post_event("bender_level2")
        self.advance_time_and_run(1)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'bender_level_up_slide')
        self.assertPlayerVarEqual(2, "bender_level")
        self.assertPlayerVarEqual(2, "bender_multiplier")
        self.assertPlayerVarEqual(2, "crew_multiplier")
        self.assertModeRunning("suicide_booth")
        self.advance_time_and_run(9)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _fry_to_level2(self):
        self.assertPlayerVarEqual(1, "fry_level")
        self.assertPlayerVarEqual(1, "fry_multiplier")
        self.assertPlayerVarEqual(2, "crew_multiplier")
        self.post_event("fry_level2")
        self.advance_time_and_run(1)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'fry_level_up_slide')
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "fry_level")
        self.assertPlayerVarEqual(2, "fry_multiplier")
        self.assertPlayerVarEqual(3, "crew_multiplier")
        self.advance_time_and_run(9)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _leela_to_level2(self):
        self.assertPlayerVarEqual(1, "leela_level")
        self.assertPlayerVarEqual(1, "leela_multiplier")
        self.assertPlayerVarEqual(3, "crew_multiplier")
        self.post_event("leela_level2")
        self.advance_time_and_run(1)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'leela_level_up_slide')
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "leela_level")
        self.assertPlayerVarEqual(2, "leela_multiplier")
        self.assertPlayerVarEqual(4, "crew_multiplier")
        self.advance_time_and_run(9)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _suicide_booth_activation(self):
        self.assertModeRunning("suicide_booth")
        self.hit_and_release_switch("s_left_outlane")
        self.hit_switch_and_run("s_suicide_booth", 1)
        self.assertTrue(self.machine.ball_holds.suicide_booth_ball_hold.is_full)
        self.advance_time_and_run(3)
        self.hit_and_release_switch("s_left_outlane")
        self.assertEqual(0, self.machine.ball_devices.bd_suicide_booth.balls)
        self.advance_time_and_run(8)
        self.assertModeNotRunning("suicide_booth")

    def _amy_to_level2(self):
        self.assertPlayerVarEqual(1, "amy_level")
        self.assertPlayerVarEqual(1, "amy_multiplier")
        self.assertPlayerVarEqual(4, "crew_multiplier")
        self.post_event("amy_level2")
        self.advance_time_and_run(1)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'amy_level_up_slide')
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "amy_level")
        self.assertPlayerVarEqual(2, "amy_multiplier")
        self.assertPlayerVarEqual(5, "crew_multiplier")
        self.assertPlayerVarEqual(2, "PF_multiplier")
        self.advance_time_and_run(9)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _runout_timer_on_PFx(self):
        self.advance_time_and_run(30)
        self.assertPlayerVarEqual(1, "PF_multiplier")

    def _zoidberg_to_level2(self):
        self.assertPlayerVarEqual(1, "zoidberg_level")
        self.assertPlayerVarEqual(1, "zoidberg_multiplier")
        self.assertPlayerVarEqual(5, "crew_multiplier")
        self.post_event("zoidberg_level2")
        self.advance_time_and_run(1)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'zoidberg_level_up_slide')
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "zoidberg_level")
        self.assertPlayerVarEqual(2, "zoidberg_multiplier")
        self.assertPlayerVarEqual(6, "crew_multiplier")

    def _trigger_zoidberg_ball_save(self):
        self.advance_time_and_run(1)

    def _hermes_to_level2(self):
        self.advance_time_and_run(1)

    def _nibbler_to_level2(self):
        self.advance_time_and_run(1)

    def _professor_to_level2(self):
        self.advance_time_and_run(1)
