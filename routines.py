from oshelper import *
from uihelper import *

def login(username, password):
  inputini = r"\lolconfig\input.ini";
  inputini_tgt = r"C:\Riot Games\League of Legends\Config\input.ini";
  overwritefile(inputini, inputini_tgt);
  gamecfg = r"\lolconfig\game.cfg";
  gamecfg_tgt = r"C:\Riot Games\League of Legends\Config\game.cfg";
  overwritefile(gamecfg, gamecfg_tgt);
  print('updated cfg and inputcfg');
  sleep(10);
  pyautogui.write(username, interval=0.1);
  sleep(1);
  pyautogui.press('tab');
  pyautogui.write(password, interval=0.1);
  sleep(1);
  pyautogui.press('enter');  
  sleep(5);  

def launch():
  execute("C:\Riot Games\Riot Client\RiotClientServices.exe --launch-product=league_of_legends --launch-patchline=live");

def prcssclear():
  riotsprcss = ["RiotClientUx", "RiotClientUxRender", "LeagueClient", str("League"+"%20"+"of"+"%20"+"Legends")];
  for process in riotsprcss:
    prcsskill(process);

def play():
  sleep(40);
  click('__assets__/br/jogar.png');
  sleep(5);
  click('__assets__/br/coopvsia.png');
  sleep(5);
  click('__assets__/br/iniciante.png');
  sleep(5);
  click('__assets__/br/confirmar.png');
  sleep(5);
  return True;
  
def queue():
  sleep(5);
  click('__assets__/br/encontrarpartida.png');
  onqueue = True;
  while onqueue:
    if click('__assets__/br/aceitar.png'):
      sleep(5);
      click('__assets__/br/chatlobby.png');
      pyautogui.write('sup mid', interval=0.1);
      pyautogui.press('enter');
      if random.randrange(100) < .55 * 100:
        pyautogui.write('vem um adc ou mid cmg', interval=0.1);
        pyautogui.press('enter');
      if random.randrange(100) < .125 * 100:
        pyautogui.write('eu honro.', interval=0.1);
        pyautogui.press('enter');
      click('__assets__/br/sup.png');
      sleep(3);
      click('__assets__/br/sona.png');
      sleep(3);
      click('__assets__/br/confirmarcampeao.png');
    else:
      if prcssrunning('League of Legends'):
        onqueue = False;
        return True;
      sleep(1);
  
def jogarnovamente():
  sleep(10);
  click('__assets__/br/proxima.png');
  sleep(5);
  click('__assets__/br/ok.png');
  sleep(3);
  click('__assets__/br/ok.png');
  sleep(5);
  click('__assets__/br/ok.png');
  sleep(5);
  click('__assets__/br/jogarnovamente.png');
  sleep(5);
  click('__assets__/br/jogarnovamente.png');


