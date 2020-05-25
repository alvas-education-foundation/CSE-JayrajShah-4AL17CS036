def main():

    # Write code here
    num = str(input())
    if len(num) == 10:
        dub = 0
        for ele in num:
            if num.count(ele) > 1:
                dub += 1
        if dub > 0:
            print("ENTER")
        else:
            print("DO NOT ENTER")
    else:
        return


main()
