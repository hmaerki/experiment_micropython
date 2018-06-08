# https://github.com/hmaerki/micropython/tree/master/canbus_example

from pyb import CAN
from pyb import LED
import micropython

ledBlue = LED(1)

IDs = (122, 123, 124, 125)

# 50kBaud
can = CAN(1, CAN.NORMAL, extframe=False, prescaler=40, sjw=1, bs1=14, bs2=6)
can.setfilter(0, CAN.LIST16, 0, IDs)

def my_handler_mainloop(reason):
  (id, isRTR, filterMatchIndex, telegram) = can.recv(0)
  print("received:", telegram)
  if telegram == b'on':
    ledBlue.on()
  else:
    ledBlue.off()

def my_canbus_interrupt(bus, reason):
  # Don't handle code in the interrupt service routine.
  # Schedule a task to be handled soon
  if reason == 0:
    # print('pending')
    micropython.schedule(my_handler_mainloop, reason)
    return
  if reason == 1:
    print('full')
    return
  if reason == 2:
    print('overflow')
    return
  print('unknown')

can.rxcallback(0, my_canbus_interrupt)

print("Now listening on these CAN-id's: ", IDs)
