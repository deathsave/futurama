from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestRobotHomeworldModeAllShotsSuccess(MpfMachineTestCase):

    def test_robot_homeworld_mode_all_shots_success(self):
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
        self._advance_bender_to_level_4()
        self._light_robot_homeworld_delivery()
        self._start_robot_homeworld_delivery()
        self._lower_bender_with_winch()
        self._dress_up_like_robots()
        self._infiltrate_robot_city()
        self._human_hunt()
        self._escape_robot_city()
        self._deliver_lugnuts()
        self._exit_robot_homeworld_to_base()

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

    def _light_moon_delivery(self):
        self.hit_switch_and_run("s_dt_nibbler", 3)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(3)

    def _start_moon_delivery(self):
        self.hit_switch_and_run("s_VUK", 5)
        self.assertEqual("start", self.machine.state_machines.moon_delivery_state.state)
        self.post_event("flipper_cradle", 4)
        self.assertEqual("step1", self.machine.state_machines.moon_delivery_state.state)

    def _deliver_crate(self):
        self.hit_and_release_switch("s_r_orbit")
        self.advance_time_and_run(11)
        self.assertPlayerVarEqual("success", "moon_delivery_status")
        self.assertEqual("step2", self.machine.state_machines.moon_delivery_state.state)

    def _ride_whalers(self):
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

    def _advance_bender_to_level_4(self):
        self.post_event("bender_level2")
        self.post_event("bender_level3")
        self.post_event("bender_level4")
        self.assertPlayerVarEqual(4, "bender_level")

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
        self.hit_switch_and_run("s_VUK", 20)
        self.assertEqual("robot_homeworld_delivery_active", self.machine.state_machines.robot_homeworld_delivery_handler.state)

    def _lower_bender_with_winch(self):
        self.advance_time_and_run(15)
        self.assertEqual("lower_bender", self.machine.state_machines.robot_homeworld_delivery_state.state)

    def _dress_up_like_robots(self):
        self.advance_time_and_run(30)
        self.assertEqual("dress_up", self.machine.state_machines.robot_homeworld_delivery_state.state)
        self.hit_and_release_switch("s_t_fry")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_t_leela")
        self.advance_time_and_run(3)

    def _infiltrate_robot_city(self):
        self.assertEqual("infiltrate", self.machine.state_machines.robot_homeworld_delivery_state.state)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_right_loop")
        self.advance_time_and_run(3)

    def _human_hunt(self):
        self.assertEqual("human_hunt", self.machine.state_machines.robot_homeworld_delivery_state.state)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_right_loop")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_left_loop")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(5)

    def _escape_robot_city(self):
        self.assertEqual("escape", self.machine.state_machines.robot_homeworld_delivery_state.state)
        self.hit_and_release_switch("s_pe_platter")
        self.hit_and_release_switch("s_pe_platter")
        self.hit_and_release_switch("s_pe_platter")
        self.hit_and_release_switch("s_pe_platter")
        self.hit_and_release_switch("s_pe_platter")
        self.hit_and_release_switch("s_pe_platter")
        self.hit_and_release_switch("s_pe_platter")
        self.hit_and_release_switch("s_pe_platter")
        self.hit_and_release_switch("s_pe_platter")
        self.advance_time_and_run(2)

    def _deliver_lugnuts(self):
        self.hit_switch_and_run("s_VUK", 5)
        self.assertEqual("deliver_lugnuts", self.machine.state_machines.robot_homeworld_delivery_state.state)
        self.assertPlayerVarEqual("success", "robot_homeworld_delivery_status")

    def _exit_robot_homeworld_to_base(self):
        self.advance_time_and_run(20)
        self.assertModeNotRunning("robot_homeworld_delivery")
        self.assertModeRunning("delivery_manager")
        self.assertModeRunning("crew_manager")
        self.assertModeRunning("slurm_caps")
        self.assertEqual(0, self.machine.ball_devices.bd_VUK.balls)
