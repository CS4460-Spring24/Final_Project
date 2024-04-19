### Problem: Extract the flag in one of these messages, all of which were encrypted with the same
###          one-time pad


# This key is literally getting reused for every single char.
# In practice, this would be a stream cipher--each char would have a different mask
# but since the XOR removes the key and the original messages are not made available
# in the challenge, this isn't relevant here.
k = 0b00001011

m1 = [k ^ ord(c) for c in 'can I have the flag']
m2 = [k ^ ord(c) for c in 'the flag is dustbin']
m3 = [k ^ ord(c) for c in 'thanks for the flag']

m12 = [c1 ^ c2 for c1, c2 in zip(m1, m2)]
m13 = [c1 ^ c3 for c1, c3 in zip(m1, m3)]
m23 = [c2 ^ c3 for c2, c3 in zip(m2, m3)]


def printXor(m, title):
    print(title)
    for c in m:
        print(f"{c:>08b} ", end="")
    print()


print(f"Space is: {ord(' '):>08b}")
printXor(m12, f"m1 XOR m2")
printXor(m13, f"m1 XOR m3")
printXor(m23, f"m2 XOR m3")

