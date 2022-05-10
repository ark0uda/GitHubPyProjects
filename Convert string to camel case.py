""" Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first
word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case,
also often referred to as Pascal case).

Examples:
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior" """


def to_camel_case(text):
    lst = text.replace('-', '_').split('_')
    return ''.join(lst[:1] + list(map(str.title, lst[1:])))
