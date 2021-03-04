import random
import os




def cls(): return os.system('cls')

cls()

name = input("what is your name?")
print(f"welcome to you, {name}")
print(f"{name.title()}, your name has {len(name)}")