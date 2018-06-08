from pyb import CAN
from pyb import LED
import micropython

ledBlue = ('blue', LED(1))
ledGreen = ('green', LED(3))

def switchLed(ledBlueGreen, value):
  name, led = ledBlueGreen
  if value != 0:
    print('Led %s ON' % name)
    led.on()
    return
  print('Led %s OFF' % name)
  led.off()

IDs = (122, 123, 124, 125)

# 50kBaud
can = CAN(1, CAN.NORMAL, extframe=False, prescaler=40, sjw=1, bs1=14, bs2=6)
can.setfilter(0, CAN.LIST16, 0, IDs)

def my_handler_mainloop(reason):
  # The id of the message.
  # A boolean that indicates if the message is an RTR message.
  # The FMI (Filter Match Index) value.
  # An array containing the data.
  (id, isRTR, filterMatchIndex, arrayData) = can.recv(0)
  print("received:", arrayData)
  switchLed(ledBlue, arrayData[0])
  switchLed(ledGreen, arrayData[1])


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

print("Now listening on these id's: ", IDs)
