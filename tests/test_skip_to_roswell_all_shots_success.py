from mpf.tests.MpfMachineTestCase import MpfMachineTestCase
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

class TestSkipToRoswellAllShotsSuccess(FullMachineTestCase):

    def test_skip_to_roswell_all_shots_success(self):
        self._start_game()
        self._skip_to_roswell_and_verify()
        self._collect_bender_test_fry_ramp_shots()
#        self._progress_microwave_test_hopeless_search()
#        self._progress_zoidberg()
#        self._progress_enos()
#        self._progress_mildred()
#        self._steal_antenna_and_wrap_it_up()
#        self._test_successful_roswell_mode_exit()


    def _start_game(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_shooter_lane")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(1)
        self.assertEqual(1, self.machine.playfield.balls)

    def _skip_to_roswell_and_verify(self):
        self.post_event("test_roswell")
        self.advance_time_and_run(5)
        self.assertEqual("roswell_delivery_next", self.machine.state_machines.roswell_delivery_handler.state)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.assertEqual("roswell_delivery_enable", self.machine.state_machines.roswell_delivery_handler.state)
        self.hit_switch_and_run("s_VUK", 5)
        self.assertEqual("roswell_delivery_active", self.machine.state_machines.roswell_delivery_handler.state)

    def _collect_bender_test_fry_ramp_shots(self):
#run the clock to get through the intro
        self.advance_time_and_run(15)
        self.assertEqual("start", self.machine.state_machines.enos_state.state)
        self.assertEqual("start", self.machine.state_machines.mildred_state.state)
        self.assertEqual("start", self.machine.state_machines.zoidberg_roswell_state.state)
        self.assertEqual("start", self.machine.state_machines.bender_pieces_state.state)
        self.assertEqual("start", self.machine.state_machines.microwave_state.state)
        self.advance_time_and_run(20)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(1)
        self.assertEqual("one_pieces", self.machine.state_machines.bender_pieces_state.state)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(1)
        self.assertEqual("two_pieces", self.machine.state_machines.bender_pieces_state.state)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(1)
        self.assertEqual("three_pieces", self.machine.state_machines.bender_pieces_state.state)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(1)
        self.assertEqual("four_pieces", self.machine.state_machines.bender_pieces_state.state)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(2)
        self.assertEqual("five_pieces", self.machine.state_machines.bender_pieces_state.state)
        self.hit_and_release_switch("s_left_ramp")
        self.advance_time_and_run(2)
        self.assertEqual("its_enos", self.machine.state_machines.enos_state.state)
        self.hit_and_release_switch("s_right_ramp")
        self.advance_time_and_run(2)
        self.assertEqual("bayonets", self.machine.state_machines.enos_state.state)
