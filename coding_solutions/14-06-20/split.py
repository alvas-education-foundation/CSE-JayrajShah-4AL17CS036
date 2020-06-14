import re
sentence = str(input("Enter a String : "))
delimiter = tuple(i for i in str(input("Enter Split String : ")))
regexPattern = '|'.join(map(re.escape, delimiter))
output = re.split(regexPattern, sentence)
os = ""
for i in output:
    os += i

print(os)
