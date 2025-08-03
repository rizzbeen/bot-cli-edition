from modules.gemini_ai import gemini
from modules.function import slowtype, red, green, yellow, blue, magenta, cyan, white, black
import time
import sys
import os
from modules.quiz import run_quiz
from modules.password import password_run
from modules.tolist import to_list
os.system('cls' if os.name == 'nt' else 'clear')
u = "\n🗣️   USER:\t"
b = "\n🤖   BOT:\t"
print(green('\nTYPE "BYE" TO CLOSE THE BOT'))
while True:
    try:
      user = input(f"{u}").strip().lower()
      if user in ["cmd"]:
        slowtype(green("\n\nLOADING..."), 0.021)
        time.sleep(1)
        print(f"{'\n\n1️⃣  .  quiz.run\n2️⃣  .  acc.run\n3️⃣  .  todo_list'}\n{'TO EXIT FROM THESE SIMULATORS TYPE EXIT\nTYPE THE COMMAND NAME TO START A SIMULATOR'}")
        continue
      if user in ["quiz.run"]:
         slowtype(f"\nQUIZ PROTOCOL STARTING......" ,0.02)
         time.sleep(2)
         run_quiz()
      elif user in ["acc.run"]:
         slowtype(f"\nPASSWORD MANAGER PROTOCOL STARTING......" ,0.02)
         time.sleep(2)
         password_run()
      elif user in ["todo_list"]:
         slowtype(f'\nTO DO LIST SIMULATOR STARTING......', 0.02)
         time.sleep(2)
         to_list()   
      elif user in ["byee", "bye", "byye"]:
        print(red("\n⚠️  STARTING BOT SHUT DOWN PROTOCOL....."))
        time.sleep(3)
        print(green("\n✅  SHUT DOWN SUCCESSFULL"))
        sys.exit()
      else:
       think = green("\n🧠  THINKING... Please wait... ⏳\n")
       slowtype(think, 0.021)
       slowtype(f"{b}{gemini(user)}", 0.01)
    except Exception:
       print("\n⚠️  COULDN'T CONNECT TO API, PLEASE TRY AGAIN LATER")
