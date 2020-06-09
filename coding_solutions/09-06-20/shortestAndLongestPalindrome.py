def isPalindrome(string):
    return string == string[::-1]


inp = input()
words = list(inp.split())
minWord, maxWord = "", ""
maxlen, minlen = 0, len(inp)

for word in words:
    if isPalindrome(word):
        if len(word) > maxlen:
            maxlen = len(word)
            maxWord = word
        if len(word) < minlen:
            minlen = len(word)
            minWord = word

print(maxWord, minWord)
