def CheckPalindrome(word):
    reverse = word[::-1]
    if word == reverse:
        print("'{}' is a palindrome".format(word))
    else:
        print("'{}' is not a palindrome".format(word))

try:
    print("Enter a word to check if it's a palindrome")
    word = str(input()).lower()

    CheckPalindrome(word)
except:
    print("There was an error")
