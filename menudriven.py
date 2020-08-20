import os
import pyttsx3

print("\nWelcome to Bot ")
pyttsx3.speak("We are here for you ")
print()
while True:
    select = input("Tell me what you want  : ")
    print()
    if (("dont" in select) or ("not" in select)):
        print("Please tell which App you want to open... \n")
    elif (("run" in select) or ("execute" in select) or ("open" in select)) and (("chrome" in select) or ("browser" in select)):
        os.system("chrome")
    elif (("run" in select) or ("execute" in select) or ("open" in select)) and (("windows media player" in select) or ("media player" in select)):
        os.system("wmplayer")
    elif (("run" in select) or ("execute" in select) or ("open" in select)) and (("explorer" in select) or ("file manager" in select)):
        os.system("explorer")
    elif (("run" in select) or ("execute" in select) or ("open" in select)) and (("calculator" in select) or ("calc" in select)):
        os.system("calc")
    elif (("run" in select) or ("execute" in select) or ("open" in select)) and (("notepad" in select) or ("editor" in select)):
        os.system("notepad")
    elif (("run" in select) or ("execute" in select) or ("open" in select)) and (("command prompt" in select) or ("cmd" in select)):
        os.system("cmd")
    elif (("run" in select) or ("execute" in select) or ("open" in select)) and ("task manager" in select):
        os.system("taskmgr")
    elif (("run" in select) or ("execute" in select) or ("open" in select)) and ("paint" in select):
        os.system("mspaint")
    elif ("close" in select) or ("quit" in select) or ("exit" in select):
        pyttsx3.speak("Thanks for using our service")
        break
    else:
        print("Enter valid choice....!\n")