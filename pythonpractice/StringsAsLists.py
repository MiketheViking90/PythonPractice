def isPalindrome(str):
    N = len(str)
    if (N%2 != 0):
        return isPalindromeRecur(str, int(N/2), int(N/2))
    else:
        return isPalindromeRecur(str, int((N/2))-1, int(N/2))

def isPalindromeRecur(str, i, j):
    while (i >= 0 and j < len(str)):
        if (str[i] != str[j]):
            return False
        else:
            i = i-1
            j = j+1
    return True;

b = isPalindrome("racecar")
print(str(b) + " T")
b = isPalindrome("abcde")
print(str(b) + " F")
