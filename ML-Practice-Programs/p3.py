'''
3. Write a Python program to test whether a passed letter is a vowel or not
'''


def is_vowel(ch):
    All_vowels = 'aeiou'
    return ch in All_vowels


char = input("Enter a Character : ")
print(is_vowel(char))
