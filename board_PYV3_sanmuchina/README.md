# Micropython PyBoard v3 - sanmuchina.com

## Board from Aliexpress
- sanmuchina.com
- SM1432F405V0.2_20170106
- USD 17

![Overview](raw/aliexpress_images/overview.jpg)
![Overview](raw/aliexpress_images/top.jpg)
![Overview](raw/aliexpress_images/bottom.jpg)

## My rating
I like the board for these reasons
- Physically big: Pin names are readable
- All I tests worked as it should.
- Cheap. Cheap delivery.

Cons
- It took me some while to find out what I collected in `Good to know`.
## Good to know
### Buttons
Name | Pyboard | sanmuchina
-|-|-
Reset | `RST` | `K1`
User | `USR` | `K2`

### Pin assignement
See (example_pins/readme.md)

### This firmware should work
Pick `Firmware suitable for hand-made PYBv3 boards` on http://micropython.org/download

# Compile and flash the firmware
# Compile
Clone
https://github.com/micropython
and compile:
```
cd micropython/ports/stm32cubemx
make BOARD=PYBV3
sudo make BOARD=PYBV3 deploy
```

## Flash
Bring the board in dfu-bootloader-mode
- On the Python prompt type: `pyb.bootloader()`
- Or: Connect pins `BOOT0` with pin `3.3V`. Press `Reset` button

Now flash:
```
sudo make BOARD=PYBV3 deploy
```

