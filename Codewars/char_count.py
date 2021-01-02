"""Description.

Welcome, Warrior! In this kata, you will get a message and 
you will need to get the frequency of each and every character!

Explanation
Your function will be called char_freq/charFreq/CharFreq and 
you will get passed a string, you will then return a dictionary 
(object in JavaScript) with as keys the characters, and as 
values how many times that character is in the string. You can 
assume you will be given valid input.
"""
import collections


def char_freq(message):
    """Count the chareters in a message.
    
    Count returns a dictionary
    ex: Counter({' ': 8, 't': 6, 'e': 4, 'r': 2, 's': 2)
    """
    return collections.Counter(message)

message = input('Enter: ')
print(char_freq(message))
