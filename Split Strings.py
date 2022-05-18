"""Complete the solution so that it splits the string into pairs of two characters. If the string contains an
odd number of characters then it should replace the missing second character of the final pair with an
underscore ('_').

Examples:
* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']"""


def solution(s):
    return [s[i]+'_' if len(s[i:]) == 1 else s[i:i+2]
            for i in range(0, len(s), 2)]

