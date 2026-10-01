# CircuitPython General Purpose I/O
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.D12)
led.direction = digitalio.Direction.OUTPUT

switch = digitalio.DigitalInOut(board.D11)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

while True:
    # We could also do "led.value = not switch.value"!
    if switch.value:
        time.sleep(1.0)
        led.value = False
    else:
        time.sleep(6.0)
        led.value = True

    time.sleep(0.1)  # small pause
