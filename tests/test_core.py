import threading
import time
import unittest

import telco


class TestCore(unittest.TestCase):
    def test_enumerate_devices(self):
        devices = telco.get_device_manager().enumerate_devices()
        self.assertTrue(len(devices) > 0)

    def test_get_existing_device(self):
        device = telco.get_device_matching(lambda d: d.id == "local")
        self.assertEqual(device.name, "Local System")

        device = telco.get_device_manager().get_device_matching(lambda d: d.id == "local")
        self.assertEqual(device.name, "Local System")

    def test_get_nonexistent_device(self):
        def get_nonexistent():
            telco.get_device_manager().get_device_matching(lambda device: device.type == "lol")

        self.assertRaisesRegex(telco.InvalidArgumentError, "device not found", get_nonexistent)

    def test_wait_for_nonexistent_device(self):
        def wait_for_nonexistent():
            telco.get_device_manager().get_device_matching(lambda device: device.type == "lol", timeout=0.1)

        self.assertRaisesRegex(telco.InvalidArgumentError, "device not found", wait_for_nonexistent)

    def test_cancel_wait_for_nonexistent_device(self):
        cancellable = telco.Cancellable()

        def wait_for_nonexistent():
            telco.get_device_manager().get_device_matching(
                lambda device: device.type == "lol", timeout=-1, cancellable=cancellable
            )

        def cancel_after_100ms():
            time.sleep(0.1)
            cancellable.cancel()

        threading.Thread(target=cancel_after_100ms).start()
        self.assertRaisesRegex(telco.OperationCancelledError, "operation was cancelled", wait_for_nonexistent)


if __name__ == "__main__":
    unittest.main()
