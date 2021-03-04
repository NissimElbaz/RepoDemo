import random
import os




def cls(): return os.system('cls')

cls()

name = input("what is your name?")
print(f"welcome to you, {name}")
print(f"{name.title()}, your name has {len(name)}")

for index, letter in enumerate(name):
    print(f"{index+1}: {letter}")
    if letter == "s":
        print("wow wow")
    else:
        print("🤴🤴🤴")

count = 0
while True:
    number = int(input("type a number: "))
    if number%5 == 0:
        print(f"{number} is multiplle of 5")
        count += 1
    else:
        break
print(f"you typed {count} numbers that multiplle of 5")
