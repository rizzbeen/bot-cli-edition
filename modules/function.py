import sys
import time
from colorama import Fore
from colorama import Style
#TYPING EFFECT
def slowtype(text, speed):
    for x in text:
     sys.stdout.write(x)
     sys.stdout.flush()
     time.sleep(speed)
    print()
#COLOR
def red(text): return Fore.RED + text + Style.RESET_ALL
def green(text): return Fore.GREEN + text + Style.RESET_ALL
def yellow(text): return Fore.YELLOW + text + Style.RESET_ALL
def blue(text): return Fore.BLUE + text + Style.RESET_ALL
def magenta(text): return Fore.MAGENTA + text + Style.RESET_ALL
def cyan(text): return Fore.CYAN + text + Style.RESET_ALL
def white(text): return Fore.WHITE + text + Style.RESET_ALL
def black(text): return Fore.BLACK + text + Style.RESET_ALL
