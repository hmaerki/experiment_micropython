# https://github.com/hmaerki/micropython/tree/master/canbus_example
import uos
print('This is a %s version %s. %s' % (uos.uname().sysname, uos.uname().version, uos.uname().machine))

import pyb

# Get clock frequency:
# https://docs.micropython.org/en/latest/pyboard/library/pyb.html#pyb.freq
freq = pyb.freq()
pclk1 = freq[3]  # [s-1]. For the Pyboard v3: 48'000'000 (48MHz)

# Don't know if these values are correct for all baudrates.
# However, there sum must be 20!
BS1 = 14
BS2 = 6

for prescaler in range(4, 500):
  tq = float(prescaler)/pclk1 # [s]
  nominal_bittime = tq * (1 + BS1 + BS2)
  baud = 1.0/nominal_bittime
  if abs(((baud+500.0) % 1000.0) - 500.0) < 1.0:
    # Print only the baudrates with a even value.
    # (There may be a better way to write the test above...)
    print('%0.2f kBaud: can = CAN(1, CAN.NORMAL, prescaler=%d, bs1=%d, bs2=%d)' % (baud/1000.0, prescaler, BS1, BS2))
