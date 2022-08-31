import psutil
import win32api
import os
import time
from time import sleep
import random
import sys
import subprocess

def execute(command): #open a program
  win32api.WinExec(command);

def ps_shell(command):
  cmd_command = r"powershell.exe " + command;
  os.system(cmd_command);
    
def clear():
  os.system('cls');

def info():
  cdir = str(os.getcwd()); 
  print("Working at '" + cdir + "'.");
  print("PID: '" + str(os.getpid()) + "'.");

def prcssrunning(name):
  for proc in psutil.process_iter():
    try:
      if name.lower() in proc.name().lower():
        return True
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
      pass
  return False;

def prcsskill(name):
  if prcssrunning(name):
    command = "taskkill /IM " + name + ".exe /T /F";
    try:
      os.system(command);
    except:
      pass

def overwritefile(file, target):
  # copy 'D:\Desktop\Unorganized\LOLIA\lolconfig\input.ini' 'C:\Riot Games\League of Legends\Config\input.ini'
  file = str(os.getcwd()) + file;
  #print('file: '+ file);
  #print('target: '+ target);
  command = "copy '" + file + "' '" + target + "'";
  #print('command: '+ command);
  try:
    ps_shell(command);
  except:
    pass
  
#
'''
#
info();
sleep(5);
file = r"\lolconfig\input.ini"
target = r"C:\Riot Games\League of Legends\Config\input.ini"
overwritefile(file, target);
#
'''
#
