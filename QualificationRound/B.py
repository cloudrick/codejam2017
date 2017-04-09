
def B():
    with open('B-large.in', 'r') as infile:
    #with open('input.txt', 'r') as infile:
        with open('output.txt', 'w') as outfile:
            T = int(infile.readline().strip())
            for t in range(T):
                line = ''
                result = infile.readline().strip()

                while result != line:
                    line = result
                    result = ''
                    for idx in range(len(line)):
                        if idx != len(line)-1 and line[idx] > line[idx+1]:
                            if result or line[idx] != '1':
                                result += str(int(line[idx]) - 1)
                            result += '9' * (len(line)-idx-1)
                            break
                        else:
                            result += line[idx]

                outfile.write('Case #%d: %s\n' % (t+1, result))
