import sys


def reverse(S, K):
    res = ''
    for i in range(K):
        res += '+' if S[i] == '-' else '-'
    return res


def calc(S, K):
    if not S:
        return 0
    if S[0] == '-':
        if len(S) < K:
            return -1
        else:
            count = calc(reverse(S[1:K], K-1) + S[K:], K)
            if count < 0:
                return -1
            else:
                return 1 + count
    else:
        return calc(S[1:], K)


def A():
    sys.setrecursionlimit(1200)
    #with open('A-small-attempt0.in', 'r') as infile:
    with open('A-large.in', 'r') as infile:
        with open('output.txt', 'w') as outfile:
            T = int(infile.readline().strip())
            for t in range(T):
                line = infile.readline().split()
                S = line[0]
                K = int(line[1])

                count = calc(S, K)

                if count < 0:
                    outfile.write('Case #%d: IMPOSSIBLE\n' % (t+1))
                else:
                    outfile.write('Case #%d: %d\n' % (t+1, count))
