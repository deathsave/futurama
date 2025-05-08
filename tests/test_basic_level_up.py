from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestBasicLevelUp(FullMachineTestCase):

    def test_basic_level_up(self):
        self._start_game()
        self._verify_cryolab_mode()
        self._nibbler_skillshot()
        self._exit_cryolab_to_base()
        self._fry_level2()
        self._fry_level3()
        self._leela_level2()
        self._leela_level3()
        self._bender_level2()
        self._bender_level3()
        self._nibbler_level2()
        self._nibbler_level3()
        self._hermes_level2()
        self._hermes_level3()
        self._zoidberg_level2()
        self._zoidberg_level3()
        self._professor_level2()
        self._professor_level3()
        self._amy_level2()
        self._amy_level3()

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

    def _fry_level2(self):
        self.assertPlayerVarEqual(1, "fry_level")
        self.hit_and_release_switch("s_t_fry")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "fry_level")
        self.assertPlayerVarEqual(2, "fry_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'fry_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

#doing this the quick and dirty way, without using xp
    def _fry_level3(self):
        self.post_event("fry_level3")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(3, "fry_level")
        self.assertPlayerVarEqual(3, "fry_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'fry_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _leela_level2(self):
        self.post_event("leela_level2")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "leela_level")
        self.assertPlayerVarEqual(2, "leela_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'leela_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _leela_level3(self):
        self.post_event("leela_level3")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(3, "leela_level")
        self.assertPlayerVarEqual(3, "leela_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'leela_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _bender_level2(self):
        self.post_event("bender_level2")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "bender_level")
        self.assertPlayerVarEqual(2, "bender_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'bender_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _bender_level3(self):
        self.post_event("bender_level3")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(3, "bender_level")
        self.assertPlayerVarEqual(3, "bender_multiplier")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'bender_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _nibbler_level2(self):
        self.post_event("nibbler_level2")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "nibbler_level")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'nibbler_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _nibbler_level3(self):
        self.post_event("nibbler_level3")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(3, "nibbler_level")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'nibbler_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _hermes_level2(self):
        self.post_event("hermes_level2")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "hermes_level")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'hermes_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _hermes_level3(self):
        self.post_event("hermes_level3")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(3, "hermes_level")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'hermes_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _zoidberg_level2(self):
        self.post_event("zoidberg_level2")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "zoidberg_level")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'zoidberg_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _zoidberg_level3(self):
        self.post_event("zoidberg_level3")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(3, "zoidberg_level")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'zoidberg_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _professor_level2(self):
        self.post_event("professor_level2")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "professor_level")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'professor_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _professor_level3(self):
        self.post_event("professor_level3")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(3, "professor_level")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'professor_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _amy_level2(self):
        self.post_event("amy_level2")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(2, "amy_level")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'amy_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _amy_level3(self):
        self.post_event("amy_level3")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(3, "amy_level")
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'amy_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')
