from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestMomZappShotsAfterFailingCryolab(FullMachineTestCase):

    def test_mom_zapp_shots_after_failing_cryolab(self):
        self._start_game()
        self._verify_cryolab_mode_and_wait()
        self._exit_to_base_mode()
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

    def _verify_cryolab_mode_and_wait(self):
        self.advance_time_and_run(3)
        self.assertModeRunning("cryolab_delivery")
        self.assertModeNotRunning("delivery_manager")
        self.assertModeNotRunning("crew_manager")
        self.assertModeNotRunning("slurm_caps")
        self.assertEqual("panuccis", self.machine.state_machines.cryolab_delivery_state.state)
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'cryolab_delivery_slide')
        self.advance_time_and_run(30)
        self.assertPlayerVarEqual("failed", "cryolab_delivery_status")

    def _exit_to_base_mode(self):
        self.advance_time_and_run(10)
        self.assertModeNotRunning("cryolab_delivery")
        self.assertModeRunning("delivery_manager")
        self.assertModeRunning("crew_manager")
        self.assertModeRunning("slurm_caps")
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'base_slide')
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')
        self.assertNotEqual("ignore", self.machine.state_machines.mom_zapp_toggle_state.state)

#there's a bit of variety to what happens before/after hitting the mom/zapp shots
#in the following steps, this is done intentionally
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
