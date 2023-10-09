From God import Secret
P1 = 41659
P2 = 61043
M = P1*P2

def bbs(n, seed):
    a = 0
    for i in range(n):
        if (seed & 1) == 1:
            a += (1 << i)
        seed = seed*seed % M
    return a


def f(n, k):
    return (3*n + 7) ^ k

def obfuscator(difficulty, number_to_cypher):
    seed = 3456
    for i in range(difficulty):
        number_to_cypher = f(number_to_cypher, bbs(difficulty, seed))
        seed += 20
    return number_to_cypher

cyphered = obfuscator(10, Secret)
print(cyphered) #272644738