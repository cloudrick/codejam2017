
import copy


def split(n):
    if n % 2:
        return int(n/2), int(n/2)
    else:
        return n/2, max(n/2-1, 0)


def C():
    with open('C-large-practice.in', 'r') as infile:
    #with open('input.txt', 'r') as infile:
        with open('output.txt', 'w') as outfile:
            T = int(infile.readline().strip())
            for t in range(T):
                line = infile.readline().split()
                N = int(line[0])
                K = int(line[1])

                data = {N: 1}
                L = R = 0

                while K > 0:
                    cur_data = copy.deepcopy(data)
                    new_data = {}
                    for key in sorted(cur_data, reverse=True):
                        if data[key] >= K:
                            L, R = split(key)
                            K = 0
                            break
                        else:
                            l, r = split(key)
                            if l not in new_data:
                                new_data[l] = 0
                            if r not in new_data:
                                new_data[r] = 0
                            new_data[l] += data[key]
                            new_data[r] += data[key]
                            K -= data[key]

                    data = new_data

                outfile.write('Case #%d: %d %d\n' % (t+1, L, R))
