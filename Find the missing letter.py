"""Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter
in the array.

You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will
always be at least 2.

The array will always contain letters in only one case.

Example:
['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
["a","b","c","d","f"] -> "e"
["O","Q","R","S"] -> "P"

Use the English alphabet with 26 letters!"""


def find_missing_letter(chars):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    index = alphabet.find(''.join(chars[0]))
    for i in range(len(''.join(chars))):
        if chars[i] != alphabet[index + i]:
            return alphabet[index + i]
