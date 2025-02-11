1.  # CircuitPython General Purpose I/O
2.  import time
3.  import board
4.  from digitalio
5.  
6.  led = digitalio.DigitalInOut(board.D12)
7.  led.direction = digitalio.Direction.OUTPUT
8.  
9.  switch = digitalio.DigitalInOut(board.D11)
10. switch.direction = digitalio.Direction.INPUT
11. 
12. while True:
13. # We could also do "led.value = not switch.value"!
14.   if switch.value:
15.     time.sleep(1.0)
16.     led.value = False
17.
18.   else:
19.     time.sleep(6.0)
20.     led.value = True
21. 
22.   time.sleep(0.1) # small pause
