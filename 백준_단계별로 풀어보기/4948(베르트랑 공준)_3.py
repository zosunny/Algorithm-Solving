N = 123456 * 2 + 1
sieve = [True] * N

for i in range(2, int(N**0.5)+1):
    if sieve[i]:
        for j in range(2*i, N, i):
            sieve[j] = False

def prime_cnt(n):
    cnt = 0
    for i in range(n+1, n*2+1):
        if sieve[i]:
            cnt += 1
    print(cnt)

while True:
    n = int(input())
    if n == 0:
        break
    prime_cnt(n)