string = 'tenet'
string = "amanaplanacanalpanama"


def palindrome(string):
    i = 0
    j = len(string) - 1

    while i < j:
        if string[i] == string[j]:
            i += 1
            j -= 1
            return True
        else:
            return False

def isPalindrome(string):
    if len(string) == 0:
        return True

    if string[0] != string[len(string)-1]:
        return False
    return isPalindrome(string[1:-1])

print(isPalindrome(string))