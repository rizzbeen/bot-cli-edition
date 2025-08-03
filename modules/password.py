import time
import sys
from modules.function import slowtype, red, green, yellow, blue, magenta, cyan, white, black
   
def password_run():
    text = "PASSWORD MANAGER --CLI EDITION"
    green_text = green("PASSWORD MANAGER --CLI EDITION")
    width = 50
    spaces = (width-len(text)) //2
    print(f"{' '* spaces}{green_text}")
    print("═"*50)
    vault = {}
    print(blue('\n\nOptions: '),"\n1️⃣ .  ADD ACCOUNT\n2️⃣ .  DELETE ACCOUNT\n3️⃣ .  VIEW ALL ACCOUNT\n4️⃣ .  CHANGE ACCOUNT PASSWORD\n5️⃣ .  EXIT")
    while True: #USER INTERACTION
        try:
            choice = input("\n➡️  ENTER YOUR CHOICE:\t").strip()
            if choice in ["EXIT"]:
                sys.exit()
            if choice.isalpha() or choice not in ['1', "2", "3", "4", "5"]:
                print("\n🚫 INVALID INPUT. PLEASE ENTER BETWEEN 1-5\n")
                continue
        except Exception:
            print("\n⚠️  Something went wrong, Please try again later\n")  
        if choice == "1":
            try:
                category = input("\n📂  ENTER A NAME OF THE CATEGORY:\t")
                if category not in vault:
                    vault[category] = {}
                name = input("\n👤  ENTER YOUR ACCOUNT NAME:\t")
                password = input("\n🔑  ENTER YOUR PASSWORD:\t")
                re_password = input("\n🔁  RE-ENTER YOUR PASSWORD AGAIN:\t")
                if re_password == password:
                    vault[category][name] = {"password": password}
                    print(f'\n✅  ACCOUNT SAVED UNDER {category}\n')
                else:
                    print("\n❌  PASSWORD DIDN'T MATCH. TRY AGAIN\n")
            except Exception:
                print("\n🚫 SOMETHING WENT WRONG. PLEASE TRY AGAIN LATER\n")    
        elif choice == "2":
            try:
                category = input("\n📂  ENTER A NAME OF THE CATEGORY:\t")
                if not vault:
                    print("\n⚠️  PLEASE ADD AN ACCOUNT FIRST\n")
                    continue       
                if category not in vault:
                    print('\n❌  CATEGORY NOT FOUND\n')
                    continue
                if category in vault:
                    name = input("\n👤  ENTER YOUR ACCOUNT NAME:\t")
                    if name not in vault[category]:
                        print("\n❌  ACCOUNT NOT FOUND\n")
                    elif name in vault[category]:
                        delete_password = input("\n🔑  ENTER YOUR PASSWORD:\n")
                        if delete_password != vault[category][name]["password"]:
                            print("\n❌  PASSWORD DIDN'T MATCH\n")
                            continue
                        if delete_password == vault[category][name]["password"]:
                            del vault[category][name]
                            print("\n✅  ACCOUNT DELETION SUCCESSFUL\n")
                            if not vault[category]:
                                delete = vault.pop(category)
            except Exception:
                print("\n🚫 SOMETHING WENT WRONG. PLEASE TRY AGAIN LATER\n")
        elif choice == '3':
            if not vault:
                print("\n⚠️  NO ACCOUNT INFO VISIBLE\n")
                continue
            print("\n📋  ALL ACCOUNTS:\n")
            for category_info, account_info in vault.items():
                print(f"📂  {category_info}:")
                for name, passwo in account_info.items():
                    print(f'  --👤 Name: {name}\n  --🔑 Password: {passwo["password"]}\n')
        elif choice == "4":
            try:
                if not vault:
                    print("\n⚠️  NO ACCOUNT VISIBLE\n")
                    continue
                category = input("\n📂  ENTER A NAME OF THE CATEGORY:\t")
                if category not in vault:
                    print("\n❌  CATEGORY NOT FOUND\n")
                    continue            
                if category in vault:
                    name = input("\n👤  ENTER YOUR ACCOUNT NAME:\t")
                    if name not in vault[category]:
                        print("\n❌  ACCOUNT NOT FOUND\n")
                        continue
                    password = input("\n🔑  ENTER YOUR PASSWORD:\t")
                    if password == vault[category][name]["password"]:
                        new_pass = input("\n🆕  ENTER YOUR NEW PASSWORD:\t")
                        vault[category][name]["password"] = new_pass
                        print("\n✅  PASSWORD HAS BEEN CHANGED SUCCESSFULLY\n")
                    else:
                        print("\n❌  PASSWORD DIDN'T MATCH\n")   
            except Exception:
                print("\n⚠️  SOMETHING WENT WRONG. PLEASE TRY AGAIN LATER\n")     
        elif choice == "5":
            slowtype("\n✨ THANKS FOR USING THIS SIMULATOR\n", 0.03)
            sys.exit()     