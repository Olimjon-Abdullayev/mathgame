import random
import time
import os
from termcolor import colored
text = "\n         ##########################################################\n\
         #######################   MATH GAME   ####################\n\
         ##########################################################\n"
text1 = "          Enter [1] if it is True, [0] if it is False\n"
def rule():
    print(colored(text, 'blue'))
    print(colored(text1, 'green'))  
def game():
    record = 0
    objs = ['+', '-', '*']
    while True:
        rule()
        a = random.randint(0,10)
        b = random.randint(0,10)
        d = a + b
        e = a-b
        f = a*b
        h = random.choice(objs)
        
        if h == '+':
            c = random.randint(d-1,d+1)
        elif h == '-':
            c = random.randint(e-1,e+1)
        else:
            c = random.randint(f-1,f+1)
        choice = input(colored(f"\n          Is {a} {h} {b} = {c} ?     >>>  ", 'red'))
        if choice == '0' or choice == '1':
            if (d == c or e ==c or f == c) and choice == "1":
                record+=1
                os.system('cls')
                print(colored("         [TRUE]", 'green'))
                time.sleep(1.5)
                os.system('cls')
            elif (d == c or e ==c or f == c) and choice == "0":
                os.system('cls')
                print(colored("         [FALSE]" , 'red'))
                time.sleep(1.5)
                os.system('cls')
                break
            elif (d != c or e !=c or f != c) and choice == "1":
                os.system('cls')
                print(colored("         [FALSE]" , 'red'))
                time.sleep(1.5)
                os.system('cls')
                break
            elif(d != c or e !=c or f != c) and choice == "0":
                record+=1
                os.system('cls')
                print(colored("         [TRUE]", 'green'))
                time.sleep(1.5)
                os.system('cls')
        else:
            os.system('cls')
            print(colored("\n       You should only type [1]  or [0]   !", 'red'))
            time.sleep(1.5)
            os.system('cls')
    print(colored(f"\n        CONGRATULATIONS, You reached level [{record}] \n\n\n", 'green'))
    time.sleep(1.5)
    os.system('cls')
game()
print(colored("\n           Do you want to replay\n ", 'blue'))
print(colored("           [1]YES\n", 'green'))
choi = input(colored("           [0]NO           ", 'red'))
os.system('cls')
if choi == '1' or choi == '0':
    if choi == '1':
        game()
    elif choi == '0':
        print(colored("              THANKS FOR TESTING ", 'green'))
else:
    print(colored("          Enter only [1] or [0]", 'green'))
