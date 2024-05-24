import time
import random
import decimal
import os

""" This program types a message to the terminal, using time.sleep to help mimick real human typing"""

message = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way"
punctation = ['?','!','.']

while(True):
    os.system('clear')
    for char in message:
        print(char, end='',flush=True)

        if (char in punctation):
            time.sleep(1)
        
        time.sleep(random.uniform(0, .2))