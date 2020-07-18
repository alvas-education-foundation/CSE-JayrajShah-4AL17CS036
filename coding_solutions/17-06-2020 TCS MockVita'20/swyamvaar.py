N = int(input())


# Checking Constraints
if 1 <= N <= (10**4):
    groom = input()
    bride = input()
    if len(groom) == len(bride):
        gRum = groom.count('r')
        gMojito = groom.count('m')

        # Check if bride matches with groom
        match = 0
        for b in bride:
            if(b == 'r'):
                if(gRum > 0):
                    gRum -= 1
                    match += 1
                else:
                    break
            else:
                if(gMojito > 0):
                    gMojito -= 1
                    match += 1
                else:
                    break
        # printing Nos of non-matches
        print(N-match, end="")
    else:
        print(1, end="")

else:
    print(1, end="")
