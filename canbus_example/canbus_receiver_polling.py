# https://github.com/hmaerki/micropython/tree/master/canbus_example

from pyb import CAN
from pyb import LED
import micropython

ledBlue = LED(1)

IDs = (122, 123, 124, 125)

# 50kBaud
can = CAN(1, CAN.NORMAL, extframe=False, prescaler=40, sjw=1, bs1=14, bs2=6)
can.setfilter(0, CAN.LIST16, 0, IDs)
can.restart()

print("Now listening on these CAN-id's: ", IDs)

while True:
  (id, isRTR, filterMatchIndex, telegram) = can.recv(0, timeout=100000)
  print("received:", telegram)
  if telegram == b'on':
    ledBlue.on()
  else:
    ledBlue.off()

