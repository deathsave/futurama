from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestNibblerSkillshotThenSlurmFactory(FullMachineTestCase):

    def test_cryolab_mode_path_nibbler_skillshot(self):
        self._start_game()
        self._verify_cryolab_mode()
        self._nibbler_skillshot()
        self._exit_to_base_mode()
        self._collect_30_slurm_caps()
        self._start_slurm_factory_mode()
        self._slurm_factory_level1()
        self._slurm_factory_level2()
        self._slurm_factory_level3()
        self._slurm_final_shot_then_exit_to_base()

    def _start_game(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_shooter_lane")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(1)
        self.assertEqual(1, self.machine.playfield.balls)
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'cryolab_delivery_slide')

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
        self.assertEqual(self.mc.targets['display1'].current_slide_name,
                         'base_slide')
        self.assertEqual(self.mc.targets['display2'].current_slide_name,
                         'PFD_base_slide')

    def _collect_30_slurm_caps(self):
        self.assertPlayerVarEqual(0, "caps_collected")
#if slurm caps is running in cryolab_delivery the above step will fail
        self.hit_and_release_switch("s_cap2")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap2")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap3")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap3")
        self.assertPlayerVarEqual(5, "caps_collected")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap2")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap2")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap3")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap3")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap2")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap2")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap3")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap3")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap2")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap2")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap3")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap3")
        self.advance_time_and_run(2)
        self.assertPlayerVarEqual(20, "caps_collected")
        self.hit_and_release_switch("s_cap2")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap2")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap3")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap3")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap2")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap2")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap3")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_cap3")
        self.advance_time_and_run(1)
        self.assertPlayerVarEqual(30, "caps_collected")
        self.assertEqual(true, self.machine.shots['start_slurm_factory_shot'].enabled)

    def _start_slurm_factory_mode(self):
        self.advance_time_and_run(2)

    def _slurm_factory_level1(self):
        self.advance_time_and_run(2)

    def _slurm_factory_level3(self):
        self.advance_time_and_run(2)

    def _slurm_final_shot_then_exit_to_base(self):
        self.advance_time_and_run(2)
