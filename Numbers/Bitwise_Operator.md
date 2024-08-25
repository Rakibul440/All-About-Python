# Bitwise operators and operations in Python:

## Bitwise Operators:

1. & (Bitwise AND)
2. | (Bitwise OR)
3. ^ (Bitwise XOR)
4. ~ (Bitwise NOT)
5. << (Left Shift)
6. '>>' (Right Shift)

## Bitwise Operations:

1. Bitwise AND: Compares each bit of the first operand to the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the result bit is set to 0.

>> Example: 5 & 3 returns 1 (because 101 & 011 = 001)

1. Bitwise OR: Compares each bit of the first operand to the corresponding bit of the second operand. If either bit is 1, the corresponding result bit is set to 1. Otherwise, the result bit is set to 0.

>> Example: 5 | 3 returns 7 (because 101 | 011 = 111)

1. Bitwise XOR: Compares each bit of the first operand to the corresponding bit of the second operand. If the bits are different, the corresponding result bit is set to 1. Otherwise, the result bit is set to 0.

>> Example: 5 ^ 3 returns 6 (because 101 ^ 011 = 110)

1. Bitwise NOT: Flips all the bits of the operand.

>> Example: ~5 returns -6 (because ~00000101 = 11111010)

1. Left Shift: Shifts the bits of the operand to the left and fills 0 on voids left as a result.

>> Example: 5 << 2 returns 20 (because 00000101 << 2 = 00010100)

1. Right Shift: Shifts the bits of the operand to the right and fills 0 on voids left as a result.

>> Example: 5 >> 2 returns 1 (because 00000101 >> 2 = 00000001)

These bitwise operators and operations are useful for manipulating binary data, performing bit-level operations, and optimizing certain algorithms.