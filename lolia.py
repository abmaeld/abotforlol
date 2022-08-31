from oshelper import *
from uihelper import *
from routines import *
from iaroutines import *
pyautogui.FAILSAFE = False;

#
''' # Test area:

sleep(5);
while True:
  locked_via_ui = click(path='__assets__/br/cameralock.png', grayscale=False, confidence=.90, button='left', clicks=2, interval=.35, duration=.35);
  if locked_via_ui:
    pyautogui.drag(2, 2, 1, button='left');
    #pyautogui.drag(2, 2, 1, button='right');
    print('locked via ui');
    locked_via_ui = False;

#
'''

# un/comment below and last line (avoid EOF error)
#'''

info();
prcssclear();

if len(sys.argv) > 1 and str(sys.argv[1]) == '-dev':
  user = 'contadovaca';
  senha = 'senhadovaca1';
else:
  user = input('usuário: ');
  senha = input('senha: ');
  sleep(5);

print('launched');
launch();

while not prcssrunning("RiotClientUx"):
  sleep(5);

print('loging in');
login(user, senha);

while not prcssrunning("LeagueClientUxRender"):
  sleep(5);

print('dismiss banner');
click('__assets__/br/ascenda.png');
sleep(3);

games = 0;
playing = True;
play();
print('play, selecting mode, select difficulty');
sleep(3);

while playing:

  print('queued');
  queue();
  print('new match');
  games += 1;
  print('game: ' + str(games));
  loading = time.time();
  sleep(10);
  while pyautogui.pixelMatchesColor(28, 18, (20, 80, 59), tolerance=15):
    if time.time() - loading >= 3*60:
      print('loading timeout');
      break;
    sleep(1);

  matchtime = time.time();
  sleep_for = random.randrange(10, 20);
  sleep(sleep_for);
  # /* in python    
  # tab or shift+tab below and comment above
  # clear();
  counter = 0;
  moving = False;
  movement = time.time();
  movingfor = 0;
  locked_via_ui = True;
  pyautogui.click(button='left', clicks=3);
  sleep(3);
  keyboard.press_and_release(['p']);
  sleep(3);
  pyautogui.moveTo(x=640, y=400);
  pyautogui.drag(5, 5, 1, button='left');
  pyautogui.drag(5, 5, 1, button='right');
  sleep(3);
  keyboard.press_and_release(['p']);
  sleep(3);
  keyboard.press_and_release(['y']);
  sleep(3);
  pyautogui.moveTo(x=1780+random.randrange(-10, 10), y=940+random.randrange(-10, 10));
  keyboard.press_and_release(['a']);
  sleep_for = random.randrange(15, 25);
  sleep(sleep_for);

  while True:
    if not prcssrunning("League of Legends") or prcssrunning("LeagueClientUxRender"):
      print('ended');
      jogarnovamente();
      break;

    locked_via_ui = click(path='__assets__/br/cameralock.png', grayscale=False, confidence=.90, button='left', clicks=2, interval=.35, duration=.35);
    if locked_via_ui:
      pyautogui.drag(2, 2, 1, button='left');
      # pyautogui.drag(2, 2, 1, button='right');
      print('locked via ui');
      locked_via_ui = False;

    timestamp = time.time();
    current_time = round((timestamp - matchtime)/60, 2);
    print(str(counter) + ': ' + str(current_time));
    multiplier = 1;
    turning_points = [4, 6, 10, 16, 18];
    
    if timestamp - matchtime < turning_points[0]*60:
      x = 1780;
      y = 940;
      multiplier = 1;
    elif timestamp - matchtime < turning_points[1]*60:
      x = 1800;
      y = 930;
      multiplier = 1.5;
    elif timestamp - matchtime < turning_points[2]*60:
      x = 1820;
      y = 900;
      multiplier = 2;
    elif timestamp - matchtime < turning_points[3]*60:
      x = 1850;
      y = 880;
      multiplier = 2.5;
    elif timestamp - matchtime <= turning_points[4]*60:
      x = 1885;
      y = 840;
      multiplier = 3;
    else:
      x = 1885;
      y = 840;
      multiplier = 2;

      deltax = 20;
      deltay = 20;
      
      x += random.randrange(-deltax, deltax);
      y += random.randrange(-deltay, deltay);

      if x > 1920:
        x = 1920;
      if y > 1080:
        y = 1080;

    skillorder = ['r', 'q', 'w', 'e'];
    for skill in skillorder:
      if counter%4 == 0:
        if random.randrange(100) < .15 * 100:
          keyboard.press(['ctrl']);
          keyboard.press_and_release([skillorder[3]]);
          keyboard.release(['ctrl']);
      keyboard.press(['ctrl']);
      keyboard.press_and_release([skill]);
      keyboard.release(['ctrl']);

    hplow = pyautogui.pixelMatchesColor(800, 1040, (1, 13, 7), tolerance=10);
    mplow = pyautogui.pixelMatchesColor(800, 1060, (1, 13, 7), tolerance=10);

    if hplow or mplow:
      if not pyautogui.pixelMatchesColor(700, 1040, (1, 13, 7), tolerance=10):
        print('recall');
        pyautogui.moveTo(x=1700, y=1050);
        keyboard.press_and_release(['g']);
        sleep(10);
        keyboard.press_and_release(['b']);
        print('b');
        sleep(10);
        keyboard.press_and_release(['p']);
        pyautogui.moveTo(x=470, y=390);
        pyautogui.drag(5, 5, 1, button='left');
        pyautogui.drag(5, 5, 1, button='right');
        sleep(1);
        pyautogui.moveTo(x=670, y=390);
        pyautogui.drag(5, 5, 1, button='left');
        pyautogui.drag(5, 5, 1, button='right');
        sleep(1);
        pyautogui.moveTo(x=870, y=390);
        pyautogui.drag(5, 5, 1, button='left');
        pyautogui.drag(5, 5, 1, button='right');
        sleep(1);
        keyboard.press_and_release(['p']);
        pyautogui.moveTo(x=x+random.randrange(-10, 10), y=y+random.randrange(-10, 10));
        keyboard.press_and_release(['a']);
        sleep(20*multiplier);

    if pyautogui.pixelMatchesColor(700, 1040, (1, 13, 7), tolerance=10):
      dead = time.time();
      print('dead');
      while pyautogui.pixelMatchesColor(700, 1040, (1, 13, 7), tolerance=10):
        if time.time() - dead >= 3*60:
          break;
        sleep(1);
      sleep(3);
      print('alive');
      keyboard.press_and_release(['p']);
      sleep(1);
      pyautogui.moveTo(x=470, y=390);
      pyautogui.drag(5, 5, 1, button='left');
      pyautogui.drag(5, 5, 1, button='right');
      sleep(1);
      pyautogui.moveTo(x=670, y=390);
      pyautogui.drag(5, 5, 1, button='left');
      pyautogui.drag(5, 5, 1, button='right');
      sleep(1);
      pyautogui.moveTo(x=870, y=390);
      pyautogui.drag(5, 5, 1, button='left');
      pyautogui.drag(5, 5, 1, button='right');
      sleep(1);
      keyboard.press_and_release(['p']);
      sleep(2);
      pyautogui.moveTo(x=x+random.randrange(-10, 10), y=y+random.randrange(-10, 10));
      keyboard.press_and_release(['a']);
      sleep(1);
      if random.randrange(100) < .2 * 100:
        pyautogui.press('enter');
        pyautogui.write('honra aí fml.', interval=0.1);
        pyautogui.press('enter');
      sleep(int(20*multiplier));

    if pyautogui.pixelMatchesColor(1030, 1040, (1, 13, 7), tolerance=10):
      pyautogui.moveTo(x=555+random.randrange(-10, 10), y=555+random.randrange(-10, 10));
      keyboard.press_and_release(['g']);
      keyboard.press_and_release(['e']);
      keyboard.press_and_release(['w']);
      print('g e w');

    if pyautogui.pixelMatchesColor(940, 1040, (1, 13, 7), tolerance=10):
      if counter % 2 == 0: 
        keyboard.press_and_release(['d']);
        print('d');
      else:
        keyboard.press_and_release(['f']);
        print('f');
        
    if time.time() - movement >= movingfor:
      moving = False;
      movingfor = 0;

    if not moving and not pyautogui.pixelMatchesColor(700, 1040, (1, 13, 7), tolerance=10):
      movement = time.time();
      max_travel_range = 7;
      min_travel_range = 3;
      if counter % 2 == 0:
        color_map_move_result = color_map_move(x, y, current_time);
        print("color_map_move_result: " + str(color_map_move_result));
        if color_map_move_result >= .5:
          pyautogui.moveTo(x=x, y=y);
          sleep(1);
          keyboard.press_and_release(['a']);
          print('a');
          # sleep_for = random.randrange(int(min_travel_range+(min_travel_range*multiplier)), int(min_travel_range+(max_travel_range*multiplier)));
          sleep_for = random.randrange(int((min_travel_range*multiplier)/2), int(min_travel_range*multiplier));
          sleep(sleep_for);
        else:
          x = x+random.randrange(-33, 33);
          y = y+random.randrange(-33, 33);
          if x > 1920:
            x = 1920;
          if y > 1080:
            y = 1080;
          pyautogui.moveTo(x=x, y=y);
          sleep(2);
          keyboard.press_and_release(['a']);
          print('a');
          # sleep_for = random.randrange(int(min_travel_range+(min_travel_range*multiplier)), int(min_travel_range+(max_travel_range*multiplier)));
          sleep_for = random.randrange(0, int(min_travel_range+(min_travel_range*multiplier)));
          sleep(sleep_for);  
      else:
        if pyautogui.pixelMatchesColor(1000, 1040, (1, 13, 7), tolerance=10):
          sleep(1);
          pyautogui.moveTo(x=555+random.randrange(-100, 100), y=555+random.randrange(-100, 100));
          sleep(1);
          keyboard.press_and_release(['g']);
          print('g');
          sleep_for = random.randrange(0, min_travel_range);
          sleep(sleep_for);
        elif random.randrange(100) < .5 * 100:
          color_map_move_result = color_map_move(x, y, current_time);
          print("color_map_move_result: " + str(color_map_move_result));
          if color_map_move_result >= .5:
            sleep(1);
            pyautogui.moveTo(x=x, y=y);
            sleep(1);
            keyboard.press_and_release(['a']);
            print('a');
            sleep_for = random.randrange(int(min_travel_range+(min_travel_range*multiplier)), int(min_travel_range+(max_travel_range*multiplier)));
            sleep(sleep_for);
          else:
            sleep(1);
            x = x+random.randrange(-33, 33);
            y = y+random.randrange(-33, 33);
            if x > 1920:
              x = 1920;
            if y > 1080:
              y = 1080;
            pyautogui.moveTo(x=x, y=y);
            sleep(2);
            keyboard.press_and_release(['a']);
            print('a');
            # sleep_for = random.randrange(int(min_travel_range+(min_travel_range*multiplier)), int(min_travel_range+(max_travel_range*multiplier)));
            sleep_for = random.randrange(min_travel_range, int(min_travel_range+(min_travel_range*multiplier)));
            sleep(sleep_for);  
        elif random.randrange(100) < .66 * 100:
          sleep(1);
          pyautogui.moveTo(x=1030+random.randrange(-100, 100), y=420+random.randrange(-100, 100));
          sleep(1);
          keyboard.press_and_release(['a']);
          print('a');
          sleep_for = random.randrange(0, min_travel_range);
          sleep(sleep_for);
        else:
          sleep(1);
          pyautogui.moveTo(x=555+random.randrange(-100, 100), y=555+random.randrange(-100, 100));
          sleep(1);
          keyboard.press_and_release(['g']);
          print('g');
          sleep_for = random.randrange(0, min_travel_range);
          sleep(sleep_for);
      

    if random.randrange(100) < .44 * 100:
      keyboard.press_and_release(['1', '2', '3', '4']);
      print('1..4');
    elif random.randrange(100) < .37 * 100:
      keyboard.press_and_release(['4', '5', '6', '7']);
      print('4..7');

    if counter % 2 == 0 or (counter % 2 != 0 and random.randrange(100) < .091 * 100):  
      ofskills = [['q', .73], ['e', .25], ['r', .15]];
      for skill in ofskills:
        if random.randrange(100) < skill[1] * 100:
          sleep(1);
          pyautogui.moveTo(x=1030+random.randrange(-50, 50), y=420+random.randrange(-50, 50));
          sleep(1);
          keyboard.press_and_release(['a']);
          sleep(1);
          keyboard.press_and_release([skill[0]]);
          print(skill[0]);
          sleep(1);
          
    if counter % 2 != 0 or (counter % 2 == 0 and random.randrange(100) < .1122 * 100): 
      dfskills = [['w', .6], ['e', .55]];
      for skill in dfskills:
        if random.randrange(100) < skill[1] * 100:
          sleep(1);
          pyautogui.moveTo(x=555+random.randrange(-50, 50), y=555+random.randrange(-50, 50));
          sleep(1);
          keyboard.press_and_release(['g']);
          sleep(1);
          keyboard.press_and_release([skill[0]]);
          print(skill[0]);
          sleep(1);
    
    sleep(random.randrange(0,2));
    counter += 1;

#'''
#
