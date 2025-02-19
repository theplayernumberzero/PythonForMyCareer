def isPalindrome(word):
    isPalindrome = True
    for i in range(0, len(word)):
        if word[i] != word[len(word)-i-1]:
            isPalindrome = False
    return isPalindrome

word = "araba"
print(f"{word} is palindrome: {isPalindrome(word=word)}") 