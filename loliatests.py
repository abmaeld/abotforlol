from oshelper import *
from uihelper import *
from routines import *
from iaroutines import *
pyautogui.FAILSAFE = False;

# ''' # Test area:

sleep(10);

for i in range(10):
  x = 1645;
  y = 805;
  x_r = random.randrange(0, 275);
  y_r = random.randrange(0, 275);

  x += x_r;
  y += y_r;

  x = 1645+162;
  y = 805+118;
  
  current_time = random.randrange(0, 10);

  print('x: ' +str(x) + ', y: ' + str(y));
  print('current_time: '+ str(current_time));
  color_map_move_result = color_map_move(x, y, current_time);
  print("color_map_move_result: " + str(color_map_move_result));
  if color_map_move_result >= .5:
    pyautogui.moveTo(x=(x)+random.randrange(-20, 20), y=(y)+random.randrange(-20, 20));
    sleep(1);
    keyboard.press_and_release(['a']);
    print('a');
    sleep_for = random.randrange(0, 1);
    sleep(sleep_for);

# '''
# un/comment below and last line (avoid EOF error)
# 
