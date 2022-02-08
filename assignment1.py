secret = 'WAUXZOZOXGQNTBPOESXQNBOHBFOKKXTOACAUZCQZKBXKKQTNFONBQNMZWEBATZXEPWCAZBPOCQZKBEXZBACBPQKXKKQTNFONBOFXQSBPQKESXQNBOHBCQSOXNGGOKMZQDOBPOKUDKBQBUBQANMQEPOZUKOGCAZONMZWEBQANCAZBPOKOMANGEXZBQFESOFONBXGQCCOZONBKOMZOBYOWONMZWEBQANXNGGOMZWEBQANKMPOFOCAZBOHBCQSOKXNGKUDFQBWAUZKAUZMOXSANTRQBPGAMUFONBXBQANXNGBOKBQNTCAZWAUZQFESOFONBXBQANUKQNTXEZATZXFFQNTSXNTUXTOACWAUZMPAQMOCAZBPOBPQZGEXZBGOBOZFQNOBPOKBXBQKBQMXSEZACQSOKACONTSQKPXNGXNABPOZSXNTUXTODWRZQBQNTXEZATZXFBAMAFEUBOBPOQZONBZAEQOKAIOZXSXZTOBOHBMAZEUKGAOKBPOKOMANGSXNTUXTOPXIOXPQTPOZONBZAEWBPXNONTSQKPBPQKXKKQTNFONBQKGUODWBPOFQGGSOACCODZUXZW'

"""
I guessed that this message would contain the word 'CRYPTOGRAPHY'.
"""

for i in range(len(secret) - 10):
    if ord(secret[i]) == ord(secret[i + 6]) and ord(secret[i + 1]) == ord(secret[i + 10]) and ord(secret[i + 2]) == ord(secret[i + 8]):
        print(secret[i-1], secret[i], secret[i+1], secret[i+2], secret[i+3], secret[i+4], secret[i+5], secret[i+6], secret[i+7], secret[i+8], secret[i+9], secret[i+10])

"""
I found out that MZWEBATZXEPW is CRYPTOGRAPHY.
For the convenience, I changed the uppercase to lowercase.
"""

print('#1')
for alphabet in secret:
    if alphabet == 'M':
        print('c', end='')
    elif alphabet == 'Z':
        print('r', end='')
    elif alphabet == 'W':
        print('y', end='')
    elif alphabet == 'E':
        print('p', end='')
    elif alphabet == 'B':
        print('t', end='')
    elif alphabet == 'A':
        print('o', end='')
    elif alphabet == 'T':
        print('g', end='')
    elif alphabet == 'X':
        print('a', end='')
    elif alphabet == 'P':
        print('h', end='')
    else:
        print('_', end='')

"""
I guessed that U is U, O is E.
"""

print()
print('#2')
for alphabet in secret:
    if alphabet == 'M':
        print('c', end='')
    elif alphabet == 'Z':
        print('r', end='')
    elif alphabet == 'W':
        print('y', end='')
    elif alphabet == 'E':
        print('p', end='')
    elif alphabet == 'B':
        print('t', end='')
    elif alphabet == 'A':
        print('o', end='')
    elif alphabet == 'T':
        print('g', end='')
    elif alphabet == 'X':
        print('a', end='')
    elif alphabet == 'P':
        print('h', end='')
    elif alphabet == 'U':
        print('u', end='')
    elif alphabet == 'O':
        print('e', end='')
    else:
        print('_', end='')

"""
I guessed that G is D, Q is I, N is N.
"""

print()
print('#3')
for alphabet in secret:
    if alphabet == 'M':
        print('c', end='')
    elif alphabet == 'Z':
        print('r', end='')
    elif alphabet == 'W':
        print('y', end='')
    elif alphabet == 'E':
        print('p', end='')
    elif alphabet == 'B':
        print('t', end='')
    elif alphabet == 'A':
        print('o', end='')
    elif alphabet == 'T':
        print('g', end='')
    elif alphabet == 'X':
        print('a', end='')
    elif alphabet == 'P':
        print('h', end='')
    elif alphabet == 'U':
        print('u', end='')
    elif alphabet == 'O':
        print('e', end='')
    elif alphabet == 'G':
        print('d', end='')
    elif alphabet == 'Q':
        print('i', end='')
    elif alphabet == 'N':
        print('n', end='')
    else:
        print('_', end='')

"""
I guessed that C is F.
"""

print()
print('#4')
for alphabet in secret:
    if alphabet == 'M':
        print('c', end='')
    elif alphabet == 'Z':
        print('r', end='')
    elif alphabet == 'W':
        print('y', end='')
    elif alphabet == 'E':
        print('p', end='')
    elif alphabet == 'B':
        print('t', end='')
    elif alphabet == 'A':
        print('o', end='')
    elif alphabet == 'T':
        print('g', end='')
    elif alphabet == 'X':
        print('a', end='')
    elif alphabet == 'P':
        print('h', end='')
    elif alphabet == 'U':
        print('u', end='')
    elif alphabet == 'O':
        print('e', end='')
    elif alphabet == 'G':
        print('d', end='')
    elif alphabet == 'Q':
        print('i', end='')
    elif alphabet == 'N':
        print('n', end='')
    elif alphabet == 'C':
        print('f', end='')
    else:
        print('_', end='')

"""
I guessed that S is L, H is X, K is S, F is M.
"""

print()
print('#5')
for alphabet in secret:
    if alphabet == 'M':
        print('c', end='')
    elif alphabet == 'Z':
        print('r', end='')
    elif alphabet == 'W':
        print('y', end='')
    elif alphabet == 'E':
        print('p', end='')
    elif alphabet == 'B':
        print('t', end='')
    elif alphabet == 'A':
        print('o', end='')
    elif alphabet == 'T':
        print('g', end='')
    elif alphabet == 'X':
        print('a', end='')
    elif alphabet == 'P':
        print('h', end='')
    elif alphabet == 'U':
        print('u', end='')
    elif alphabet == 'O':
        print('e', end='')
    elif alphabet == 'G':
        print('d', end='')
    elif alphabet == 'Q':
        print('i', end='')
    elif alphabet == 'N':
        print('n', end='')
    elif alphabet == 'C':
        print('f', end='')
    elif alphabet == 'S':
        print('l', end='')
    elif alphabet == 'H':
        print('x', end='')
    elif alphabet == 'K':
        print('s', end='')
    elif alphabet == 'F':
        print('m', end='')
    else:
        print('_', end='')

"""
I guessed that D is b.
"""

print()
print('#6')
for alphabet in secret:
    if alphabet == 'M':
        print('c', end='')
    elif alphabet == 'Z':
        print('r', end='')
    elif alphabet == 'W':
        print('y', end='')
    elif alphabet == 'E':
        print('p', end='')
    elif alphabet == 'B':
        print('t', end='')
    elif alphabet == 'A':
        print('o', end='')
    elif alphabet == 'T':
        print('g', end='')
    elif alphabet == 'X':
        print('a', end='')
    elif alphabet == 'P':
        print('h', end='')
    elif alphabet == 'U':
        print('u', end='')
    elif alphabet == 'O':
        print('e', end='')
    elif alphabet == 'G':
        print('d', end='')
    elif alphabet == 'Q':
        print('i', end='')
    elif alphabet == 'N':
        print('n', end='')
    elif alphabet == 'C':
        print('f', end='')
    elif alphabet == 'S':
        print('l', end='')
    elif alphabet == 'H':
        print('x', end='')
    elif alphabet == 'K':
        print('s', end='')
    elif alphabet == 'F':
        print('m', end='')
    elif alphabet == 'D':
        print('b', end='')
    else:
        print('_', end='')


"""
For the convenience, I arranged in alphabetical order.
I guessed that R is W, I is V, Y is K.
"""

print()
print('#7')
for alphabet in secret:
    if alphabet == 'A':
        print('o', end='')
    elif alphabet == 'B':
        print('t', end='')
    elif alphabet == 'C':
        print('f', end='')
    elif alphabet == 'D':
        print('b', end='')
    elif alphabet == 'E':
        print('p', end='')
    elif alphabet == 'F':
        print('m', end='')
    elif alphabet == 'G':
        print('d', end='')
    elif alphabet == 'H':
        print('x', end='')
    elif alphabet == 'I':
        print('v', end='')
    elif alphabet == 'K':
        print('s', end='')
    elif alphabet == 'M':
        print('c', end='')
    elif alphabet == 'N':
        print('n', end='')
    elif alphabet == 'O':
        print('e', end='')
    elif alphabet == 'P':
        print('h', end='')
    elif alphabet == 'Q':
        print('i', end='')
    elif alphabet == 'R':
        print('w', end='')
    elif alphabet == 'S':
        print('l', end='')
    elif alphabet == 'T':
        print('g', end='')
    elif alphabet == 'U':
        print('u', end='')
    elif alphabet == 'W':
        print('y', end='')
    elif alphabet == 'X':
        print('a', end='')
    elif alphabet == 'Y':
        print('k', end='')
    elif alphabet == 'Z':
        print('r', end='')
    else:
        print('_', end='')

"""
you are reading the plain text message of our first assignment in cryptography
for the first part of this assignment email this plain text file and describe the substitution cipher used for encryption
for the second part implement a different secret key encryption and decryption scheme for text files and submit your
source along with documentation and testing for your implementation using a programming language of your choice
for the third part determine the statistical profiles of english and another language by writing a program to compute
their entropies over a large text corpus does the second language have a higher entropy than english this assignment is
due by the middle of february

You are reading the plain text message of our first assignment in cryptography.
For the first part of this assignment email this plain text file and describe the substitution cipher used for encryption.
For the second part implement a different secret key encryption and decryption scheme for text files and submit your
source along with documentation and testing for your implementation using a programming language of your choice.
For the third part determine the statistical profiles of english and another language by writing a program to compute
their entropies over a large text corpus does the second language have a higher entropy than english.
This assignment is due by the middle of February.
"""