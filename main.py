# This is a sample Python script.
import json
import math
import os
import sys
from datetime import datetime
from random import randint


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(f"Witaj, {sys.argv[1]}!")
    else:
        print_hi(input("Podaj swoje imię: "))
    print(os.listdir())
    print(sys.argv)
    print(math.pi)
    print(datetime.now)
    print(randint(1, 10))
    print(json.loads('{"key": "value"}'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
