def main():
    counter = {}
    N = int(input())
    if N >= 1 and N <= 50:
        a = list(map(int, input().split()))
        for i in a:
            if i >= 1 and i <= 50:
                counter[i] = a.count(i)
            else:
                return

        print(("Counter(", counter, ")"))

    else:
        return
    # Write code here


main()
