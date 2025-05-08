from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestBasicLevelUp(FullMachineTestCase):

    def test_basic_level_up(self):
        self._start_game()
        self._verify_cryolab_mode()
        self._nibbler_skillshot()
        self._exit_cryolab_to_base()
        self._fry_level2()
        self._fry_level3()

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
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'fry_level_up_slide')
        self.advance_time_and_run(8)
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')
