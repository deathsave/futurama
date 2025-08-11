from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase

from mpf.tests.MpfGameTestCase import MpfGameTestCase

class TestFourPlayerMaxS1(FullMachineTestCase):

    def test_four_player_max(self):
        self._start_game()

    def _start_game(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_shooter_lane")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(1)
        self.assertEqual(1, self.machine.playfield.balls)


class TestFourPlayerMaxS2(MpfGameTestCase):

    def _test_exactly_one_player(self):
        self.assertPlayerCount(1)

class TestFourPlayerMaxS3(FullMachineTestCase):

    def _add_player2(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(2)

class TestFourPlayerMaxS4(MpfGameTestCase):

    def _test_exactly_two_players(self):
        self.assertPlayerCount(2)

class TestFourPlayerMaxS5(FullMachineTestCase):

    def _add_player3(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(2)

class TestFourPlayerMaxS6(MpfGameTestCase):

    def _test_exactly_three_players(self):
        self.assertPlayerCount(3)

class TestFourPlayerMaxS7(FullMachineTestCase):

    def _add_player4(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(2)

class TestFourPlayerMaxS8(MpfGameTestCase):

    def _test_exactly_four_players(self):
        self.assertPlayerCount(4)

class TestFourPlayerMaxS9(FullMachineTestCase):

    def _try_player5(self):
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(2)

class TestFourPlayerMaxS10(MpfGameTestCase):

    def _test_still_exactly_four_players(self):
        self.assertPlayerCount(4)
