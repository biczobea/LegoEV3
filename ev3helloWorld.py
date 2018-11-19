import ev3dev2.fonts as fonts
from ev3dev2.display import Display
Display.draw.text((10,10), 'Hello World!', font=fonts.load('luBS14'))