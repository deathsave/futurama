from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestMomZappAfterMoonModeAllShotsSuccess(FullMachineTestCase):

    def test_mom_zapp_after_moon_mode_all_shots_success(self):
        self._start_game()
        self._verify_cryolab_mode()
        self._nibbler_skillshot()
        self._exit_cryolab_to_base()
        self._light_moon_delivery()
        self._start_moon_delivery()
        self._deliver_crate()
        self._ride_whalers()
        self._lunar_rover()
        self._joyride()
        self._escape_farmer()
        self._find_lunar_lander()
        self._exit_moon_to_base()
        self._activate_mom_scene1()
        self._activate_zapp_scene1()
        self._activate_mom_scene2()
        self._activate_zapp_scene2()
        self._activate_mom_scene3()
        self._activate_zapp_scene3()
        self._activate_mom_scene4()
        self._activate_zapp_scene4()
        self._activate_mom_scene5()
        self._activate_zapp_scene5()

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

    def _start_moon_delivery(self):
        self.hit_switch_and_run("s_VUK", 5)
        self.assertEqual("start", self.machine.state_machines.moon_delivery_state.state)
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'moon_delivery_intro_slide')
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'delivery_instructions_slide')
        self.assertNotEqual("ignore", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.post_event("flipper_cradle", 4)
        self.assertEqual("step1", self.machine.state_machines.moon_delivery_state.state)

    def _deliver_crate(self):
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(5)
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'crate_delivered_slide')
        self.advance_time_and_run(10)
        self.assertPlayerVarEqual("success", "moon_delivery_status")
        self.assertEqual("step2", self.machine.state_machines.moon_delivery_state.state)

    def _ride_whalers(self):
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'moon_delivery_slide')
        self.hit_and_release_switch("s_right_loop")
        self.advance_time_and_run(5)
        self.hit_and_release_switch("s_left_loop")
        self.advance_time_and_run(5)
        self.assertEqual("step3", self.machine.state_machines.moon_delivery_state.state)

    def _lunar_rover(self):
        self.advance_time_and_run(3)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(24)
        self.assertEqual("step4", self.machine.state_machines.moon_delivery_state.state)

    def _joyride(self):
        self.hit_and_release_switch("s_pe_platter")
        self.advance_time_and_run(30)
        self.assertEqual("step5", self.machine.state_machines.moon_delivery_state.state)

    def _escape_farmer(self):
        self.hit_and_release_switch("s_t_fry")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_t_leela")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_t_bender")
        self.advance_time_and_run(14)
        self.assertEqual("step6", self.machine.state_machines.moon_delivery_state.state)

    def _find_lunar_lander(self):
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(3)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(3)
        self.hit_switch_and_run("s_VUK", 4)
        self.assertEqual("steps_complete", self.machine.state_machines.moon_delivery_state.state)

    def _exit_moon_to_base(self):
        self.assertTrue(self.machine.ball_holds.final_scene_hold.is_full)
        self.advance_time_and_run(30)
        self.assertModeNotRunning("moon_delivery")
        self.assertModeRunning("delivery_manager")
        self.assertModeRunning("crew_manager")
        self.assertModeRunning("slurm_caps")
        self.assertEqual(0, self.machine.ball_devices.bd_VUK.balls)
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'base_slide')
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')
        self.assertNotEqual("ignore", self.machine.state_machines.mom_zapp_toggle_state.state)

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
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'its_mom_slide')

    def _activate_zapp_scene1(self):
        self.assertPlayerVarEqual(1, "zapp_multiplier")
        self.assertEqual("mom", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(2) #leaving off s_left_inlane intentionally for variety in testing
        self.assertEqual("zapp", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "zapp_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'the_zapp_brannigan_slide')

    def _activate_mom_scene2(self):
        self.assertEqual("zapp", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.assertPlayerVarEqual(2, "mom_multiplier")
        self.hit_switch_and_run("s_VUK", 3)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_left_inlane")
        self.assertEqual("mom", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(2)
        self.assertPlayerVarEqual(3, "mom_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'moms_robot_oil_slide')

    def _activate_zapp_scene2(self):
        self.assertPlayerVarEqual(2, "zapp_multiplier")
        self.assertEqual("mom", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(20) #longer for testing variety
        self.assertEqual("zapp", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(3, "zapp_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'zapp_and_kif_slide')

    def _activate_mom_scene3(self):
        self.assertEqual("zapp", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.assertPlayerVarEqual(3, "mom_multiplier")
        self.hit_and_release_switch("s_t_fry")
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_left_inlane")
        self.assertEqual("mom", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(2)
        self.assertPlayerVarEqual(4, "mom_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'mom_suit_slide')
        self.advance_time_and_run(15)

    def _activate_zapp_scene3(self):
        self.assertPlayerVarEqual(3, "zapp_multiplier")
        self.assertEqual("mom", self.machine.state_machines.mom_zapp_toggle_state.state)
        #lets toggle that back and forth again for variety in testing
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(2)
        self.assertEqual("zapp", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_left_ramp")
        self.hit_and_release_switch("s_left_inlane")
        self.advance_time_and_run(2)
        self.assertEqual("mom", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_left_ramp")
        self.hit_and_release_switch("s_right_sling")
        self.assertEqual("zapp", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(4, "zapp_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'zapp_velour_slide')

    def _activate_mom_scene4(self):
        self.assertEqual("zapp", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.assertPlayerVarEqual(4, "mom_multiplier")
        self.hit_switch_and_run("s_VUK", 3)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_left_inlane")
        self.assertEqual("mom", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(2)
        self.assertPlayerVarEqual(5, "mom_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'mom_wont_rest_slide')

    def _activate_zapp_scene4(self):
        self.assertPlayerVarEqual(4, "zapp_multiplier")
        self.assertEqual("mom", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(2)
        self.assertEqual("zapp", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(5, "zapp_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'zapp_tries_seductive_slide')

    def _activate_mom_scene5(self):
        self.assertEqual("zapp", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.assertPlayerVarEqual(5, "mom_multiplier")
        self.hit_switch_and_run("s_VUK", 3)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_left_inlane")
        self.assertEqual("mom", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(2)
        self.assertPlayerVarEqual(6, "mom_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'mom_what_needs_to_be_done_slide')

    def _activate_zapp_scene5(self):
        self.assertPlayerVarEqual(5, "zapp_multiplier")
        self.assertEqual("mom", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(2)
        self.assertEqual("zapp", self.machine.state_machines.mom_zapp_toggle_state.state)
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(6, "zapp_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'zapp_25_star_general_slide')
