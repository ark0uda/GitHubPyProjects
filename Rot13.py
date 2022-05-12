"""ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the
alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special
characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet
should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating."""

def rot13(m):
    lst1 = [ord(str(m[i])) for i in range(len(m))]
    lst2 = list(map(lambda x: x if x < 65 else x + 13 if x < 78 else x - 13 if x < 91 else x + 13 if x < 110 else x - 13 if x < 123 else x, lst1))
    return ''.join([chr(lst2[x]) for x in range(len(lst2))])




