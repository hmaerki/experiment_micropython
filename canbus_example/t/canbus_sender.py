from pyb import CAN
from pyb import LED
import pyb
import micropython

DESTINATION_CAN_ID = 123

ledBlue = LED(1)

# 50kBaud
can = CAN(1, CAN.NORMAL, extframe=False, prescaler=40, sjw=1, bs1=14, bs2=6)


def my_handler_mainloop(switchValue):
  if switchValue:
    ledBlue.on()
    telegram = b'\5\22\33'
  else:
    ledBlue.off()
    telegram = 'b\0\42\45\22'

  can.send(telegram, DESTINATION_CAN_ID)

def my_switch_callback():
  # Don't handle code in the interrupt service routine.
  # Schedule a task to be handled soon
  micropython.schedule(my_handler_mainloop, switch.value())

switch = pyb.Switch()
switch.callback(my_switch_callback)

print("Press Switch to send CAN-telegrams!")
