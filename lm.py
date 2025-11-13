

p = 23
g = 5

a = 6
b = 15

A = pow(g, a, p)
B = pow(g, b, p)

shared_alice = pow(B, a, p)
shared_bob = pow(A, b, p)

print("Public prime p:", p)
print("Generator g:", g)
print("Alice's public key A:", A)
print("Bob's public key B:", B)
print("Shared secret (Alice):", shared_alice)
print("Shared secret (Bob):  ", shared_bob)
print("Shared keys equal? ->", shared_alice == shared_bob)
