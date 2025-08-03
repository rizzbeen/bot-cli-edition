from modules.function import slowtype, red, green, yellow, blue, magenta, cyan, white, black
import time
import sys

def to_list():#INTERFACE
    text = "TO DO LIST --CLI EDITION"
    gr_text = green("TO DO LIST --CLI EDITION")
    width = 45
    spaces = (width - len(text)) // 2
    print(f"\n{' ' * spaces}{gr_text}")
    print("=" * 45)
    # OPTIONS
    print(f"\n{blue('📋 OPTIONS:')}\n 1️⃣  . ADD TASK\n 2️⃣  . DELETE TASK\n 3️⃣  . VIEW TASK\n 4️⃣  . MARK AS DONE\n 5️⃣  . TERMINATE SIMULATOR")
    list_vault = []
    while True:
        choice = input("\n➡️  ENTER YOUR CHOICE:\t").strip()
        if choice.upper() == "EXIT":
            print("\n👋 Exiting the TO DO LIST. Goodbye!\n")
            sys.exit()
        if choice.isalpha() or choice not in ["1", "2", "3", "4", "5"]:
            print("\n⚠️  PLEASE ENTER A NUMBER BETWEEN 1-5\n")
            continue
        if choice == "1":
            add_task = input("\n📝 ENTER THE TASK NAME:\t")
            list_vault.append({"task": add_task, "DONE": False})
            print(f'\n✅ YOUR TASK "{add_task}" HAS BEEN ADDED SUCCESSFULLY!\n')
        elif choice == "2":
            if not list_vault:
                print("\n🚫 NO TASK FOUND\n")
                continue
            print('\n🗑️  TASKS:')
            for index, task in enumerate(list_vault, start=1):
                print(f'{"✅" if task["DONE"] else "❌"} {index}. {task["task"]}')
            try:
                delete = int(input("\n❓ ENTER THE TASK NUMBER TO DELETE:\t").strip())
                try:
                    task = list_vault[delete - 1]
                except IndexError:
                    print("\n⚠️  TASK NOT FOUND\n")
                    continue
                list_vault.pop(delete - 1)
                print("\n🗑️  TASK DELETED SUCCESSFULLY!\n")
            except Exception:
                print("\n⚠️  SOMETHING WENT WRONG, PLEASE TRY AGAIN LATER\n")
        elif choice == "4":
            try:
                if not list_vault:
                    print("\n🚫 NO TASK FOUND\n")
                    continue
                print("\nTASKS:")
                for i, t in enumerate(list_vault, start=1):
                    print(f'{"✅" if t["DONE"] else "❌"} {i}. {t["task"]}')
                mark = int(input("\n⭐ ENTER THE TASK NUMBER TO MARK AS DONE:\t").strip())
                try:
                    task = list_vault[mark - 1]
                except IndexError:
                    print("\n⚠️  TASK NOT FOUND\n")
                    continue
                if task["DONE"]:
                    print('\nℹ️  TASK ALREADY MARKED AS DONE\n')
                    continue
                else:
                    task["DONE"] = True
                    print(f'\n🎉 TASK | {task["task"]} | MARKED AS DONE!\n')
            except Exception:
                print('\n⚠️  SOMETHING WENT WRONG, PLEASE TRY AGAIN LATER\n')
        elif choice == "3":
            print("\n" + "═" * 35)
            text = "TASK LIST"
            blue_text = blue("📋 TASK LIST")
            width = 30
            spaces = (width - len(text)) // 2
            print(f'{" " * spaces}{blue_text}')
            print("═" * 35)
            if not list_vault:
                print("\n🚫 NO TASKS TO SHOW\n")
            else:
                for index, task in enumerate(list_vault, start=1):
                    marked = "✅" if task['DONE'] else "❌"
                    print(f'{marked} {index}. {task["task"]}')
            print("═" * 35 + "\n")
        elif choice == "5":
            print("\n THANKS FOR USING OUR SERVICE! 👋\n")
            sys.exit()

           
          








      