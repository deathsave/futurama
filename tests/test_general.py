"""Tests General/Base Functionality"""

import os
from mpf.tests.MpfMachineTestCase import MpfMachineTestCase

class TestGeneral(MpfMachineTestCase):

    """Tests start-up sequence"""

    def get_config_file(self):
        return 'config.yaml'

    def get_machine_path(self):
        return os.path.abspath(os.path.join(
            os.path.realpath(__file__),
            os.pardir,os.pardir
        ))

    def test_start(self):
        self.assertModeRunning('attract')
        self.assertEqual(3,
            self.machine.ball_devices.bd_trough.balls)
