
sharedPrime = int(input("\nEnter the value of p(shared prime)"))
sharedBase = int(input("\nEnter the value of g(shared base)"))

aliceSecret = int(input("\nEnter the value of a(alice secret)"))
bobSecret = int(input("\nEnter the value of a(bob secret)"))


print("\nPublicly Shared Variables:")
print("    Publicly Shared Prime: ", sharedPrime)
print("    Publicly Shared Base:  ", sharedBase)


A = (sharedBase**aliceSecret) % sharedPrime
print("\n  Alice Sends Over Public Chanel: ", A)


B = (sharedBase ** bobSecret) % sharedPrime
print("  Bob Sends Over Public Chanel: ", B)

print("\n------------\n")
print("Privately Calculated Shared Secret:")
aliceSharedSecret = (B ** aliceSecret) % sharedPrime
print("    Alice Shared Secret: ", aliceSharedSecret)

bobSharedSecret = (A**bobSecret) % sharedPrime
print("    Bob Shared Secret: ", bobSharedSecret)
