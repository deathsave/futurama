from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestGeneral(MpfMachineTestCase):

    def test_game_start(self):
        self.assertModeRunning("attract")
        self.assertModeNotRunning("base")
        self.assertModeNotRunning("game")

        # Player starts the game and puts a
        # ball into the shooter lane
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(1)
        self.assertEqual(2,
            self.machine.ball_devices["bd_trough"].balls)
        self.assertEqual(1,
            self.machine.ball_devices["bd_plunger"].balls)
        self.assertEqual(0, self.machine.playfield.balls)
        self.assertModeRunning("base")
        self.assertModeRunning("game")

        # Player puts the ball into play
        self.hit_and_release_switch("s_shooter_lane")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_cap1")
        self.advance_time_and_run(1)
        self.assertEqual(2,
            self.machine.ball_devices["bd_trough"].balls)
        self.assertEqual(0,
            self.machine.ball_devices["bd_plunger"].balls)
        self.assertEqual(1, self.machine.playfield.balls)
