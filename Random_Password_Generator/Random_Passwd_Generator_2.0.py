import random
import time


ALPHABETS_LOWER = "abcdefghijklmnopqrstuvwxyz"
ALPHABETS_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS         =  "1234567890"
SPECIAL_CHARECTERS = "!@#$%^&*()_-=+{}[]|\/`~<>,.?';:"

ALL = ALPHABETS_LOWER + ALPHABETS_UPPER + NUMBERS + SPECIAL_CHARECTERS
LENGTH = 12

Passwd = "".join(random.sample(ALL, LENGTH))
print(f"Your new password is:  {Passwd}")
time.sleep(5)