import sys

import telco


def on_process_crashed(crash):
    print("on_process_crashed")
    print("\tcrash:", crash)


def on_detached(reason, crash):
    print("on_detached()")
    print("\treason:", reason)
    print("\tcrash:", crash)


device = telco.get_usb_device()
device.on("process-crashed", on_process_crashed)
session = device.attach("Hello")
session.on("detached", on_detached)
print("[*] Ready")
sys.stdin.read()
