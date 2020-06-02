def explode(string, n):

    if n == 1:
        return string
    explode((string+string), n-1)


string = str(input("Enter a String"))
n = int(input("Enter N"))
print(explode(string, n))
