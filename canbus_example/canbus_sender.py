# https://github.com/hmaerki/micropython/tree/master/canbus_example

from pyb import CAN
from pyb import LED
import pyb
import micropython

DESTINATION_CAN_ID = 123

ledBlue = LED(1)

switch = pyb.Switch()

# 50kBaud
can = CAN(1, CAN.NORMAL, extframe=False, prescaler=40, sjw=1, bs1=14, bs2=6)


print("Press Switch to send CAN-telegrams, press <ctrl-c> to abort.")

lastValue = None

while True:
  newValue = switch.value()
  if lastValue != newValue:
    lastValue = newValue
    if newValue:
      ledBlue.on()
      telegram = b'on'
    else:
      ledBlue.off()
      telegram = b'off'

    print("Sending %s to CAN-id %d" % (telegram, DESTINATION_CAN_ID))
    can.send(telegram, DESTINATION_CAN_ID)
