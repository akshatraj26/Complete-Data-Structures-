def IsPalindrome(string):
    if len(string) == 0:
        return True

    if string[0] != string[len(string) - 1]:
        return False
    return IsPalindrome(string[-1:1])

print(IsPalindrome("teneta"))

string = "teneta"

j = len(string) - 1
for i in range(len(string)):
    if i > j and string[i] == string[j]:
        print("palindrome")
        j = j -1
    else:
        print("Not a palindrome")
j = len(string) - 1
i = 0

while i < j:
    if string[i] == string[j]:
        i += 1
        j -= 1
        print("Palindrome")
    else:
        "Not a palindrome"

